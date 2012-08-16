__author__ = 'Вячеслав'
from tkinter import *
from tkinter.ttk import *
root = Tk()
content = Frame(root)
frame = Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
namelbl = Label(content, text="Name")
name = Entry(content)
content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)

root.mainloop()

