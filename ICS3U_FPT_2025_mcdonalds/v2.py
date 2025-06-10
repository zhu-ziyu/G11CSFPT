from tkinter import *
from tkinter.font import Font

# YOU ARE NOT RESPONSIBLE TO UNDERSTAND THIS FUNCTION
# (existing data loading function)
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
        line = line.strip().split(",")
        name_list.append(line[0])
        calorie_list.append(int(line[1]))
        fat_list.append(float(line[2]))
        sugar_list.append(int(line[3]))
        category_list.append(line[4])
        allergens_list.append(line[5])
    return name_list, calorie_list, fat_list, sugar_list, category_list, allergens_list

# MAIN DATA
all_name_list, all_calorie_list, all_fat_list, all_sugar_list, all_category_list, all_allergens_list = generate_list_mcd("/mcd_clean.csv")

# COMMAND STUBS (NO LOGIC)
def search():
    pass

def get_advice():
    pass

def filter_by_calorie(val):
    pass

def filter_by_fat(val):
    pass

def filter_by_sugar(val):
    pass

def update_list(*args):
    pass

# SETUP WINDOW
root = Tk()
root.title("ICS3U1-FPT")
root.geometry("1920x1080")

# MAIN FRAME
mainframe = Frame(root, bg='red')
mainframe.grid(padx=50, pady=50)

# SEARCH SECTION
search_label = Label(mainframe, text="SEARCH :", bg='orange', fg='white')
search_entry = Entry(mainframe)
go_button = Button(mainframe, text="GO", command=search, bg='orange', fg='white')

# AI ADVICE BUTTON
advice_button = Button(mainframe, text="Get some advice from AI :", command=get_advice, bg='orange', fg='white')

# FILTER SCALES
cal_label = Label(mainframe, text="MAX CAL", fg='white', bg='red')
cal_scale = Scale(mainframe, from_=0, to=1000, orient=HORIZONTAL, command=filter_by_calorie)
fat_label = Label(mainframe, text="MAX FAT", fg='white', bg='red')
fat_scale = Scale(mainframe, from_=0, to=100, orient=HORIZONTAL, command=filter_by_fat)
sugar_label = Label(mainframe, text="MAX SGR", fg='white', bg='red')
sugar_scale = Scale(mainframe, from_=0, to=100, orient=HORIZONTAL, command=filter_by_sugar)

# CATEGORY RADIOBUTTONS
category_var = StringVar(value="")
# Left column
rb_snack = Radiobutton(mainframe, text="Snack & Sides", variable=category_var, value="Snack & Sides", command=update_list, bg='red', fg='white', indicatoron=0)
rb_burger = Radiobutton(mainframe, text="Burger & Sandwiches", variable=category_var, value="Burger & Sandwiches", command=update_list, bg='red', fg='white', indicatoron=0)
rb_chicken = Radiobutton(mainframe, text="Chicken & Fish", variable=category_var, value="Chicken & Fish", command=update_list, bg='red', fg='white', indicatoron=0)
rb_dessert = Radiobutton(mainframe, text="Desserts & Shakes", variable=category_var, value="Desserts & Shakes", command=update_list, bg='red', fg='white', indicatoron=0)
# Right column
rb_mccafe = Radiobutton(mainframe, text="McCafe", variable=category_var, value="McCafe", command=update_list, bg='red', fg='white', indicatoron=0)
rb_bev = Radiobutton(mainframe, text="Beverages", variable=category_var, value="Beverages", command=update_list, bg='red', fg='white', indicatoron=0)
rb_cond = Radiobutton(mainframe, text="Condiments", variable=category_var, value="Condiments", command=update_list, bg='red', fg='white', indicatoron=0)
rb_break = Radiobutton(mainframe, text="Breakfast", variable=category_var, value="Breakfast", command=update_list, bg='red', fg='white', indicatoron=0)

# LISTBOX
name_var = StringVar(value=all_name_list)
name_listbox = Listbox(mainframe, listvariable=name_var, selectmode=SINGLE)

# LAYOUT WITH GRID
search_label.grid(row=0, column=0, sticky='w')
search_entry.grid(row=0, column=1, columnspan=2, sticky='we')
go_button.grid(row=0, column=3, padx=(10,0))

advice_button.grid(row=1, column=0, columnspan=4, pady=(20,10), sticky='we')

cal_label.grid(row=2, column=0, sticky='w')
cal_scale.grid(row=2, column=1, columnspan=3, sticky='we')
fat_label.grid(row=3, column=0, sticky='w')
fat_scale.grid(row=3, column=1, columnspan=3, sticky='we')
sugar_label.grid(row=4, column=0, sticky='w')
sugar_scale.grid(row=4, column=1, columnspan=3, sticky='we')

# Radiobuttons positions
rb_snack.grid(row=5, column=0, sticky='w', pady=2)
rb_burger.grid(row=6, column=0, sticky='w', pady=2)
rb_chicken.grid(row=7, column=0, sticky='w', pady=2)
rb_dessert.grid(row=8, column=0, sticky='w', pady=2)

rb_mccafe.grid(row=5, column=3, sticky='w', pady=2)
rb_bev.grid(row=6, column=3, sticky='w', pady=2)
rb_cond.grid(row=7, column=3, sticky='w', pady=2)
rb_break.grid(row=8, column=3, sticky='w', pady=2)

# Listbox on the right side
name_listbox.grid(row=2, column=5, rowspan=7, sticky='nswe', padx=(50,0))

# EXPAND COLUMNS
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(5, weight=2)

# START MAIN LOOP
root.mainloop()
