import tkinter as tk
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

# ——— 主窗口设置 ———
root = tk.Tk()
root.title("ICS3U Final Performance Task")
root.geometry("1920x720")
# 整体半透明
root.wm_attributes('-alpha', 0.95)

# ——— 渐变背景 Canvas ———
canvas = tk.Canvas(root, width=1920, height=720, highlightthickness=0)
canvas.place(x=0, y=0)
for i in range(720):
    g = int(165 * i / 719)
    color = f'#ff{g:02x}00'
    canvas.create_line(0, i, 1920, i, fill=color)

# ——— 左右 Frame 嵌入 Canvas ———
left_frame = tk.Frame(canvas, bg="red")
right_frame = tk.Frame(canvas, bg="red")
canvas.create_window((20, 20),   window=left_frame,  anchor='nw')
canvas.create_window((940, 20),  window=right_frame, anchor='nw')

# ——— 左侧布局 —— 使用 grid ——
left_frame.grid_columnconfigure(0, weight=1, minsize=300)
left_frame.grid_columnconfigure(1, weight=1, minsize=300)
left_frame.grid_columnconfigure(2, weight=2, minsize=400)

# 标题与 Logo
title_font = Font(family="Arial", size=64, weight="bold")
tk.Label(left_frame,
         text="ICS3U1-FPT",
         font=title_font,
         fg="white",
         bg="red"
        ).grid(row=0, column=0, columnspan=2, sticky="w")


# 搜索框 & GO
search_entry = tk.Entry(left_frame,
                        font=("Arial", 32),
                        fg="white",
                        bg="#FF8C00",
                        insertbackground="white")
search_entry.insert(0, "SEARCH :")
search_entry.grid(row=1, column=0, columnspan=2,
                  sticky="we", pady=20, ipady=10)

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

# AI 建议按钮
tk.Button(left_frame,
          text="Get some advice from AI :",
          font=("Arial", 28),
          fg="white",
          bg="#FF8C00",
          anchor="w",
          command=get_ai_advice
         ).grid(row=2, column=0, columnspan=2,
                sticky="we", pady=20, ipady=10)

# 滑块 + Spinbox 组
cal_var = tk.DoubleVar()
fat_var = tk.DoubleVar()
sug_var = tk.DoubleVar()

# MAX CAL
tk.Label(left_frame,
         text="MAX CAL",
         font=("Arial", 24),
         fg="white",
         bg="red"
        ).grid(row=3, column=0, sticky="w", pady=5)
tk.Spinbox(left_frame,
           from_=0, to=1000,
           font=("Arial", 16),
           textvariable=cal_var,
           width=8
          ).grid(row=3, column=1, sticky="w")
tk.Scale(left_frame,
         variable=cal_var,
         from_=0, to=1000,
         orient="horizontal",
         length=400,
         command=lambda e: None
        ).grid(row=3, column=2, sticky="w")

# MAX FAT
tk.Label(left_frame,
         text="MAX FAT",
         font=("Arial", 24),
         fg="white",
         bg="red"
        ).grid(row=4, column=0, sticky="w", pady=5)
tk.Spinbox(left_frame,
           from_=0, to=200,
           font=("Arial", 16),
           textvariable=fat_var,
           width=8
          ).grid(row=4, column=1, sticky="w")
tk.Scale(left_frame,
         variable=fat_var,
         from_=0, to=200,
         orient="horizontal",
         length=400,
         command=lambda e: None
        ).grid(row=4, column=2, sticky="w")

# MAX SGR
tk.Label(left_frame,
         text="MAX SGR",
         font=("Arial", 24),
         fg="white",
         bg="red"
        ).grid(row=5, column=0, sticky="w", pady=5)
tk.Spinbox(left_frame,
           from_=0, to=200,
           font=("Arial", 16),
           textvariable=sug_var,
           width=8
          ).grid(row=5, column=1, sticky="w")
tk.Scale(left_frame,
         variable=sug_var,
         from_=0, to=200,
         orient="horizontal",
         length=400,
         command=lambda e: None
        ).grid(row=5, column=2, sticky="w")

# 分类单选（左侧四个）
category_var = tk.StringVar()
tk.Radiobutton(left_frame,
               text="Snack & Sides",
               variable=category_var,
               value="Snack & Sides",
               font=("Arial", 20),
               fg="white",
               bg="red",
               selectcolor="black",
               activebackground="red",
               command=update_filters
              ).grid(row=6, column=0, sticky="w", pady=5)
tk.Radiobutton(left_frame,
               text="Burger & Sandwiches",
               variable=category_var,
               value="Burger & Sandwiches",
               font=("Arial", 20),
               fg="white",
               bg="red",
               selectcolor="black",
               activebackground="red",
               command=update_filters
              ).grid(row=7, column=0, sticky="w", pady=5)
tk.Radiobutton(left_frame,
               text="Chicken & Fish",
               variable=category_var,
               value="Chicken & Fish",
               font=("Arial", 20),
               fg="white",
               bg="red",
               selectcolor="black",
               activebackground="red",
               command=update_filters
              ).grid(row=8, column=0, sticky="w", pady=5)
tk.Radiobutton(left_frame,
               text="Desserts & Shakes",
               variable=category_var,
               value="Desserts & Shakes",
               font=("Arial", 20),
               fg="white",
               bg="red",
               selectcolor="black",
               activebackground="red",
               command=update_filters
              ).grid(row=9, column=0, sticky="w", pady=5)

# 分类单选（右侧四个）
tk.Radiobutton(left_frame,
               text="McCafe",
               variable=category_var,
               value="McCafe",
               font=("Arial", 20),
               fg="white",
               bg="red",
               selectcolor="black",
               activebackground="red",
               command=update_filters
              ).grid(row=6, column=1, sticky="w", pady=5)
tk.Radiobutton(left_frame,
               text="Beverages",
               variable=category_var,
               value="Beverages",
               font=("Arial", 20),
               fg="white",
               bg="red",
               selectcolor="black",
               activebackground="red",
               command=update_filters
              ).grid(row=7, column=1, sticky="w", pady=5)
tk.Radiobutton(left_frame,
               text="Condiments",
               variable=category_var,
               value="Condiments",
               font=("Arial", 20),
               fg="white",
               bg="red",
               selectcolor="black",
               activebackground="red",
               command=update_filters
              ).grid(row=8, column=1, sticky="w", pady=5)
tk.Radiobutton(left_frame,
               text="Breakfast",
               variable=category_var,
               value="Breakfast",
               font=("Arial", 20),
               fg="white",
               bg="red",
               selectcolor="black",
               activebackground="red",
               command=update_filters
              ).grid(row=9, column=1, sticky="w", pady=5)

# ——— 右侧 Listbox ———
right_frame.grid_rowconfigure(0, weight=0)
right_frame.grid_columnconfigure(0, weight=1)
name_var = tk.StringVar(value=all_name_list)
name_listbox = tk.Listbox(right_frame,
                           listvariable=name_var,
                           selectmode=tk.SINGLE,
                           font=("Arial", 14),
                           bg="#f2f2f2",    # 浅灰，模拟半透明
                          fg="black",
                          height=30)
name_listbox.grid(row=0, column=0, sticky="nsew")

# ——— 启动主循环 ———
root.mainloop()
