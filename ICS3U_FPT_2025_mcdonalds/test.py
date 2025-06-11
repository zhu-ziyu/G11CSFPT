import tkinter as tk
from tkinter.font import Font

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

# ——— 回调函数占位 ———
def search():
    pass

def get_ai_advice():
    pass

def update_filters():
    pass

# ——— 读取数据 ———
all_name_list, *_ = generate_list_mcd("mcd_clean.csv")

# ——— 主窗口基础设置 ———
# ——— 主窗口基础设置 ———
root = tk.Tk()
root.title("ICS3U Final Performance Task")
root.geometry("1920x720")
# 暂时不要再把 root 背景设成纯红了
# root.configure(bg="red")

# ——— 下面这段，插入在 root.geometry(...) 之后 ———
# 创建一个 Canvas 覆盖整个窗口，用来绘制渐变
gradient_canvas = tk.Canvas(root, width=1920, height=720, highlightthickness=0)
gradient_canvas.grid(row=0, column=0, columnspan=2, sticky="nsew")

height = 720
for i in range(height):
    # 从红 (255,0,0) 渐变到橙 (255,140,0)
    r = 255
    g = int(140 * (i / (height - 1)))
    b = 0
    color = f"#{r:02x}{g:02x}{b:02x}"
    # 逐行画线实现渐变
    gradient_canvas.create_line(0, i, 1920, i, fill=color)


# 把 root 分成左右两部分
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2, minsize=900)   # 左侧 panel
root.grid_columnconfigure(1, weight=3, minsize=1000)  # 右侧 listbox

left_frame = tk.Frame(root, bg="red")
left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

right_frame = tk.Frame(root, bg="red")
right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

# ——— 左侧布局 ———
# 列宽分配：0 = 标签，1 = Spinbox/按钮，2 = Scale/Go
left_frame.grid_columnconfigure(0, weight=1, minsize=300)
left_frame.grid_columnconfigure(1, weight=1, minsize=300)
left_frame.grid_columnconfigure(2, weight=2, minsize=400)

# 标题 & logo
title_font = Font(family="Arial", size=64, weight="bold")
title_label = tk.Label(left_frame, text="ICS3U1-FPT", font=title_font, fg="white", bg="red")
title_label.grid(row=0, column=0, columnspan=2, sticky="w")

# 搜索框 & GO
search_entry = tk.Entry(left_frame,
                        font=("Arial", 32),
                        fg="white",
                        bg="#FF8C00",
                        insertbackground="white")
search_entry.insert(0, "SEARCH :")
search_entry.grid(row=1, column=0, columnspan=2, sticky="we", pady=20, ipady=10)


