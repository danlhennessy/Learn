from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("PY Text Editor")
root.geometry("900x600")

#Frame
my_frame = Frame(root)
my_frame.pack(pady=5, padx=5)

#Scroll Bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Text Box
my_text = Text(my_frame, width=120, height=120, fg="blue", bg='white', undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#Scroll Bar Config
text_scroll.config(command=my_text.yview)

#Menu Bar
my_menu = Menu(root)
root.config(menu=my_menu)

#New File Function
def file_new():
    my_text.delete('1.0', END)
    root.title('New File - PY Text Editor')

#Open File Function
def file_open():
    my_text.delete('1.0', END)
    #Shows Open file dialogue and sets chosen file = 'f'
    f = filedialog.askopenfilename()
    #Opens selected file in read format
    f = open(f, 'r')
    #Inserts file into 'my_text' widget
    my_text.insert(END, f.read())

#Save File Function
def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(my_text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()

#Menu - File
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="Save", command=file_save)
file_menu.add_command(label="Quit", command=root.destroy)

#Menu - Edit
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)

root.mainloop()