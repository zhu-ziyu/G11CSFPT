'''
June 2025
ICS3U Final Performance Task
CODED BY ***SAM***

'''



from tkinter import *
from tkinter.font import Font

from PIL import ImageTk



#YOU ARE NOT RESPONSIBLE TO UNDERSTAND THIS FUNCTION
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
                
    return name_list,\
           calorie_list,\
           fat_list,\
           sugar_list,\
           category_list,\
           allergens_list


def all_name_list_test():
    pass;


def all_calorie_list_test():
    pass

def search():
    pass

def seachbyai():
    pass

def seachbyb():
    pass

def on_advice():
    pass

#MAIN
global matched_indexes, all_name_list, all_calorie_list, all_fat_list, all_sugar_list, all_category_list, all_allergens_list

matched_indexes = []
all_name_list,\
    all_calorie_list,\
    all_fat_list,\
    all_sugar_list,\
    all_category_list,\
    all_allergens_list = generate_list_mcd("mcd_clean.csv")



root = Tk()
mainframe = Frame(root)

name_var = StringVar()
name_var.set(all_name_list)
name_listbox = Listbox(mainframe, listvariable=name_var, selectmode=SINGLE)

Labeltext1 = Label(mainframe, text="MAX CAL")
Labeltext2 = Label(mainframe, text="MAX FAT")
Labeltext3 = Label(mainframe, text="MAX SGR")

Labeltext1.grid(row=0, column=0)
Labeltext2.grid()
Labeltext3.grid()

search_frame = Frame(mainframe, bg='orange', height=50)
search_frame.grid(fill='x', pady=(0, 10))
search_label = Label(search_frame, text="SEARCH :", bg='orange', fg='white', font=('Arial', 16, 'bold'))
search_label.grid(side='left', padx=(10,5))
search_entry = Entry(search_frame, bg='white', fg='black', font=('Arial', 16))
search_entry.grid(expand=True, padx=(0,10))
search_button = Button(search_frame, text="Go", command=search)
search_button.grid(side='right', padx=(0,10))

categories = [
    "Snack & Sides",
    "Burger & Sandwiches",
    "Chicken & Fish",
    "Desserts & Shakes",
    "McCafe",
    "Beverages",
    "Condiments",
    "Breakfast",
    "Condiments"
]
cat_title = Label(mainframe, text="Food Categories", bg='red', fg='black')
#我也不知道....暂定


advice_label = Label(mainframe, text="Get some advice from AI :", bg='orange', fg='white', font=('Arial', 16, 'bold'))
advice_label.grid(side='left', padx=(10,5))
advice_entry = Entry(mainframe, bg='white', fg='black', font=('Arial', 16))
advice_button = Button(mainframe, text="Ask", command=on_advice)
advice_button.grid(side='right', padx=(0,10))

#暂时留空,暂时储存在这
PhotoImage = ImageTk.PhotoImage()
logo_frame = Frame(left_col, bg='red')
logo_frame.grid(side='bottom', pady=10)
logo_label = Label(logo_frame, text="McDonald's Logo", bg='red', fg='yellow', font=('Arial', 24, 'bold'))
logo_label.grid()

Labelbigtext= Label(mainframe, text="ICS3U1-FPT")

#GRID WIDGETS
mainframe.grid(padx=50, pady=50)
name_listbox.grid(row=2, column=1, columnspan=2)


root.mainloop()