go_button = tk.Button(left_frame,
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


# AI 建议 按钮
ai_button = tk.Button(left_frame,
                      text="Get some advice from AI :",
                      font=("Arial", 28),
                      fg="white",
                      bg="#FF8C00",
                      anchor="w",
                      command=get_ai_advice)
ai_button.grid(row=2, column=0, columnspan=2, sticky="we", pady=10)

# 滑块 + Spinbox
cal_var = tk.DoubleVar()
fat_var = tk.DoubleVar()
sug_var = tk.DoubleVar()

# MAX CAL
lbl_cal = tk.Label(left_frame, text="MAX CAL", font=("Arial", 24), fg="white", bg="red")
lbl_cal.grid(row=3, column=0, sticky="w", pady=5)
sp_cal = tk.Spinbox(left_frame, from_=0, to=1000, font=("Arial", 16),
                    textvariable=cal_var, width=8)
sp_cal.grid(row=3, column=1, sticky="w")
sc_cal = tk.Scale(left_frame, variable=cal_var, from_=0, to=1000,
                  orient="horizontal", length=400, command=lambda e: None)
sc_cal.grid(row=3, column=2, sticky="w")

# MAX FAT
lbl_fat = tk.Label(left_frame, text="MAX FAT", font=("Arial", 24), fg="white", bg="red")
lbl_fat.grid(row=4, column=0, sticky="w", pady=5)
sp_fat = tk.Spinbox(left_frame, from_=0, to=200, font=("Arial", 16),
                    textvariable=fat_var, width=8)
sp_fat.grid(row=4, column=1, sticky="w")
sc_fat = tk.Scale(left_frame, variable=fat_var, from_=0, to=200,
                  orient="horizontal", length=400, command=lambda e: None)
sc_fat.grid(row=4, column=2, sticky="w")

# MAX SGR
lbl_sug = tk.Label(left_frame, text="MAX SGR", font=("Arial", 24), fg="white", bg="red")
lbl_sug.grid(row=5, column=0, sticky="w", pady=5)
sp_sug = tk.Spinbox(left_frame, from_=0, to=200, font=("Arial", 16),
                    textvariable=sug_var, width=8)
sp_sug.grid(row=5, column=1, sticky="w")
sc_sug = tk.Scale(left_frame, variable=sug_var, from_=0, to=200,
                  orient="horizontal", length=400, command=lambda e: None)
sc_sug.grid(row=5, column=2, sticky="w")

# Radiobuttons （左侧四个）
category_var = tk.StringVar()
rb_snack = tk.Radiobutton(left_frame, text="Snack & Sides",    variable=category_var,
                          value="Snack & Sides",    font=("Arial", 20),
                          fg="white", bg="red", selectcolor="black",
                          activebackground="red", command=update_filters)
rb_snack.grid(row=6, column=0, sticky="w", pady=5)

rb_burger = tk.Radiobutton(left_frame, text="Burger & Sandwiches", variable=category_var,
                           value="Burger & Sandwiches", font=("Arial", 20),
                           fg="white", bg="red", selectcolor="black",
                           activebackground="red", command=update_filters)
rb_burger.grid(row=7, column=0, sticky="w", pady=5)

rb_chicken = tk.Radiobutton(left_frame, text="Chicken & Fish", variable=category_var,
                            value="Chicken & Fish", font=("Arial", 20),
                            fg="white", bg="red", selectcolor="black",
                            activebackground="red", command=update_filters)
rb_chicken.grid(row=8, column=0, sticky="w", pady=5)

rb_desserts = tk.Radiobutton(left_frame, text="Desserts & Shakes", variable=category_var,
                             value="Desserts & Shakes", font=("Arial", 20),
                             fg="white", bg="red", selectcolor="black",
                             activebackground="red", command=update_filters)
rb_desserts.grid(row=9, column=0, sticky="w", pady=5)

# Radiobuttons （右侧四个）
rb_mccafe = tk.Radiobutton(left_frame, text="McCafe", variable=category_var,
                           value="McCafe", font=("Arial", 20),
                           fg="white", bg="red", selectcolor="black",
                           activebackground="red", command=update_filters)
rb_mccafe.grid(row=6, column=1, sticky="w", pady=5)

rb_beverages = tk.Radiobutton(left_frame, text="Beverages", variable=category_var,
                              value="Beverages", font=("Arial", 20),
                              fg="white", bg="red", selectcolor="black",
                              activebackground="red", command=update_filters)
rb_beverages.grid(row=7, column=1, sticky="w", pady=5)

rb_condiments = tk.Radiobutton(left_frame, text="Condiments", variable=category_var,
                               value="Condiments", font=("Arial", 20),
                               fg="white", bg="red", selectcolor="black",
                               activebackground="red", command=update_filters)
rb_condiments.grid(row=8, column=1, sticky="w", pady=5)

rb_breakfast = tk.Radiobutton(left_frame, text="Breakfast", variable=category_var,
                              value="Breakfast", font=("Arial", 20),
                              fg="white", bg="red", selectcolor="black",
                              activebackground="red", command=update_filters)
rb_breakfast.grid(row=9, column=1, sticky="w", pady=5)


# ——— 右侧 Listbox ———
right_frame.grid_rowconfigure(0, weight=0)
right_frame.grid_columnconfigure(0, weight=1)
name_var = tk.StringVar(value=all_name_list)
name_listbox = tk.Listbox(right_frame,
                          listvariable=name_var,
                          selectmode=tk.SINGLE,
                          font=("Arial", 14),
                          bg="white",
                          fg="black",
                        height = 30
                            )
name_listbox.grid(row=0, column=0, sticky="nsew")


# ——— 启动主循环 ———
root.mainloop()
