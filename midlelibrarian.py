#from main import e1

__author__ = 'Вячеслав'
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from sys import exit as ext
from scrolledlist import *
import sqlite3
from hashlib import md5
import re



b1  = '<Button-1>'
b1w = '<Double-1>'
b2  = '<Button-2>'
tab=''
specialty = ("Библитекарь", "Читатель", "Адинистратор")
root=True #кнопки
root=True #таблица
numberUser=0
NumberUserCur=0

try:
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
except:
    showerror('Ошибка', 'Ошибка при рабое с базой данных, возможно ее кто-то уже использует.')
    exit()
def ViewBooks():
    bookList = ScrolledList(parent=root)
    bookList.listbox.config(height=15,width=50)
    bookList.grid(column=4,row=0)

def addBook():

    leftFrame  = Frame(root)
    rightFrame = Frame(root)
    bottom     = Frame(root)

    button1 = Button(bottom,text='Подтвердить',command=(lambda: creatUserAct(e1,e2,e3,roleBox) ) )
    button2 = Button(bottom,text='Отмена' ,command=(lambda: root.destroy() ) )
    randPas = Button(bottom,text='Случайный пароль' ,command=(lambda: randPasAct() ) )
    Label(leftFrame, text="Логин").grid(row=0)
    Label(leftFrame, text="Пароль").grid(row=1)
    Label(leftFrame, text='Подтвердите пароль').grid(row=2)
    Label(rightFrame, text='Тип учетной записи').grid(column=0)
    e1 = Entry(leftFrame)
    e2 = Entry(leftFrame)
    e3 = Entry(leftFrame)

    roleBox = Listbox(rightFrame)
    [roleBox.insert('end',x) for x in specialty]
    roleBox.config(height=4,width=20)
    roleBox.grid(row=3,column=0)
    e1.grid(row=0, column=1,padx=5,pady=5,columnspan=2,ipadx=5)
    e2.grid(row=1, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    e3.grid(row=2, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    randPas.grid(row=3, column=1,ipadx=5,rowspan=10)
    button1.grid(row=3, column=0,columnspan=1,ipadx=5,ipady=5,rowspan=10)
    button2.grid(row=3, column=2,columnspan=2,ipadx=5,ipady=5)
    leftFrame.grid(row=0, column=4)
    rightFrame.grid(row=0,column=5)
    bottom.grid(row=1,column=4)
    e1.focus_set()



root=Tk()
root.title('Администрирование БД')
master = Frame(root)
accountingF = Frame(master)
getNdelF = Frame(master)
classifF = Frame(master)

issueB            = Button (accountingF,text='Выдача книг чиателю', command=lambda: ViewBooks() )
getB              = Button (accountingF,text='Прием книг у читателя',command=lambda:ViewBooks())
insertB           = Button (getNdelF,text='Добавление новой книги в фонд библиотеки',command=lambda:addBook() )
delB              = Button (getNdelF,text='Удаление книги')
cataloging        = Button (classifF,text='Каталогизация' )
classificationB   = Button (classifF,text='Классификация книг')

issueB.grid(padx=20,ipady=5)
getB.grid(padx=20,ipady=5)
insertB.grid(padx=20,ipady=5)
delB.grid(padx=20,ipady=5)
cataloging.grid(padx=20,ipady=5)
classificationB.grid(padx=20,ipady=5)

master.grid()
accountingF.grid(padx=20,ipady=5)
getNdelF.grid(padx=20,ipady=5,row=1)
classifF.grid(padx=20,ipady=5,row=2)


root.mainloop()
