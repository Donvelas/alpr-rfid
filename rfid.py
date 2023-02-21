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
    filename = filedialog.askopenfile(
        initialdir='',
        title="Open a file",
        filetypes=(("xlsx files", ".xlsx"), ("All files", "*.*"))
    )
    
    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)
        except ValueError:
            my_label.config(text="File couldn't be opened, try again")
        except FileNotFoundError:
            my_label.config(text="File not found")
    
    # clear old tree view        
    clear_tree()
    
# clear tree function 
def clear_tree():
    my_tree.delete(*my_tree.get_children())
            
        
        

# add a menu to the window
my_menu = Menu(root)
root.config(menu=my_menu)

# add menu button to open spreadsheet
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Speadsheets", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)

# Labels for error codes
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()