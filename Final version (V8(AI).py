from tkinter import *
from tkinter.font import Font
import difflib
import requests
import json

#pip install requests json difflib

#Teacher, if you are looking at this code,
# I would be very grateful that you would be willing to spend one more minute to experience the
# AI search function I wrote. I am just interested in this so I want to write it in.
# The final score can be calculated according to my final version.(v5.py)
# This version only changes the part of the get_random_one function, and you can jump directly.
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
            if len(parts) < 6:
                continue
            name_list.append(parts[0])
            calorie_list.append(int(parts[1]))
            fat_list.append(float(parts[2]))
            sugar_list.append(int(parts[3]))
            category_list.append(parts[4])
            allergens_list.append(parts[5])  # 例如 "Egg;Milk"
    return name_list, calorie_list, fat_list, sugar_list, category_list, allergens_list

#头疼
def search():
    query = search_entry.get().strip()
    if query.lower() in ("", "search :", "search:"):
        query = ""
    sel_cat = category_var.get()
    max_cal = cal_var.get()
    max_fat = fat_var.get()
    max_sug = sug_var.get()
    if all_var.get():
        to_filter = ["Cereal Containing gluten", "Egg", "Milk", "Soya", "Sesame"]
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
        # 分类过滤
        if sel_cat != "All" and cat != sel_cat:
            continue
        # 过敏源过滤
        allerg_items = allerg_str.split(";") if allerg_str else []
        if any(a in allerg_items for a in to_filter):
            continue
        # 阈值过滤
        if cal > max_cal or fat > max_fat or sug > max_sug:
            continue
        # 搜索匹配
        if query and query.lower() not in name.lower():
            continue
        results.append(name)

    if not results and query:
        close = difflib.get_close_matches(query, all_name_list, n=10, cutoff=0.5)
        results = close if close else []

    if results:
        for item in results:
            name_listbox.insert(END, item)
    else:
        name_listbox.insert(END, "No matches found")

def get_ai_advice():
    # ai search (the API of this API provider always fails. If you can't run it,
    # you can regenerate a free API(this is web https://openrouter.ai)
    max_cal = cal_var.get()
    max_fat = fat_var.get()
    max_sug = sug_var.get()
    sel_cat = category_var.get()

    if all_var.get():
        selected_allergens = ["All"]
    else:
        selected_allergens = []
        if gluten_var.get():  selected_allergens.append("gluten")
        if egg_var.get():     selected_allergens.append("egg")
        if milk_var.get():    selected_allergens.append("milk")
        if soya_var.get():    selected_allergens.append("soya")
        if sesame_var.get():  selected_allergens.append("sesame")

    items = name_listbox.get(0, END)
    items_str = ", ".join(items) if items else "None"

    prompt = (
        f"请基于以下条件推荐一款麦当劳产品，给出原因（鉴于你.....所以推荐...因为里面含有....回答不超过50字）英文输出：\n"
        f"类别：{sel_cat}；最大热量：{max_cal}；最大脂肪：{max_fat}；"
        f"最大糖分：{max_sug}；避开过敏源：{','.join(selected_allergens)}；"
        f"可选项列表：{items_str}"
    )

    try:
        resp = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer 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",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://yourdomain.com",
                "X-Title": "Studio",
            },
            data=json.dumps({
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
            })
        )
        resp.raise_for_status()
        data = resp.json()
        answer = data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        answer = f"ai request failed, you can try to replace api：{e}"

    Aiseed.set(answer)


def update_filters(*args):
    search()


all_name_list, all_calorie_list, all_fat_list, all_sugar_list, all_category_list, all_allergens_list = \
    generate_list_mcd("mcd_clean.csv")

root = Tk()
root.title("ICS3U Final Performance Task")
root.geometry("1920x800")
root.configure(bg="red")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2, minsize=900)
root.grid_columnconfigure(1, weight=3, minsize=1000)

# 左侧
left_frame = Frame(root, bg="red")
left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
left_frame.grid_columnconfigure(0, weight=1, minsize=300)
left_frame.grid_columnconfigure(1, weight=1, minsize=300)
left_frame.grid_columnconfigure(2, weight=2, minsize=400)

# 右侧
right_frame = Frame(root, bg="red")
right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
right_frame.grid_rowconfigure(0, weight=0)
right_frame.grid_rowconfigure(1, weight=0)
right_frame.grid_rowconfigure(2, weight=1)
for c in range(3):
    right_frame.grid_columnconfigure(c, weight=1)

#左侧内容
title_font = Font(family="Arial", size=64, weight="bold")
Label(left_frame, text="ICS3U1-FPT", font=title_font, fg="white", bg="red")\
    .grid(row=0, column=0, columnspan=2, sticky="w")

# 搜索框
search_entry = Entry(left_frame,
                     font=("Arial", 32),
                     fg="white",
                     bg="#FF8C00",
                     insertbackground="white")
search_entry.insert(0, "SEARCH :")
search_entry.grid(row=1, column=0, columnspan=2, sticky="we", pady=20, ipady=10)

