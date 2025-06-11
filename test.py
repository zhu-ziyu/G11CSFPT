import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import random

# ——— 数据读取函数（无需理解，可直接使用） ———
def generate_list_mcd(filename):
    name_list = []
    calorie_list = []
    fat_list = []
    sugar_list = []
    category_list = []
    allergens_list = []
    with open(filename, encoding="utf-8", errors='replace') as file_in:
        file_in.readline()  # 跳过表头
        for line in file_in:
            parts = line.strip().split(",")
            if len(parts) < 6:
                continue
            name_list.append(parts[0])
            calorie_list.append(int(parts[1]))
            fat_list.append(float(parts[2]))
            sugar_list.append(int(parts[3]))
            category_list.append(parts[4])
            allergens_list.append(parts[5])
    return name_list, calorie_list, fat_list, sugar_list, category_list, allergens_list

# ——— 回调函数实现 ———
def filter_items():
    """ 根据当前搜索框文本和各项过滤条件，返回符合条件的食品名称列表 """
    term = search_entry.get().lower().replace("search :", "").strip()
    max_cal = cal_var.get()
    max_fat = fat_var.get()
    max_sug = sug_var.get()
    selected_cat = category_var.get()

    results = []
    for name, cal, fat, sug, cat in zip(
        all_name_list, calorie_list, fat_list, sugar_list, category_list
    ):
        if term and term not in name.lower():
            continue
        if cal > max_cal or fat > max_fat or sug > max_sug:
            continue
        if selected_cat and cat != selected_cat:
            continue
        results.append(name)
    return results

def update_listbox(items):
    """ 更新右侧列表框显示 """
    name_listbox.delete(0, tk.END)
    for item in items:
        name_listbox.insert(tk.END, item)

def search():
    """ 点击 GO 后执行搜索+过滤 """
    matched = filter_items()
    update_listbox(matched)

def update_filters():
    """ 滑块或单选改变时自动刷新列表 """
    search()  # 逻辑一致

def get_ai_advice():
    """ 随机从当前过滤结果中给出 3 条“AI 建议” """
    current = filter_items()
    if not current:
        messagebox.showinfo("AI 建议", "未找到符合条件的项目，无法给出建议。")
        return
    suggestions = random.sample(current, min(3, len(current)))
    text = "我推荐你尝试：\n" + "\n".join(f"- {s}" for s in suggestions)
    messagebox.showinfo("AI 建议", text)

# ——— 读取数据 ———
all_name_list, calorie_list, fat_list, sugar_list, category_list, allergens_list = generate_list_mcd("mcd_clean.csv")

# ——— 主窗口基础设置 ———
root = tk.Tk()
root.title("ICS3U Final Performance Task")
root.geometry("1920x720")
root.configure(bg="red")

# 划分左右两部分
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2, minsize=900)
root.grid_columnconfigure(1, weight=3, minsize=1000)

left_frame = tk.Frame(root, bg="red")
left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
right_frame = tk.Frame(root, bg="red")
right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

# ——— 左侧布局 ———
left_frame.grid_columnconfigure(0, weight=1, minsize=300)
left_frame.grid_columnconfigure(1, weight=1, minsize=300)
left_frame.grid_columnconfigure(2, weight=2, minsize=400)

# 标题
title_font = Font(family="Arial", size=64, weight="bold")
tk.Label(left_frame, text="ICS3U1-FPT", font=title_font, fg="white", bg="red")\
    .grid(row=0, column=0, columnspan=2, sticky="w")

# 搜索框 & GO 按钮
search_entry = tk.Entry(
    left_frame, font=("Arial", 32), fg="white", bg="#FF8C00", insertbackground="white"
)
search_entry.insert(0, "SEARCH :")
search_entry.grid(row=1, column=0, columnspan=2, sticky="we", pady=20, ipady=10)

go_button = tk.Button(
    left_frame, text="GO", font=("Arial", 32), fg="white", bg="#FF8C00", command=search
)
go_button.grid(row=1, column=2, rowspan=2, sticky="we", pady=20, padx=(20,0), ipady=40)

# AI 建议按钮
ai_button = tk.Button(
    left_frame,
    text="Get some advice from AI :",
    font=("Arial", 28),
    fg="white",
    bg="#FF8C00",
    anchor="w",
    command=get_ai_advice,
)
ai_button.grid(row=2, column=0, columnspan=2, sticky="we", pady=10)

# 滑块及 Spinbox
cal_var = tk.DoubleVar(value=1000)
fat_var = tk.DoubleVar(value=200)
sug_var = tk.DoubleVar(value=200)

def make_slider(label, var, row, max_val):
    tk.Label(left_frame, text=label, font=("Arial", 24), fg="white", bg="red")\
        .grid(row=row, column=0, sticky="w", pady=5)
    tk.Spinbox(left_frame, from_=0, to=max_val, font=("Arial", 16),
               textvariable=var, width=8).grid(row=row, column=1, sticky="w")
    tk.Scale(left_frame, variable=var, from_=0, to=max_val,
             orient="horizontal", length=400,
             command=lambda e: update_filters()).grid(row=row, column=2, sticky="w")

make_slider("MAX CAL", cal_var, 3, 1000)
make_slider("MAX FAT", fat_var, 4, 200)
make_slider("MAX SGR", sug_var, 5, 200)

# 分类单选
category_var = tk.StringVar(value="")
cats = [
    ("Snack & Sides", 6, 0),
    ("Burger & Sandwiches", 7, 0),
    ("Chicken & Fish", 8, 0),
    ("Desserts & Shakes", 9, 0),
    ("McCafe", 6, 1),
    ("Beverages", 7, 1),
    ("Condiments", 8, 1),
    ("Breakfast", 9, 1),
]
for text, r, c in cats:
    tk.Radiobutton(
        left_frame,
        text=text,
        variable=category_var,
        value=text,
        font=("Arial", 20),
        fg="white",
        bg="red",
        selectcolor="black",
        activebackground="red",
        command=update_filters,
    ).grid(row=r, column=c, sticky="w", pady=5)

# ——— 右侧 Listbox ———
right_frame.grid_rowconfigure(0, weight=1)
right_frame.grid_columnconfigure(0, weight=1)
name_var = tk.StringVar(value=all_name_list)
name_listbox = tk.Listbox(
    right_frame,
    listvariable=name_var,
    selectmode=tk.SINGLE,
    font=("Arial", 14),
    bg="white",
    fg="black",
    height=30
)
name_listbox.grid(row=0, column=0, sticky="nsew")

# 初始加载全部项目
update_listbox(all_name_list)

# ——— 启动主循环 ———
root.mainloop()
