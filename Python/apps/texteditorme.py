from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("PY Text Editor")
root.geometry("900x900")

#Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#Scroll Bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Text Box
my_text = Text(my_frame, width=100, height=20, fg="blue", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#Scroll Bar Config
text_scroll.config(command=my_text.yview)

#Menu Bar
my_menu = Menu(root)
root.config(menu=my_menu)

#Menu - File
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_command(label="Quit")

#Menu - Edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)

root.mainloop()