#奇怪小ADD.........................
def on_search_focus_in(event):
    if search_entry.get() in ("SEARCH :", "SEARCH:"):
        search_entry.delete(0, END)


search_entry.bind("<FocusIn>", on_search_focus_in)

# GO
go_button = Button(left_frame, text="GO", font=("Arial", 32),
                   fg="white", bg="#FF8C00", command=search)
go_button.grid(row=1, column=2, rowspan=2, sticky="we",
               pady=20, padx=(20,0), ipady=40)

Button(left_frame, text="get ai advice",
       font=("Arial", 28), fg="white", bg="#FF8C00",
       anchor="w", command=get_ai_advice)\
    .grid(row=2, column=0, columnspan=2, sticky="we",
          pady=20, ipady=10)

#Spinbox
cal_var = DoubleVar(value=max(all_calorie_list))
fat_var = DoubleVar(value=max(all_fat_list))
sug_var = DoubleVar(value=max(all_sugar_list))

Label(left_frame, text="MAX CAL", font=("Arial", 24),
      fg="white", bg="red").grid(row=3, column=0, sticky="w", pady=5)
Spinbox(left_frame, from_=0, to=max(all_calorie_list),
        textvariable=cal_var, font=("Arial",16), width=8).grid(row=3, column=1, sticky="w")
Scale(left_frame, variable=cal_var, from_=0, to=max(all_calorie_list),
      orient=HORIZONTAL, length=250, sliderlength=30,
      command=update_filters).grid(row=3, column=2, sticky="w")

Label(left_frame, text="MAX FAT", font=("Arial", 24),
      fg="white", bg="red").grid(row=4, column=0, sticky="w", pady=5)
Spinbox(left_frame, from_=0, to=max(all_fat_list),
        textvariable=fat_var, font=("Arial",16), width=8).grid(row=4, column=1, sticky="w")
Scale(left_frame, variable=fat_var, from_=0, to=max(all_fat_list),
      orient=HORIZONTAL, length=250, sliderlength=30,
      command=update_filters).grid(row=4, column=2, sticky="w")

Label(left_frame, text="MAX SGR", font=("Arial", 24),
      fg="white", bg="red").grid(row=5, column=0, sticky="w", pady=5)
Spinbox(left_frame, from_=0, to=max(all_sugar_list),
        textvariable=sug_var, font=("Arial",16), width=8).grid(row=5, column=1, sticky="w")
Scale(left_frame, variable=sug_var, from_=0, to=max(all_sugar_list),
      orient=HORIZONTAL, length=250, sliderlength=30,
      command=update_filters).grid(row=5, column=2, sticky="w")

#分类下拉菜单
options = ["All"] + sorted(set(all_category_list))
category_var = StringVar(value="All")
optmenu = OptionMenu(left_frame, category_var, *options, command=update_filters)
optmenu.config(font=("Arial",20), fg="white", bg="red", highlightthickness=0)
optmenu["menu"].config(font=("Arial",20), bg="white")
optmenu.grid(row=6, column=0, columnspan=2, sticky="we", pady=20)

Aiseed = StringVar()
Aiseed_msg = Message(left_frame, textvariable=Aiseed,
    fg="white", bg="red", font=("Arial",20), width=850)
Aiseed_msg.grid(row=7, column=0, columnspan=3, rowspan=2, sticky="wn", pady=10)

#右侧
gluten_var  = BooleanVar()
egg_var     = BooleanVar()
milk_var    = BooleanVar()
soya_var    = BooleanVar()
sesame_var  = BooleanVar()
all_var     = BooleanVar()

Checkbutton(right_frame, text="Cereal Containing gluten", variable=gluten_var,
            font=("Arial",16), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters)\
    .grid(row=0, column=0, sticky="w", padx=5, pady=5)
Checkbutton(right_frame, text="Egg", variable=egg_var,
            font=("Arial",16), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters)\
    .grid(row=0, column=1, sticky="w", padx=5, pady=5)
Checkbutton(right_frame, text="Milk", variable=milk_var,
            font=("Arial",16), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters)\
    .grid(row=0, column=2, sticky="w", padx=5, pady=5)

Checkbutton(right_frame, text="Soya", variable=soya_var,
            font=("Arial",16), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters)\
    .grid(row=1, column=0, sticky="w", padx=5, pady=5)
Checkbutton(right_frame, text="Sesame", variable=sesame_var,
            font=("Arial",16), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters)\
    .grid(row=1, column=1, sticky="w", padx=5, pady=5)
Checkbutton(right_frame, text="All", variable=all_var,
            font=("Arial",16), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters)\
    .grid(row=1, column=2, sticky="w", padx=5, pady=5)

# 右侧DListbox
name_var = StringVar(value=all_name_list)
name_listbox = Listbox(right_frame, listvariable=name_var,
                       selectmode=SINGLE, font=("Arial",14),
                       bg="white", fg="black")
name_listbox.grid(row=2, column=0, columnspan=3, sticky="nsew")

root.mainloop()