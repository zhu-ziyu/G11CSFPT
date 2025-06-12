from tkinter import *
from tkinter.font import Font

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


def search():
    get_ai_advice
def get_ai_advice():
    pass

def update_filters():
    rb_snack.get()
    rb_burger.get()
    rb_chicken.get()
    rb_desserts.get()
    rb_mccafe.get()
    rb_beverages.get()
    rb_condiments.get()
    rb_breakfast.get()

#读取————表格（咕咕咕
all_name_list, *_ = generate_list_mcd("mcd_clean.csv")


root = Tk()
root.title("ICS3U Final Performance Task")
root.geometry("1920x720")
root.configure(bg="red")

# 把 root 分成左右两部分
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2, minsize=900)   # 左侧 panel
root.grid_columnconfigure(1, weight=3, minsize=1000)  # 右侧 listbox

left_frame = Frame(root, bg="red")
left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

right_frame = Frame(root, bg="red")
right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

#左侧布局
left_frame.grid_columnconfigure(0, weight=1, minsize=300)
left_frame.grid_columnconfigure(1, weight=1, minsize=300)
left_frame.grid_columnconfigure(2, weight=2, minsize=400)

# 标题 & logo
title_font = Font(family="Arial", size=64, weight="bold")
title_label = Label(left_frame, text="ICS3U1-FPT", font=title_font, fg="white", bg="red")
title_label.grid(row=0, column=0, columnspan=2, sticky="w")

# 搜索框 & GO
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


# AI 建议 按钮
ai_button = Button(left_frame,
                      text="Get some advice from AI :",
                      font=("Arial", 28),
                      fg="white",
                      bg="#FF8C00",
                      anchor="w",
                      command=get_ai_advice)
ai_button.grid(row=2, column=0, columnspan=2, sticky="we", pady=10)

# 滑块 + Spinbox
cal_var = DoubleVar()
fat_var = DoubleVar()
sug_var = DoubleVar()

# MAX CAL
lbl_cal = Label(left_frame, text="MAX CAL", font=("Arial", 24), fg="white", bg="red")
lbl_cal.grid(row=3, column=0, sticky="w", pady=5)
sp_cal = Spinbox(left_frame, from_=0, to=1000, font=("Arial", 16),
                    textvariable=cal_var, width=8)
sp_cal.grid(row=3, column=1, sticky="w")
sc_cal = Scale(left_frame, variable=cal_var, from_=0, to=1000,
                  orient="horizontal", length=400, command=lambda e: None)
sc_cal.grid(row=3, column=2, sticky="w")

# MAX FAT
lbl_fat = Label(left_frame, text="MAX FAT", font=("Arial", 24), fg="white", bg="red")
lbl_fat.grid(row=4, column=0, sticky="w", pady=5)
sp_fat = Spinbox(left_frame, from_=0, to=200, font=("Arial", 16),
                    textvariable=fat_var, width=8)
sp_fat.grid(row=4, column=1, sticky="w")
sc_fat = Scale(left_frame, variable=fat_var, from_=0, to=200,
                  orient="horizontal", length=400, command=lambda e: None)
sc_fat.grid(row=4, column=2, sticky="w")

# MAX SGR
lbl_sug = Label(left_frame, text="MAX SGR", font=("Arial", 24), fg="white", bg="red")
lbl_sug.grid(row=5, column=0, sticky="w", pady=5)
sp_sug = Spinbox(left_frame, from_=0, to=200, font=("Arial", 16),
                    textvariable=sug_var, width=8)
sp_sug.grid(row=5, column=1, sticky="w")
sc_sug = Scale(left_frame, variable=sug_var, from_=0, to=200,
                  orient="horizontal", length=400, command=lambda e: None)
sc_sug.grid(row=5, column=2, sticky="w")

# Radiobuttons
category_var = StringVar()
rb_snack = Radiobutton(left_frame, text="Snack & Sides",    variable=category_var,
                          value="Snack & Sides",    font=("Arial", 20),
                          fg="white", bg="red", selectcolor="black",
                          activebackground="red", command=update_filters)
rb_snack.grid(row=6, column=0, sticky="w", pady=5)

rb_burger = Radiobutton(left_frame, text="Burger & Sandwiches", variable=category_var,
                           value="Burger & Sandwiches", font=("Arial", 20),
                           fg="white", bg="red", selectcolor="black",
                           activebackground="red", command=update_filters)
rb_burger.grid(row=7, column=0, sticky="w", pady=5)

rb_chicken = Radiobutton(left_frame, text="Chicken & Fish", variable=category_var,
                            value="Chicken & Fish", font=("Arial", 20),
                            fg="white", bg="red", selectcolor="black",
                            activebackground="red", command=update_filters)
rb_chicken.grid(row=8, column=0, sticky="w", pady=5)

rb_desserts = Radiobutton(left_frame, text="Desserts & Shakes", variable=category_var,
                             value="Desserts & Shakes", font=("Arial", 20),
                             fg="white", bg="red", selectcolor="black",
                             activebackground="red", command=update_filters)
rb_desserts.grid(row=9, column=0, sticky="w", pady=5)

# Radiobuttons
rb_mccafe = Radiobutton(left_frame, text="McCafe", variable=category_var,
                           value="McCafe", font=("Arial", 20),
                           fg="white", bg="red", selectcolor="black",
                           activebackground="red", command=update_filters)
rb_mccafe.grid(row=6, column=1, sticky="w", pady=5)

rb_beverages = Radiobutton(left_frame, text="Beverages", variable=category_var,
                              value="Beverages", font=("Arial", 20),
                              fg="white", bg="red", selectcolor="black",
                              activebackground="red", command=update_filters)
rb_beverages.grid(row=7, column=1, sticky="w", pady=5)

rb_condiments = Radiobutton(left_frame, text="Condiments", variable=category_var,
                               value="Condiments", font=("Arial", 20),
                               fg="white", bg="red", selectcolor="black",
                               activebackground="red", command=update_filters)
rb_condiments.grid(row=8, column=1, sticky="w", pady=5)

rb_breakfast = Radiobutton(left_frame, text="Breakfast", variable=category_var,
                              value="Breakfast", font=("Arial", 20),
                              fg="white", bg="red", selectcolor="black",
                              activebackground="red", command=update_filters)
rb_breakfast.grid(row=9, column=1, sticky="w", pady=5)


#右侧
right_frame.grid_rowconfigure(0, weight=0)
right_frame.grid_columnconfigure(0, weight=1)
name_var = StringVar(value=all_name_list)
name_listbox = Listbox(right_frame,
                          listvariable=name_var,
                          selectmode=SINGLE,
                          font=("Arial", 14),
                          bg="red",
                          fg="black",
                          height = 40)
name_listbox.grid(row=0, column=0, sticky="nsew")


root.mainloop()

