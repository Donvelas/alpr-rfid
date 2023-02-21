#dependancies 
# pandas, numpy, xlrd

from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog


root = Tk()
root.title('metrics')
root.geometry('600x600')
root.resizable(True, True)

# create frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# create tree view
my_tree = ttk.Treeview()

# file open function
def file_open():
    pass

# add a menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add menu botton
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Speadsheets", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)

root.mainloop()