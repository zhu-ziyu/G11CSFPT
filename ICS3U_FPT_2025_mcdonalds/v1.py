from tkinter import *
from tkinter.font import Font

# YOU ARE NOT RESPONSIBLE TO UNDERSTAND THIS FUNCTION
def generate_list_mcd(filename):
    name_list = []
    calorie_list = []
    fat_list = []
    sugar_list = []
    category_list = []
    allergens_list = []

    file_in = open(filename, encoding="utf-8", errors='replace')
    file_in.readline()

    for line in file_in:
        parts = line.strip().split(",")
        name_list.append(parts[0])
        calorie_list.append(int(parts[1]))
        fat_list.append(float(parts[2]))
        sugar_list.append(int(parts[3]))
        category_list.append(parts[4])
        allergens_list.append(parts[5])

    return name_list, \
        calorie_list, \
        fat_list, \
        sugar_list, \
        category_list, \
        allergens_list

# MAIN
matched_indexes = []
all_name_list, \
    all_calorie_list, \
    all_fat_list, \
    all_sugar_list, \
    all_category_list, \
    all_allergens_list = generate_list_mcd("mcd_clean.csv")

# CREATE APP WINDOW
root = Tk()
root.title("ICS3U1-FPT")
root.configure(bg="red")
# 让窗口和内部布局可伸缩
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# MAIN FRAME FOR LAYOUT
mainframe = Frame(root, bg="red")
mainframe.grid(sticky="nsew", padx=20, pady=20)
for c in range(5):
    mainframe.columnconfigure(c, weight=1)
for r in range(10):
    mainframe.rowconfigure(r, weight=0)
# 让列表区域可扩展
mainframe.rowconfigure(2, weight=1)

# FONTS
title_font  = Font(family="Arial", size=48, weight="bold")
label_font  = Font(family="Arial", size=24)
button_font = Font(family="Arial", size=24)
listbox_font= Font(family="Arial", size=18)

# --- TITLE ---
title_label = Label(mainframe, text="ICS3U1-FPT",
                    font=title_font, fg="white", bg="red")
title_label.grid(row=0, column=3, columnspan=2,
                 sticky="e", padx=5, pady=5)

# --- SEARCH SECTION ---
search_label = Label(mainframe, text="SEARCH :",
                     font=label_font, fg="white", bg="#FFA500")
search_label.grid(row=1, column=0, sticky="w",
                  padx=5, pady=5)
search_entry = Entry(mainframe, font=label_font, width=20)
search_entry.grid(row=1, column=1, sticky="w",
                  padx=5, pady=5)
search_button = Button(mainframe, text="GO",
                       font=button_font,
                       bg="#FFA500", fg="white",
                       command=lambda: on_search())
search_button.grid(row=1, column=2, sticky="w",
                   padx=5, pady=5)

# --- AI ADVICE BUTTON ---
advice_button = Button(mainframe,
                       text="Get some advice from AI :",
                       font=button_font,
                       bg="#FFA500", fg="white",
                       command=lambda: on_ai_advice())
advice_button.grid(row=2, column=0, columnspan=3,
                   sticky="w", padx=5, pady=(0,10))

# --- RESULT LISTBOX ---
name_var = StringVar(value=all_name_list)
name_listbox = Listbox(mainframe,
                       listvariable=name_var,
                       selectmode=SINGLE,
                       font=listbox_font,
                       width=40, height=15)
name_listbox.grid(row=2, column=3, rowspan=8, columnspan=2,
                  sticky="nsew", padx=5, pady=5)

# --- VARIABLES FOR FILTERS ---
cal_var = IntVar(value=2000)
fat_var = DoubleVar(value=200.0)
sgr_var = IntVar(value=200)

# --- NUTRITION FILTERS FRAME ---
nutrient_frame = LabelFrame(
    mainframe, text="Nutrition Filters",
    font=label_font, fg="white", bg="red",
    labelanchor="n"
)
nutrient_frame.grid(row=3, column=0, columnspan=3,
                    rowspan=3, sticky="nsew",
                    padx=5, pady=5)
for c in range(3):
    nutrient_frame.columnconfigure(c, weight=1)

# CALORIES
cal_label = Label(nutrient_frame, text="MAX CAL",
                  font=label_font, fg="white", bg="red")
cal_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
cal_spin = Spinbox(nutrient_frame, from_=0, to=2000,
                   textvariable=cal_var,
                   font=label_font, width=6,
                   command=lambda: on_cal_spin())
