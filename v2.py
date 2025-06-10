import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("McDonald's Menu Filter")
root.configure(bg='red')

# Left Frame
left_frame = tk.Frame(root, bg='red')
left_frame.pack(side='left', fill='both', expand=True)

# Search Label (Orange Bar)
search_label = tk.Label(left_frame, text="SEARCH :", bg='orange', fg='white')
search_label.pack(fill='x')

# Sliders
max_cal_var = tk.IntVar()
cal_label = tk.Label(left_frame, text="MAX CAL", bg='red', fg='black')
cal_label.pack(anchor='w')
cal_scale = tk.Scale(left_frame, from_=0, to=1000, orient='horizontal', variable=max_cal_var)
cal_scale.pack(fill='x')

max_fat_var = tk.IntVar()
fat_label = tk.Label(left_frame, text="MAX FAT", bg='red', fg='black')
fat_label.pack(anchor='w')
fat_scale = tk.Scale(left_frame, from_=0, to=100, orient='horizontal', variable=max_fat_var)
fat_scale.pack(fill='x')

max_sgr_var = tk.IntVar()
sgr_label = tk.Label(left_frame, text="MAX SGR", bg='red', fg='black')
sgr_label.pack(anchor='w')
sgr_scale = tk.Scale(left_frame, from_=0, to=100, orient='horizontal', variable=max_sgr_var)
sgr_scale.pack(fill='x')

# Food Categories
categories = [
    "Snack & Sides",
    "Burger & Sandwiches",
    "Chicken & Fish",
    "Desserts & Shakes",
    "McCafe",
    "Beverages",
    "Condiments",
    "Breakfast"
]
cat_vars = [tk.IntVar() for _ in range(8)]
cat_vars[1].set(1)  # Burger & Sandwiches
cat_vars[4].set(1)  # McCafe

cat_title = tk.Label(left_frame, text="Food Categories", bg='red', fg='black')
cat_title.pack(anchor='w')

cat_buttons = []
for i, cat in enumerate(categories):
    def toggle(i=i):
        if cat_vars[i].get() == 0:
            cat_vars[i].set(1)
            cat_buttons[i].config(text="● " + categories[i])
        else:
            cat_vars[i].set(0)
            cat_buttons[i].config(text="○ " + categories[i])
    text = "● " + cat if cat_vars[i].get() == 1 else "○ " + cat
    btn = tk.Button(left_frame, text=text, command=toggle, bg='red', fg='black', activebackground='red', activeforeground='black', borderwidth=0, anchor='w')
    btn.pack(fill='x', anchor='w')
    cat_buttons.append(btn)

# Allergens
allergens = [
    "Cereal Containing gluten",
    "Milk",
    "Soya",
    "Egg"
]
all_vars = [tk.IntVar() for _ in range(4)]

allergen_title = tk.Label(left_frame, text="Allergens", bg='red', fg='black')
allergen_title.pack(anchor='w')

all_buttons = []
for i, allg in enumerate(allergens):
    def toggle(i=i):
        if all_vars[i].get() == 0:
            all_vars[i].set(1)
            all_buttons[i].config(text="● " + allergens[i])
        else:
            all_vars[i].set(0)
            all_buttons[i].config(text="○ " + allergens[i])
    text = "○ " + allg  # All unselected
    btn = tk.Button(left_frame, text=text, command=toggle, bg='red', fg='black', activebackground='red', activeforeground='black', borderwidth=0, anchor='w')
    btn.pack(fill='x', anchor='w')
    all_buttons.append(btn)

# Horizontal Line
line = tk.Label(left_frame, text="", bg='gray', height=2)
line.pack(fill='x')

# McDonald's Logo (Placeholder)
logo_label = tk.Label(left_frame, text="McDonald's", bg='red', fg='yellow')
logo_label.pack(anchor='s')

# Right Frame
right_frame = tk.Frame(root, bg='red')
right_frame.pack(side='right', fill='both', expand=True)

# AI Advice Label (Orange Bar)
ai_label = tk.Label(right_frame, text="Get some advice from AI :", bg='orange', fg='white')
ai_label.pack(fill='x')

# Agree Button
agree_button = tk.Button(right_frame, text=" Agree to the User Guidelines", bg='black', fg='white')
agree_button.pack()

# Column Selections
columns = ["ITEM", "CAL", "FAT", "SGR"]
col_vars = [tk.IntVar(value=1) for _ in range(4)]  # All selected initially

col_frame = tk.Frame(right_frame, bg='red')
col_frame.pack()

col_buttons = []
tree = ttk.Treeview(right_frame, columns=("ITEM", "CAL", "FAT", "SGR", "CATEGORY", "ALLERGENS"), show='headings')
tree.heading("ITEM", text="ITEM")
tree.heading("CAL", text="CAL")
tree.heading("FAT", text="FAT")
tree.heading("SGR", text="SGR")
tree.heading("CATEGORY", text="CATEGORY")
tree.heading("ALLERGENS", text="ALLERGENS")

for i, col in enumerate(columns):
    def toggle(i=i):
        if col_vars[i].get() == 0:
            col_vars[i].set(1)
            col_buttons[i].config(text="● " + columns[i])
            tree.column(columns[i], width=100)
        else:
            col_vars[i].set(0)
            col_buttons[i].config(text="○ " + columns[i])
            tree.column(columns[i], width=0)
    text = "● " + col  # All selected
    btn = tk.Button(col_frame, text=text, command=toggle, bg='red', fg='black', activebackground='red', activeforeground='black', borderwidth=0)
    btn.pack(side='left')
    col_buttons.append(btn)

# Table
tree.insert("", "end", values=("Iced Tea Extra Small (12 fl oz cup)", 0, 0, 0, "Beverages", "Unknown"))
tree.insert("", "end", values=("White Hot Chocolate (Small) (13.7 oz cup)", 310, 14, 39, "McCafe", "Cereal Containing gluten, Milk, Soya"))
tree.insert("", "end", values=("Premium Grilled Chicken Club Sandwich (9.8 oz)", 610, 20, 14, "Burgers & Sandwiches", "Cereal Containing gluten, Milk, Soya"))
tree.pack(fill='both', expand=True)

# Initially show all columns
for col in columns:
    tree.column(col, width=100)
tree.column("CATEGORY", width=100)
tree.column("ALLERGENS", width=100)

# Start the main loop
root.mainloop()