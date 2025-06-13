from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import difflib
import threading
import requests
import json

# ——— 数据读取函数 ———
def generate_list_mcd(filename):
    name_list = []
    calorie_list = []
    fat_list = []
    sugar_list = []
    category_list = []
    allergens_list = []
    with open(filename, encoding="utf-8", errors='replace') as file_in:
        file_in.readline()
        for line in file_in:
            parts = line.strip().split(",")
            if len(parts) < 6: continue
            name_list.append(parts[0])
            calorie_list.append(int(parts[1]))
            fat_list.append(float(parts[2]))
            sugar_list.append(int(parts[3]))
            category_list.append(parts[4])
            allergens_list.append(parts[5])
    return name_list, calorie_list, fat_list, sugar_list, category_list, allergens_list

# ——— 全局数据 ———
all_name_list, all_calorie_list, all_fat_list, all_sugar_list, all_category_list, all_allergens_list = \
    generate_list_mcd("mcd_clean.csv")

# ——— 搜索 / 筛选 逻辑 ———
def search():
    query = search_entry.get().strip()
    if query.lower() in ("", "search :", "search:"):
        query = ""
    sel_cat = category_var.get()
    max_cal = cal_var.get()
    max_fat = fat_var.get()
    max_sug = sug_var.get()
    if all_var.get():
        to_filter = ["Cereal Containing gluten","Egg","Milk","Soya","Sesame"]
    else:
        to_filter = []
        if gluten_var.get():  to_filter.append("Cereal Containing gluten")
        if egg_var.get():     to_filter.append("Egg")
        if milk_var.get():    to_filter.append("Milk")
        if soya_var.get():    to_filter.append("Soya")
        if sesame_var.get():  to_filter.append("Sesame")
    name_listbox.delete(0, END)
    results = []
    for name, cal, fat, sug, cat, allerg_str in zip(
        all_name_list,
        all_calorie_list,
        all_fat_list,
        all_sugar_list,
        all_category_list,
        all_allergens_list
    ):
        if sel_cat!="All" and cat!=sel_cat: continue
        items = allerg_str.split(";") if allerg_str else []
        if any(a in items for a in to_filter): continue
        if cal>max_cal or fat>max_fat or sug>max_sug: continue
        if query and query.lower() not in name.lower(): continue
        results.append(name)
    if not results and query:
        results = difflib.get_close_matches(query, all_name_list, n=10, cutoff=0.5)
    if results:
        for it in results:
            name_listbox.insert(END, it)
    else:
        name_listbox.insert(END, "No matches found")

def update_filters(*args):
    search()

# ——— 异步 AI 请求 + 进度条 ———
def _threaded_ai_call(prompt):
    """后台线程：向 OpenRouter 发送请求，返回结果后通过 root.after 更新 UI。"""
    try:
        resp = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                # 可选两行
                "HTTP-Referer": "https://yourdomain.com",
                "X-Title":      "Studio",
            },
            json={
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages":[{"role":"user","content":prompt}]
            },
            timeout=30
        )
        resp.raise_for_status()
        answer = resp.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        answer = f"AI 请求失败：{e}"
    # 回到主线程更新 UI
    root.after(0, _on_ai_result, answer)

def _on_ai_result(answer):
    """AI 请求完成后的主线程回调：停止进度条、启用按钮、显示结果。"""
    ai_progress.stop()
    ai_progress.grid_remove()
    ai_button.config(state=NORMAL)
    Aiseed.set(answer)

def get_ai_advice():
    """点击按钮时触发：构造 prompt，启动进度条并启动后台线程。"""
    # 构造 Prompt
    max_cal = cal_var.get(); max_fat = fat_var.get(); max_sug = sug_var.get()
    sel_cat = category_var.get()
    if all_var.get():
        sel_all = ["All"]
    else:
        sel_all = []
        if gluten_var.get(): sel_all.append("gluten")
        if egg_var.get():    sel_all.append("egg")
        if milk_var.get():   sel_all.append("milk")
        if soya_var.get():   sel_all.append("soya")
        if sesame_var.get(): sel_all.append("sesame")
    items = name_listbox.get(0, END)
    items_str = ", ".join(items) if items else "None"
    prompt = (
        f"Please recommend one McDonald's item (<=50 words) based on:\n"
        f"Category: {sel_cat}; Max Calories: {max_cal}; Max Fat: {max_fat}; Max Sugar: {max_sug};\n"
        f"Avoid allergens: {','.join(sel_all)}; Options: {items_str}"
    )
    # 禁用按钮、显示进度条
    ai_button.config(state=DISABLED)
    ai_progress.grid(row=2, column=0, columnspan=2, sticky="we", pady=5)
    ai_progress.start(10)
    # 启动后台线程
    threading.Thread(target=_threaded_ai_call, args=(prompt,), daemon=True).start()

# ——— GUI 初始化 ———
API_KEY = "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"  # ← 替换为你的有效 API Key