cal_spin.grid(row=0, column=1, sticky="w", padx=5, pady=5)
cal_spin.bind('<KeyRelease>', lambda e: on_cal_spin())
cal_scale = Scale(nutrient_frame, from_=0, to=2000,
                  orient=HORIZONTAL, length=400,
                  variable=cal_var,
                  command=lambda v: on_cal_scale(v))
cal_scale.grid(row=0, column=2, sticky="we", padx=5, pady=5)

# FAT
fat_label = Label(nutrient_frame, text="MAX FAT",
                  font=label_font, fg="white", bg="red")
fat_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
fat_spin = Spinbox(nutrient_frame, from_=0, to=200,
                   increment=0.1,
                   textvariable=fat_var,
                   font=label_font, width=6,
                   command=lambda: on_fat_spin())
fat_spin.grid(row=1, column=1, sticky="w", padx=5, pady=5)
fat_spin.bind('<KeyRelease>', lambda e: on_fat_spin())
fat_scale = Scale(nutrient_frame, from_=0, to=200,
                  orient=HORIZONTAL, length=400,
                  variable=fat_var,
                  command=lambda v: on_fat_scale(v))
fat_scale.grid(row=1, column=2, sticky="we", padx=5, pady=5)

# SUGAR
sgr_label = Label(nutrient_frame, text="MAX SGR",
                  font=label_font, fg="white", bg="red")
sgr_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
sgr_spin = Spinbox(nutrient_frame, from_=0, to=200,
                   textvariable=sgr_var,
                   font=label_font, width=6,
                   command=lambda: on_sgr_spin())
sgr_spin.grid(row=2, column=1, sticky="w", padx=5, pady=5)
sgr_spin.bind('<KeyRelease>', lambda e: on_sgr_spin())
sgr_scale = Scale(nutrient_frame, from_=0, to=200,
                  orient=HORIZONTAL, length=400,
                  variable=sgr_var,
                  command=lambda v: on_sgr_scale(v))
sgr_scale.grid(row=2, column=2, sticky="we", padx=5, pady=5)

# --- CATEGORY RADIOS FRAME ---
category_frame = LabelFrame(
    mainframe, text="Categories",
    font=label_font, fg="white", bg="red",
    labelanchor="n"
)
category_frame.grid(row=6, column=0, columnspan=3,
                    rowspan=4, sticky="nsew",
                    padx=5, pady=5)
# Left categories
left_cat_var = StringVar()
categories_left = ["Snack & Sides", "Burger & Sandwiches",
                   "Chicken & Fish", "Desserts & Shakes"]
for i, cat in enumerate(categories_left):
    rb = Radiobutton(
        category_frame, text=cat,
        variable=left_cat_var, value=cat,
        font=("Arial",20), fg="white", bg="red",
        indicatoron=0,
        command=lambda: update_list()
    )
    rb.grid(row=i, column=0, sticky="w", padx=5, pady=3)
# Right categories
right_cat_var = StringVar()
categories_right = ["McCafe", "Beverages", "Condiments", "Breakfast"]
for i, cat in enumerate(categories_right):
    rb = Radiobutton(
        category_frame, text=cat,
        variable=right_cat_var, value=cat,
        font=("Arial",20), fg="white", bg="red",
        indicatoron=0,
        command=lambda: update_list()
    )
    rb.grid(row=i, column=1, sticky="w", padx=5, pady=3)

# --- CALLBACK BINDING FUNCTIONS ---
def on_cal_spin():
    try:
        val = cal_var.get()
    except TclError:
        return
    cal_scale.set(val)
    update_filters()

def on_cal_scale(val):
    cal_var.set(int(float(val)))
    update_filters()

def on_fat_spin():
    try:
        val = fat_var.get()
    except TclError:
        return
    fat_scale.set(val)
    update_filters()

def on_fat_scale(val):
    fat_var.set(float(val))
    update_filters()

def on_sgr_spin():
    try:
        val = sgr_var.get()
    except TclError:
        return
    sgr_scale.set(val)
    update_filters()

def on_sgr_scale(val):
    sgr_var.set(int(float(val)))
    update_filters()

def update_filters():
    # 这里可以添加根据 cal_var、fat_var、sgr_var、
    # left_cat_var、right_cat_var 来过滤 matched_indexes
    update_list()

def on_search():
    # 搜索逻辑占位
    pass

def on_ai_advice():
    # AI 建议逻辑占位
    pass

def update_list():
    # 根据 matched_indexes 更新列表内容
    pass

# LAUNCH
root.mainloop()
