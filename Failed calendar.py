import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import re
# from ttkthemes import ThemedTk
import events
import os

if os.name == 'nt':  # 'nt' indicates Windows
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

# root = ThemedTk(theme='adapta')
root = Tk()
root.title("My Birthday Tracker")
root.geometry('600x400')  # Set the window size
#screen sizes
root.resizable(False, False)  # Disable resizing
style = ttk.Style(root)
style.theme_use("clam")  # Use the "clam" theme for a more modern look
# style.theme_use("adapta")  # Use the "clam" theme for a more modern look

tab_control = ttk.Notebook(root)
display_tab = ttk.Frame(tab_control)
add_tab = ttk.Frame(tab_control)

tab_control.add(display_tab, text="Display", padding=10)
tab_control.add(add_tab, text="Add birthday", padding=10)

tab_control.pack(expand=1, fill="both", padx=10, pady=10)

display_label = ttk.Label(display_tab, text="This is the display tab")
display_label.grid(column=0, row=0, pady=10, sticky="w")

ttk.Label(add_tab, text="This is the add tab").\
    grid(column=0, row=0, padx=30, pady=30)

listbox = tk.Listbox(display_tab, bd=0, highlightthickness=0)
listbox.grid(column=0, pady=10, row=1)
#listbox.insert(tk.END, "Hello World")
#pacekot

for row in events.load_birthdays():
    listbox.insert(tk.END, ''.join(row))

ttk.Label(add_tab, text="Person's Name:").\
grid(column=0, row=1, pady=5, sticky="w")
name_entry = ttk.Entry(add_tab)
name_entry.grid(column=1, row=1, pady=5, sticky="w")

ttk.Label(add_tab, text="Birthday (YYYY/MM/DD):").\
grid(column=0, row=2, pady=5, sticky="w")
birthday_entry = ttk.Entry(add_tab)
birthday_entry.grid(column=1, row=2, pady=5, sticky="w")


# Function to add a birthday to the list
def add_birthday():
    name = name_entry.get()
    birthday = birthday_entry.get()
    # YYYY/MM/DD uz YYYY-MM-DD
    birthday = birthday.replace('/','-')
    birthday = birthday.strip()
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', birthday):
        messagebox.showerror("ERROR", "Invalid Date!")
        return
    year = birthday[:4]
    events.save_birthday(name, birthday)
    messagebox.showinfo("Success", "Birthday added successfully!")
    

add_button = ttk.Button(add_tab, text="Add Birthday", command=add_birthday)
add_button.grid(column=1, row=4, pady=20, sticky="e")


root.mainloop()

#regex python apstit