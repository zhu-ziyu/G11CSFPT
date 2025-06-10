import tkinter as tk

# Callback functions
def on_bullet_click(name):
    print(f"Option clicked: {name}")

def on_search():
    print(f"Search query: {search_entry.get()}")

def on_advice():
    print(f"AI advice input: {advice_entry.get()}")

# Main window
root = tk.Tk()
root.title("Nutrition UI")
root.configure(bg='red')
root.geometry('1200x800')

# Main container: split left and right
main_frame = tk.Frame(root, bg='red')
main_frame.pack(fill='both', expand=True)

# Left column
left_col = tk.Frame(main_frame, bg='red')
left_col.pack(side='left', fill='both', expand=True, padx=20, pady=20)

# Right column
right_col = tk.Frame(main_frame, bg='red')
right_col.pack(side='left', fill='both', expand=True, padx=20, pady=20)

# Left side components: Search, sliders, options, allergens, logo
# Search bar
search_frame = tk.Frame(left_col, bg='orange', height=50)
search_frame.pack(fill='x', pady=(0, 10))
search_label = tk.Label(search_frame, text="SEARCH :", bg='orange', fg='white', font=('Arial', 16, 'bold'))
search_label.pack(side='left', padx=(10,5))
search_entry = tk.Entry(search_frame, bg='white', fg='black', font=('Arial', 16))
search_entry.pack(fill='x', expand=True, padx=(0,10))
search_button = tk.Button(search_frame, text="Go", command=on_search)
search_button.pack(side='right', padx=(0,10))

# Sliders
slider_frame = tk.Frame(left_col, bg='red')
slider_frame.pack(fill='x', pady=(0, 20))
for label_text in ["MAX CAL", "MAX FAT", "MAX SGR"]:
    row = tk.Frame(slider_frame, bg='red')
    row.pack(fill='x', pady=5)

    tk.Label(row, text=label_text, bg='red', fg='white', font=('Arial', 14)).pack(side='left', padx=(0,10))
    var = tk.IntVar(value=50)
    entry = tk.Entry(row, textvariable=var, width=5, bg='lightgrey', font=('Arial', 12))
    entry.pack(side='left', padx=(0,10))
    scale = tk.Scale(row, variable=var, from_=0, to=100, orient='horizontal', length=300,
                     bg='white', troughcolor='lightgrey')
    scale.pack(side='left')

# Option bullets
options_frame = tk.Frame(left_col, bg='red')
options_frame.pack(fill='both', expand=True, pady=(0, 20))

left_opts = ["Snack & Sides", "Burger & Sandwiches", "Chicken & Fish", "Desserts & Shakes"]
right_opts = ["McCafe", "Beverages", "Condiments", "Breakfast"]

left_frame = tk.Frame(options_frame, bg='red')
left_frame.pack(side='left', fill='both', expand=True)
right_frame = tk.Frame(options_frame, bg='red')
right_frame.pack(side='left', fill='both', expand=True)
for opt in left_opts:
    btn = tk.Button(left_frame, text=f"● {opt}", bg='red', fg='white', bd=0,
                    font=('Arial', 14), anchor='w', command=lambda o=opt: on_bullet_click(o))
    btn.pack(fill='x', pady=2)
for opt in right_opts:
    btn = tk.Button(right_frame, text=f"● {opt}", bg='red', fg='white', bd=0,
                    font=('Arial', 14), anchor='w', command=lambda o=opt: on_bullet_click(o))
    btn.pack(fill='x', pady=2)

# Allergens list
allergens_frame = tk.Frame(left_col, bg='red')
allergens_frame.pack(fill='x', pady=(0,20))
for item in ["Cereal Containing gluten", "Milk", "Soya", "Egg", "/", "/"]:
    lbl = tk.Label(allergens_frame, text=item, bg='lightgrey', fg='black', font=('Arial', 12), anchor='w')
    lbl.pack(fill='x', pady=1)

# Logo placeholder
logo_frame = tk.Frame(left_col, bg='red')
logo_frame.pack(side='bottom', pady=10)
logo_label = tk.Label(logo_frame, text="McDonald's Logo", bg='red', fg='yellow', font=('Arial', 24, 'bold'))
logo_label.pack()

# Right side components: AI advice and guidelines placeholder
# Advice bar
advice_frame = tk.Frame(right_col, bg='orange', height=50)
advice_frame.pack(fill='x', pady=(0, 20))
advice_label = tk.Label(advice_frame, text="Get some advice from AI :", bg='orange', fg='white', font=('Arial', 16, 'bold'))
advice_label.pack(side='left', padx=(10,5))
advice_entry = tk.Entry(advice_frame, bg='white', fg='black', font=('Arial', 16))
advice_entry.pack(fill='x', expand=True, padx=(0,10))
advice_button = tk.Button(advice_frame, text="Ask", command=on_advice)
advice_button.pack(side='right', padx=(0,10))

# Placeholder: additional right-side items (e.g., guidelines, table)
guidelines_label = tk.Label(right_col, text="● Agree to the User Guidelines", bg='red', fg='white', font=('Arial', 14), anchor='w')
guidelines_label.pack(fill='x', pady=2)

root.mainloop()
