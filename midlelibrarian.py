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

#крутяцкая функция!:)
def execsql(request1,*values):
    if len(values):
        tmp=[]
        for obj in values[0]:
            if str(type(obj)) == "<class 'tkinter.Entry'>":
                tmp.append(obj.get())
            else:tmp.append(obj)
        values = tuple(tmp)
    try:
        if not len(values):cur.execute(request1)
        else:
            cur.execute(request1,values)
            for obj in cur:
                print(obj)
        for line in cur:
            yield line
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        conn.commit()


def addBook():
    def OkAct(q):
        print(type(q))
        #s=''
        s = execsql('INSERT INTO books values(?,?,?,?,?,?,?,?)',(ISBN,author,2,4,5,6,7,8))
        #s = execsql('select * from users where name="марк"')
        '''
        ISBN = Entry
        author = Ent
        title = Entr
        years     =
        publisher =
        keywords  =
        sity      =
        ISBN.grid(ro
        author.grid(
            title.grid(r
        years.grid(r
        publisher.gr
        keywords.gri
        sity.grid(ro
        bbk.grid(row
        '''
        for line in s:
            print(line)

    def OkAct1():
        for x in execsql('select * from users where name=?',('марк',)):
            print(x)


    def cancelAct():
        leftFrame.grid_remove()
        rightFrame.grid_remove()
        bottom.grid_remove()

    leftFrame  = Frame(root)
    rightFrame = Frame(root)
    bottom     = Frame(root)

    button1 = Button(bottom,text='Подтвердить',command=lambda: OkAct(ISBN)  )
    button2 = Button(bottom,text='Отмена' ,command=lambda: cancelAct () )
    Label(leftFrame, text="ISBN").grid(row=0)
    Label(leftFrame, text="Автор").grid(row=1)
    Label(leftFrame, text='Название').grid(row=2)
    Label(leftFrame, text='годы').grid(row=3)
    Label(leftFrame, text='издательство').grid(row=4)
    Label(leftFrame, text='ключевые слова').grid(row=5)
    Label(leftFrame, text='город').grid(row=6)
    Label(leftFrame, text='ББК').grid(row=7)



    ISBN = Entry(leftFrame)
    author = Entry(leftFrame)
    title = Entry(leftFrame)
    years     = Entry(leftFrame)
    publisher = Entry(leftFrame)
    keywords  = Entry(leftFrame)
    sity      = Entry(leftFrame)
    bbk      = Entry(leftFrame)
    ISBN.grid(row=0, column=1,padx=5,pady=5,columnspan=2,ipadx=5)
    author.grid(row=1, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    title.grid(row=2, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    years.grid(row=3, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    publisher.grid(row=4, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    keywords.grid(row=5, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    sity.grid(row=6, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    bbk.grid(row=7, column=1,padx=5,pady=5,columnspan=5,ipadx=5)

    button1.grid(row=3, column=0,columnspan=1,ipadx=5,ipady=5,rowspan=10)
    button2.grid(row=3, column=2,columnspan=2,ipadx=5,ipady=5)
    leftFrame.grid(row=0, column=4)
    rightFrame.grid(row=0,column=5)
    bottom.grid(row=1,column=4)
    ISBN.focus_set()
    #s = execsql('INSERT INTO books values(?,?,?,?,?,?,?,?)',(ISBN.get(),author.get(),3,4,5,6,7,8))
    #for line in s:
    #    print(line)


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
