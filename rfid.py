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
            
# Button for choosing file
button1 = Button(root, text="open file", command=file_open).pack()

# Labels for error codes
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()