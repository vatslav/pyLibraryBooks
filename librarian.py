__author__ = 'Вячеслав'
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from sys import exit as ext
import sqlite3
from hashlib import md5

b1  = '<Button-1>'
b1w = '<Double-1>'
b2  = '<Button-2>'
tab=''
root1=True #кнопки
root=True #таблица
conn = sqlite3.connect('library.db')
cur = conn.cursor()

def getTab(x=1,y=0):
    return tab.cells[x][y].value.get()
def setTab(x=1,y=0, val=None):
    global tab
    tab.cells[x][y].value.set(val)
def setTitile(val):
    global tab
    for i in range( len(val) ):

        tab.cells[0][i].value.set(val[i])

def exBut():
    root1.title('Создание нового пользователя')
    if getTab(1,0)=='' or getTab(1,2)=='' or getTab(1,1)=='':
        showerror('Ошибка ввода', "Пожалуйста, заполните все поля ввода")
    else:
        hsh = md5()
        hsh.update( getTab(1,1).encode('utf-8') )
        global root1,root,tab
        cur.execute("insert into users values (?,?,?)", (getTab(1,0),hsh.hexdigest() ,getTab(1,2)))
        conn.commit()
        #showinfo('Готово', 'Пользователь создан')
        setTab(0,0,'');setTab(0,1,'');setTab(0,2,'')
        root.destroy()


def creatUser():
    global tab,root1,root
    #root2 = Toplevel(root1)
    root = Toplevel(root1)
    #root1.withdraw(True)
    #root.title('table111')
    #root2.overrideredirect(True)
    tab = Table(root,3,2)
    tab.pack()
    setTitile(['Имя','Пароль','Тип пользователя'])
    com = Button(root,text='Подтвердить', command=(lambda: exBut() ) )
    com.pack()

def changeUser():
    global tab,root1,root
    pass




    #cur.execute("insert into users values (?,?,?)", ('kola','qwer',1))
    #conn.commit()

def ViewUser(name):
    request='select * from users where name="' + str(name) + '"'
    i=0;buf=""
    for s in cur.execute(request):
        buf=s
        i+=1
    if i>1: print("users table is invalid")
    if buf!='':
        return buf
    else:
        print('не найдено не одного юзера')
        return buf


class Cell(Entry):
    def __init__(self, parent):
        self.value = StringVar()
        Entry.__init__(self, parent, textvariable = self.value)

class Table(Frame):
    def __init__(self, parent, columns = 4, rows = 10):
        Frame.__init__(self, parent)
        self.cells = [[Cell(self) for i in range(columns)] for j in range(rows)]
        [self.cells[i][j].grid(row = i, column = j) for i in range(rows) for j in range(columns)]



def viewTable(x,y,r1,title=1):
    global root1,root
    y=y+1
    root = Toplevel(r1)
    tab = Table(root,x,y)
    tab.pack()
    com = Button(root,text='Подтвердить')
    com.pack()



def mymain():
    global root1
    root1=Tk()
    root1.title('Администрирование БД')
    viewAllBooks    = Button (text='посмотреть список книг')
    creatLibrarian  = Button (text='Создать/изменть  учетную запись библиотекаря', command=(lambda:creatUser()) )
    changeLibrarian = Button (text='Изменить  учетную запись библиотекаря', command=(lambda:changeUser()) )
    viewLibrarian   = Button (text='Посмотреть информацию о библиотекаре')

    #viewAllBooks.bind(b1,)
    #creatLibrarian.bind(b1,lambda: creatUser(root1))

    #viewAllBooks.pack(expand=False)
    #creatLibrarian.pack(expand=True)
    #viewLibrarian.pack()
    viewAllBooks.grid(padx=20,ipady=5)
    creatLibrarian.grid(columnspan=5,padx=20,ipady=5)
    viewLibrarian.grid(ipady=2)
    #


    root1.mainloop()



mymain()