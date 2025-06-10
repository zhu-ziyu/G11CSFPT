'''
June 2025
ICS3U Final Performance Task
CODED BY ***your name here***

'''

from tkinter import *
from tkinter.font import Font


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
            



#MAIN
global matched_indexes, all_name_list, all_calorie_list, all_fat_list, all_sugar_list, all_category_list, all_allergens_list

matched_indexes = []
all_name_list,\
    all_calorie_list,\
    all_fat_list,\
    all_sugar_list,\
    all_category_list,\
    all_allergens_list = generate_list_mcd("mcd_clean.csv")


#CREATE WIDGETS
root = Tk()
mainframe = Frame(root)

#you can change the information default displayed in listbox
name_var = StringVar()
name_var.set(all_name_list)
name_listbox = Listbox(mainframe, listvariable=name_var, selectmode=SINGLE)



#GRID WIDGETS
mainframe.grid(padx=50, pady=50)
name_listbox.grid(row=2, column=1, columnspan=2)




