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
root1=True #кнопки
root=True #таблица
numberUser=0
NumberUserCur=0
try:
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
except:
    showerror('Ошибка', 'Ошибка при рабое с базой данных, возможно ее кто-то уже использует.')
    exit()






def mymain():
    #print('mymain init)')
    global root1
    root1=Tk()
    root1.title('Администрирование БД')
    viewAllBooks    = Button (text='посмотреть список книг')
    creatLibrarian  = Button (text='Создать учетную запись библиотекаря',   command=(lambda:creatUser()) )
    changeLibrarian = Button (text='Изменить  учетную запись библиотекаря', command=(lambda:changeUser()) )
    viewLibrarian   = Button (text='Посмотреть информацию о библиотекаре')

    viewAllBooks.grid(padx=20,ipady=5)
    creatLibrarian.grid(columnspan=5,padx=20,ipady=5)
    changeLibrarian.grid(columnspan=5,padx=20,ipady=5)
    viewLibrarian.grid(ipady=2)
    s=ScrolledList()
    print('da')

    root1.mainloop()


mymain()