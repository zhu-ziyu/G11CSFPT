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
    pass

def get_ai_advice():
    pass

def update_filters():
    selected = []
    if snack_var.get():       selected.append("Snacks & Sides")
    if burger_var.get():      selected.append("Burgers & Sandwiches")
    if chicken_var.get():     selected.append("Chicken & Fish")
    if desserts_var.get():    selected.append("Desserts & Shakes")
    if mccafe_var.get():      selected.append("McCafe")
    if beverages_var.get():   selected.append("Beverages")
    if condiments_var.get():  selected.append("Condiments")
    if breakfast_var.get():   selected.append("Breakfast")

    name_listbox.delete(0, END)

    for name, cat in zip(all_name_list, all_category_list):
        if not selected or cat in selected:
            name_listbox.insert(END, name)


all_name_list, _, _, _, all_category_list, _ = generate_list_mcd("mcd_clean.csv")

root = Tk()
root.title("ICS3U Final Performance Task")
root.geometry("1920x720")
root.configure(bg="red")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2, minsize=900)
root.grid_columnconfigure(1, weight=3, minsize=1000)

left_frame = Frame(root, bg="red")
left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

right_frame = Frame(root, bg="red")
right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)


left_frame.grid_columnconfigure(0, weight=1, minsize=300)
left_frame.grid_columnconfigure(1, weight=1, minsize=300)
left_frame.grid_columnconfigure(2, weight=2, minsize=400)

# 标题
title_font = Font(family="Arial", size=64, weight="bold")
Label(left_frame,
      text="ICS3U1-FPT",
      font=title_font,
      fg="white",
      bg="red").grid(row=0, column=0, columnspan=2, sticky="w")

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

# AI 建议按钮
Button(left_frame,
       text="Get some advice from AI :",
       font=("Arial", 28),
       fg="white",
       bg="#FF8C00",
       anchor="w",
       command=get_ai_advice).grid(row=2, column=0, columnspan=2, sticky="we", pady=20, ipady=10)

#滑块
cal_var = DoubleVar()
fat_var = DoubleVar()
sug_var = DoubleVar()

Label(left_frame, text="MAX CAL", font=("Arial", 24), fg="white", bg="red").grid(row=3, column=0, sticky="w", pady=5)
Spinbox(left_frame, from_=0, to=1000, font=("Arial", 16), textvariable=cal_var, width=8).grid(row=3, column=1, sticky="w")
Scale(left_frame, variable=cal_var, from_=0, to=1000, orient=HORIZONTAL, length=400, command=lambda e: None).grid(row=3, column=2, sticky="w")

Label(left_frame, text="MAX FAT", font=("Arial", 24), fg="white", bg="red").grid(row=4, column=0, sticky="w", pady=5)
Spinbox(left_frame, from_=0, to=200, font=("Arial", 16), textvariable=fat_var, width=8).grid(row=4, column=1, sticky="w")
Scale(left_frame, variable=fat_var, from_=0, to=200, orient=HORIZONTAL, length=400, command=lambda e: None).grid(row=4, column=2, sticky="w")

Label(left_frame, text="MAX SGR", font=("Arial", 24), fg="white", bg="red").grid(row=5, column=0, sticky="w", pady=5)
Spinbox(left_frame, from_=0, to=200, font=("Arial", 16), textvariable=sug_var, width=8).grid(row=5, column=1, sticky="w")
Scale(left_frame, variable=sug_var, from_=0, to=200, orient=HORIZONTAL, length=400, command=lambda e: None).grid(row=5, column=2, sticky="w")


snack_var    = BooleanVar()
burger_var   = BooleanVar()
chicken_var  = BooleanVar()
desserts_var = BooleanVar()
mccafe_var   = BooleanVar()
beverages_var= BooleanVar()
condiments_var=BooleanVar()
breakfast_var= BooleanVar()

Checkbutton(left_frame, text="Snack & Sides",    variable=snack_var,    onvalue=True, offvalue=False,
            font=("Arial",20), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=6, column=0, sticky="w", pady=5)
Checkbutton(left_frame, text="Burger & Sandwiches", variable=burger_var, onvalue=True, offvalue=False,
            font=("Arial",20), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=7, column=0, sticky="w", pady=5)
Checkbutton(left_frame, text="Chicken & Fish",     variable=chicken_var, onvalue=True, offvalue=False,
            font=("Arial",20), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=8, column=0, sticky="w", pady=5)
Checkbutton(left_frame, text="Desserts & Shakes",  variable=desserts_var,onvalue=True, offvalue=False,
            font=("Arial",20), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=9, column=0, sticky="w", pady=5)

Checkbutton(left_frame, text="McCafe",       variable=mccafe_var,   onvalue=True, offvalue=False,
            font=("Arial",20), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=6, column=1, sticky="w", pady=5)
Checkbutton(left_frame, text="Beverages",    variable=beverages_var,onvalue=True, offvalue=False,
            font=("Arial",20), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=7, column=1, sticky="w", pady=5)
Checkbutton(left_frame, text="Condiments",   variable=condiments_var,onvalue=True, offvalue=False,
            font=("Arial",20), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=8, column=1, sticky="w", pady=5)
Checkbutton(left_frame, text="Breakfast",    variable=breakfast_var,onvalue=True, offvalue=False,
            font=("Arial",20), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=9, column=1, sticky="w", pady=5)



#右侧过敏源筛选
#Cereal Containing gluten;
#Egg;
#Milk;
#Soya;
#Sesame

Sesame_var = BooleanVar()
Soya_var   = BooleanVar()
milk_var= BooleanVar()
egg_var=BooleanVar()
ccg_var= BooleanVar()

Checkbutton(right_frame, text="Cereal Containing gluten",    variable=ccg_var,onvalue=True, offvalue=False,
            font=("Arial",10), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=0, column=0, sticky="w", pady=5)
Checkbutton(right_frame, text="Egg",    variable=egg_var,onvalue=True, offvalue=False,
            font=("Arial",10), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=0, column=1, sticky="w", pady=5)
Checkbutton(right_frame, text="Milk",    variable=milk_var,onvalue=True, offvalue=False,
            font=("Arial",10), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=0, column=2, sticky="w", pady=5)
Checkbutton(right_frame, text="Soya",    variable=Soya_var,onvalue=True, offvalue=False,
            font=("Arial",10), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=1, column=3, sticky="w", pady=5)
Checkbutton(right_frame, text="Sesame",    variable=Sesame_var,onvalue=True, offvalue=False,
            font=("Arial",10), fg="white", bg="red", selectcolor="black",
            activebackground="red", command=update_filters).grid(row=1, column=4, sticky="w", pady=5)

#Listbox
right_frame.grid_rowconfigure(0, weight=0)
right_frame.grid_columnconfigure(0, weight=1)

name_var = StringVar(value=all_name_list)
name_listbox = Listbox(right_frame,
                       listvariable=name_var,
                       selectmode=SINGLE,
                       font=("Arial",14),
                       bg="white",
                       fg="black",
                       height=40)
name_listbox.grid(row=2, columnspan=4,column=0, sticky="nsew")

root.mainloop()
