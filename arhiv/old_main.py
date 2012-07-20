__author__ = 'Вячеслав'
#коннект в бд
#выбор типа пользователя
#работа в нем
from tkinter import *
from tkinter.messagebox import *
#from tkinter.ttk import *
from sys import exit as ext
import sqlite3
root = Tk()
err = Label(root,text='',bg='red')
b1  = '<Button-1>'
b1w = '<Double-1>'
b2  = '<Button-2>'
b2w = '<Double-2>'

try:
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
except:
    err['text'] = 'ошибка открытия базы данных'
    err.pack()
    err.mainloop()
    exit()
#cur.execute("")
#391 все из букс
for row in cur.execute("select * from books"):
    print(row)

def okAct(event):
    pass

def quit(event):
    ext()
    return

#GUI:
logW = Entry(root,width=20,bd=3)
pasW = Entry(root,width=20,bd=3)
okW = Button(root, text='Ok')
cancelW = Button(root, text='Cancel')
logL = Label(root, text='Логин')
pasL = Label(root, text='Пароль')



logL.pack(side=LEFT)
pasL.pack(side=LEFT)
logW.pack(side=RIGHT)
pasW.pack(side=RIGHT)
okW.pack(side=LEFT)
cancelW.pack(side=RIGHT)
okW.bind(b1,okAct)
okW.bind(b1w,quit)

#logL.drid(row=0,column=0)
#pasL.drid(row=1,column=0)
#logW.drid(row=0,column=1)
#pasW.drid(row=1,column=1)
#okW.drid(row=2,column=0)
#cancelW.drid(row=2,column=2)
okW.bind(b1,okAct)
okW.bind(b1w,quit)


root.mainloop()
print('finish')