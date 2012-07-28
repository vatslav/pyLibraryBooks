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
import random,datetime, time



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
    conn = sqlite3.connect('db6.sqlite')
    cur = conn.cursor()
except:
    showerror('Ошибка', 'Ошибка при рабое с базой данных, возможно ее кто-то уже использует.')
    exit()
def ViewBooks():
    bookList = ScrolledList(parent=root)
    bookList.listbox.config(height=15,width=50)
    bookList.grid(column=4,row=0)
#если среди аргументов есть Entry, замещает его на его содержимое, т.е. на entry.get() -генератор
def genGet(*values):
    for obj in values[0]:
        if str(type(obj)) == "<class 'tkinter.Entry'>":
            yield obj.get()
        else:yield obj

#если среди аргументов есть Entry, замещает его на его содержимое, т.е. на entry.get() -возвращает картеж, в том же порядкке
def funcGet(*values):
    tmp=[]
    #print(values,type(values),len(values))
    for obj in values[0]:
        if str(type(obj)) == "<class 'tkinter.Entry'>":
            tmp.append(obj.get())
        else:
            tmp.append(obj)
    return tuple(tmp)

#проверяет, все ли поля заполнены
def testCompair(*args):
    args = funcGet(*args)
    if len(args) == 1:args=args[0] #помогает от звездочки:)
    for obj in args:
        if not obj:
            showerror('Ошибка',"Пожалуйста, заполните все поля ввода данных")
            return False
    return True

#крутяцкая функция!:)
def execsql(request1,*values):
    if len(values):
        values = funcGet(*values)
    try:
        if not len(values):cur.execute(request1)
        else:
            cur.execute(request1,values)
            for obj in cur:
                print(obj)
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        conn.commit()
        for line in cur:
            yield line

def inscsql(request1,*values):
    if len(values):
        values = funcGet(*values)
    try:
        if not len(values):cur.execute(request1)
        else:
            cur.execute(request1,values)
            for obj in cur:
                print(obj)
    except sqlite3.IntegrityError as NoUn:
        showerror('Ошибка', NoUn)
        return None
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
        return None

    else:
        conn.commit()
        return
def tuple2str(t):
    tmp = ''
    for x in t:
        tmp = tmp + str(x) +','
    tmp = tmp[0:-1]
    return tmp

def time2sec(t):
    return time.mktime(t.timetuple())
def sec2time(t):
    return datetime.datetime.fromtimestamp(float(t))



def handlerBrackets(s):
    return '('+s+')'

def addBook():

    def OkAct():
        ts = datetime.datetime.today()
        args = (ISBN,bbk,author,title,years,publisher,keywords,sity,ts)
        #args = (random.randint(0,9999),20,3,4,5,6,7,8,ts)
        #if not testCompair(args):return #8
       #req = 'INSERT INTO books ' + handlerBrackets( tuple2str(args) ) + 'values(?,?,?,?,?,?,?,?)'
        req = 'INSERT INTO books (ISBN,autors,title,years,publisher,keywords,city,bbk,createTime) values(?,?,?,?,?,?,?,?,?)'
        #req2 = 'values(?,?,?,?,?,?,?,?,?,?)'
        print(req, args)
        if inscsql(req,args):
            showinfo('Успех',"Книги добавлена")

    def OkAct1():
        for x in execsql('select * from users where name=?',('марк',)):
            print(x)


    def cancelAct():
        leftFrame.grid_remove()
        rightFrame.grid_remove()
        bottom.grid_remove()
        #делаем фреймы видимыми
    try:
        if not leftFrame.winfo_viewable():
            leftFrame.grid()
            rightFrame.grid()
            bottom.grid()
            ISBN.focus_set()
            #а если фреймы еще не создавались, то создаем их
    except UnboundLocalError:


        leftFrame  = Frame(root)
        rightFrame = Frame(root)
        bottom     = Frame(root)

        button1 = Button(bottom,text='Подтвердить',command=lambda: OkAct()  )
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
        bbk      = Entry(leftFrame)
        author = Entry(leftFrame)
        title = Entry(leftFrame)
        years     = Entry(leftFrame)
        publisher = Entry(leftFrame)
        keywords  = Entry(leftFrame)
        sity      = Entry(leftFrame)

        ISBN.grid(row=0, column=1,padx=5,pady=5,columnspan=2,ipadx=5)
        bbk.grid(row=1, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
        author.grid(row=2, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
        title.grid(row=3, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
        years.grid(row=4, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
        publisher.grid(row=5, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
        keywords.grid(row=6, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
        sity.grid(row=7, column=1,padx=5,pady=5,columnspan=5,ipadx=5)


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
