from tkinter import *
from tkinter.font import Font

# ——— 数据读取函数 ———
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
            allergens_list.append(parts[5])  # 例如
    return name_list, calorie_list, fat_list, sugar_list, category_list, allergens_list

# ——— 回调函数 ———
def search():
    # TODO: 搜索逻辑
    pass

def get_ai_advice():
    # TODO: AI 建议逻辑
    pass

def update_filters(*args):
    sel_cat = category_var.get()

    # “All” 代表用户对所有列出的过敏源都过敏
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
    for name, cat, allerg_str in zip(all_name_list, all_category_list, all_allergens_list):
        # 分类过滤
        if sel_cat != "All" and cat != sel_cat:
            continue

        # 过敏源过滤：如果食品含有 to_filter 中的任何一种，则跳过
        allerg_items = allerg_str.split(";") if allerg_str else []
        if any(a in allerg_items for a in to_filter):
            continue

        name_listbox.insert(END, name)

# ——— 读取数据 ———
all_name_list, _, _, _, all_category_list, all_allergens_list = generate_list_mcd("mcd_clean.csv")

# ——— 主窗口设置 ———
root = Tk()
root.title("ICS3U Final Performance Task")
root.geometry("1920x720")
root.configure(bg="red")

# 分割左右两部分
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2, minsize=900)
root.grid_columnconfigure(1, weight=3, minsize=1000)

# 左侧面板
left_frame = Frame(root, bg="red")
left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# 右侧面板
right_frame = Frame(root, bg="red")
right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

# ——— 左侧布局 ———
left_frame.grid_columnconfigure(0, weight=1, minsize=300)
left_frame.grid_columnconfigure(1, weight=1, minsize=300)
left_frame.grid_columnconfigure(2, weight=2, minsize=400)

title_font = Font(family="Arial", size=64, weight="bold")
Label(left_frame, text="ICS3U1-FPT", font=title_font, fg="white", bg="red")\
    .grid(row=0, column=0, columnspan=2, sticky="w")

# SEARCH & GO
search_entry = Entry(left_frame,
                     font=("Arial", 32),
                     fg="white",
                     bg="#FF8C00",
                     insertbackground="white")
search_entry.insert(0, "SEARCH :")
search_entry.grid(row=1, column=0, columnspan=2, sticky="we", pady=20, ipady=10)

go_button = Button(left_frame,
                   text="GO",
                   font=("Arial", 32),
                   fg="white",
                   bg="#FF8C00",
                   command=search)
go_button.grid(row=1, column=2,
               rowspan=2,
               sticky="we",
               pady=20,
               padx=(20,0),
               ipady=40)

Button(left_frame,
       text="Get some advice from AI :",
       font=("Arial", 28),
       fg="white",
       bg="#FF8C00",
       anchor="w",
       command=get_ai_advice)\
    .grid(row=2, column=0, columnspan=2, sticky="we", pady=20, ipady=10)

# 滑块 + Spinbox
cal_var = DoubleVar()
fat_var = DoubleVar()
sug_var = DoubleVar()

Label(left_frame, text="MAX CAL", font=("Arial", 24), fg="white", bg="red")\
    .grid(row=3, column=0, sticky="w", pady=5)
Spinbox(left_frame, from_=0, to=1880, font=("Arial", 16), textvariable=cal_var, width=8)\
    .grid(row=3, column=1, sticky="w")
Scale(left_frame, variable=cal_var, from_=0, to=1880,
      orient=HORIZONTAL, length=400, command=lambda e: None)\
    .grid(row=3, column=2, sticky="w")

Label(left_frame, text="MAX FAT", font=("Arial", 24), fg="white", bg="red")\
    .grid(row=4, column=0, sticky="w", pady=5)
Spinbox(left_frame, from_=0, to=118, font=("Arial", 16), textvariable=fat_var, width=8)\
    .grid(row=4, column=1, sticky="w")
Scale(left_frame, variable=fat_var, from_=0, to=118,
      orient=HORIZONTAL, length=400, command=lambda e: None)\
    .grid(row=4, column=2, sticky="w")

Label(left_frame, text="MAX SGR", font=("Arial", 24), fg="white", bg="red")\
    .grid(row=5, column=0, sticky="w", pady=5)
Spinbox(left_frame, from_=0, to=155 , font=("Arial", 16), textvariable=sug_var, width=8)\
    .grid(row=5, column=1, sticky="w")
Scale(left_frame, variable=sug_var, from_=0, to=155,
      orient=HORIZONTAL, length=400, command=lambda e: None)\
    .grid(row=5, column=2, sticky="w")

# 分类下拉菜单
options = [
    "All",
    "Snacks & Sides", "Burgers & Sandwiches", "Chicken & Fish", "Desserts & Shakes",
    "McCafe", "Beverages", "Condiments", "Breakfast","Salads","All Day Breakfast"
]
category_var = StringVar(value="All")
optmenu = OptionMenu(left_frame, category_var, *options, command=update_filters)
optmenu.config(font=("Arial", 20), fg="white", bg="red", highlightthickness=0)
optmenu["menu"].config(font=("Arial", 20), bg="white")
optmenu.grid(row=6, column=0, columnspan=2, sticky="we", pady=20)

# ——— 右侧：过敏源多选（Checkbutton） ———
gluten_var  = BooleanVar()
egg_var     = BooleanVar()
milk_var    = BooleanVar()
soya_var    = BooleanVar()
sesame_var  = BooleanVar()
all_var     = BooleanVar()  # “All” 表示对所有列出过敏源都过敏

right_frame.grid_rowconfigure(0, weight=0)
right_frame.grid_rowconfigure(1, weight=0)
right_frame.grid_rowconfigure(2, weight=1)
right_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_columnconfigure(1, weight=1)
right_frame.grid_columnconfigure(2, weight=1)

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

# ——— 右侧 Listbox ———
name_var = StringVar(value=all_name_list)
name_listbox = Listbox(right_frame,
                       listvariable=name_var,
                       selectmode=SINGLE,
                       font=("Arial",14),
                       bg="white",
                       fg="black")
name_listbox.grid(row=2, column=0, columnspan=3, sticky="nsew")

root.mainloop()
