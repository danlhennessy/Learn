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

text_scroll.config(command=my_text.yview)

root.mainloop()