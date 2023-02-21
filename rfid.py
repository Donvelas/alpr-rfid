#dependencies to pip install 
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

# file open function, this will do all the work
def file_open():
    file_name = filedialog.askopenfile(
        initialdir=""
    )

# add a menu to the window
my_menu = Menu(root)
root.config(menu=my_menu)

# add menu button to open spreadsheet
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Speadsheets", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)

root.mainloop()