root = Tk()
root.title("ICS3U Final Performance Task")
root.geometry("1920x800")
root.configure(bg="red")

# split panels
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2, minsize=900)
root.grid_columnconfigure(1, weight=3, minsize=1000)

# 左侧
left_frame = Frame(root, bg="red")
left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
for i,w in enumerate((300,300,400)):
    left_frame.grid_columnconfigure(i, weight=1, minsize=w)

# 右侧
right_frame = Frame(root, bg="red")
right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
for r in range(3):
    right_frame.grid_rowconfigure(r, weight=(0 if r<2 else 1))
for c in range(3):
    right_frame.grid_columnconfigure(c, weight=1)

# 标题
title_font = Font(family="Arial", size=64, weight="bold")
Label(left_frame, text="ICS3U1-FPT", font=title_font, fg="white", bg="red")\
 .grid(row=0, column=0, columnspan=2, sticky="w")

# 搜索框
search_entry = Entry(left_frame, font=("Arial",32),
                     fg="white", bg="#FF8C00", insertbackground="white")
search_entry.insert(0, "SEARCH :")
search_entry.grid(row=1, column=0, columnspan=2, sticky="we", pady=20, ipady=10)
def on_search_focus_in(e):
    if search_entry.get().lower().startswith("search"):
        search_entry.delete(0, END)
search_entry.bind("<FocusIn>", on_search_focus_in)

# GO 按钮
Button(left_frame, text="GO", font=("Arial",32),
       fg="white", bg="#FF8C00", command=search)\
 .grid(row=1, column=2, rowspan=2, sticky="we",
       pady=20, padx=(20,0), ipady=40)

# AI 建议按钮
ai_button = Button(left_frame, text="Get some advice from AI :",
                   font=("Arial",28), fg="white", bg="#FF8C00",
                   anchor="w", command=get_ai_advice)
ai_button.grid(row=2, column=0, columnspan=2, sticky="we",
               pady=20, ipady=10)

# AI 进度条（隐藏）
ai_progress = ttk.Progressbar(left_frame, mode="indeterminate")
ai_progress.grid_remove()

# 滑块 + Spinbox
cal_var = DoubleVar(value=max(all_calorie_list))
fat_var = DoubleVar(value=max(all_fat_list))
sug_var = DoubleVar(value=max(all_sugar_list))
for idx,(label,var,mx,row) in enumerate([
    ("MAX CAL", cal_var, max(all_calorie_list), 3),
    ("MAX FAT", fat_var, max(all_fat_list),       4),
    ("MAX SGR", sug_var, max(all_sugar_list),     5),
]):
    Label(left_frame, text=label, font=("Arial",24), fg="white", bg="red")\
     .grid(row=row, column=0, sticky="w", pady=5)
    Spinbox(left_frame, from_=0, to=mx, textvariable=var,
            font=("Arial",16), width=8).grid(row=row, column=1, sticky="w")
    Scale(left_frame, variable=var, from_=0, to=mx,
          orient=HORIZONTAL, length=250, sliderlength=30,
          command=update_filters).grid(row=row, column=2, sticky="w")

# 分类下拉
options = ["All"]+sorted(set(all_category_list))
category_var = StringVar(value="All")
opt = OptionMenu(left_frame, category_var, *options, command=update_filters)
opt.config(font=("Arial",20), fg="white", bg="red", highlightthickness=0)
opt["menu"].config(font=("Arial",20), bg="white")
opt.grid(row=6, column=0, columnspan=2, sticky="we", pady=20)

# AI 输出
Aiseed = StringVar()
Aiseed_msg = Message(left_frame, textvariable=Aiseed,
    fg="white", bg="red", font=("Arial",20), width=850)
Aiseed_msg.grid(row=7, column=0, columnspan=3, rowspan=2, sticky="wn", pady=10)

# 过敏源多选
gluten_var=BooleanVar(); egg_var=BooleanVar(); milk_var=BooleanVar()
soya_var=BooleanVar(); sesame_var=BooleanVar(); all_var=BooleanVar()
for txt,var,r,c in [
    ("Cereal Containing gluten",gluten_var,0,0),
    ("Egg",egg_var,0,1),("Milk",milk_var,0,2),
    ("Soya",soya_var,1,0),("Sesame",sesame_var,1,1),
    ("All",all_var,1,2),
]:
    Checkbutton(right_frame, text=txt, variable=var,
        font=("Arial",16), fg="white", bg="red",
        selectcolor="black", activebackground="red",
        command=update_filters).grid(row=r, column=c,
        sticky="w", padx=5, pady=5)

# 结果列表
name_var = StringVar(value=all_name_list)
name_listbox = Listbox(right_frame, listvariable=name_var,
                      selectmode=SINGLE, font=("Arial",14),
                      bg="white", fg="black")
name_listbox.grid(row=2, column=0, columnspan=3, sticky="nsew")

root.mainloop()
