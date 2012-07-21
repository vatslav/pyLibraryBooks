#from main import e1

__author__ = 'Вячеслав'
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from sys import exit as ext
import scrolledlist
import sqlite3
from hashlib import md5



b1  = '<Button-1>'
b1w = '<Double-1>'
b2  = '<Button-2>'
tab=''
root1=True #кнопки
root=True #таблица
try:
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
except:
    showerror('Ошибка', 'Ошибка при рабое с базой данных, возможно ее кто-то уже использует.')
    exit()

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
        cur.execute("insert into users values (?,?,?)", (getTab(1,0).lower(),hsh.hexdigest() ,getTab(1,2)))
        conn.commit()
        #showinfo('Готово', 'Пользователь создан')
        setTab(0,0,'');setTab(0,1,'');setTab(0,2,'')
        root.destroy()

def creatUserAct(e1,e2,e3,userBox):
    if e1.get()=='' or e2.get()=='' or e3.get()=='':
        showerror('Ошибка ввода', "Пожалуйста, заполните все поля ввода")
        return
    if e2.get()!=e3.get():
        showerror('Ошибка', 'Введенные пароли не совпадают')
        return
    hsh = md5()
    hsh.update( e2.get().encode('utf-8') )
    hashpass = hsh.hexdigest()

    #cur.execute("insert into users values (?,?,?)", ('kola','qwer',1))
    #conn.commit()
    name = e1.get().lower()
    #sel = userBox.get( userBox.curselection() )
    try:
        role = userBox.get( userBox.curselection() )
        #print(sel)
    except TclError as notSelect:
        showerror('Ошибка ввода', "Пожалуйста, выбирите тип учетной записи пользователя")
        return
    try:

        insUserValue = (name, hashpass, role )
        insUserComand = 'INSERT INTO users values (?,?,?)'
        cur.execute(insUserComand,insUserValue)
    except sqlite3.DatabaseError as err:
        print('Ошибка', err)
        errMsg = 'Ошиюбка выполнения запроса:\n"' + str(err) + '"'
        showerror('Ошибка', errMsg)
    else:
        conn.commit()
        root.destroy()#====== переставить строкой ниже, если научусь скрывать главное окно
        showinfo('Успех', "Новый пользователь создан")




def creatUser():

    global tab,root1,root
    root = Toplevel()
    leftFrame  = Frame(root)
    rightFrame = Frame(root)
    button1 = Button(root,text='Подтвердить',command=(lambda: creatUserAct(e1,e2,e3,roleBox) ) )
    button2 = Button(root,text='Отмена' ,command=(lambda: root.destroy() ) )

    Label(leftFrame, text="Логин").grid(row=0)
    Label(leftFrame, text="Пароль").grid(row=1)
    Label(leftFrame, text='Подтвердите пароль').grid(row=2)
    Label(rightFrame, text='Тип учетной записи').grid(column=3)
    e1 = Entry(leftFrame)
    e2 = Entry(leftFrame)
    e3 = Entry(leftFrame)
    elements = ("Библитекарь", "Читатель", "Адинистратор")
    roleBox = Listbox(rightFrame)
    [roleBox.insert('end',x) for x in elements]
    roleBox.grid(row=1,column=3)
    #scrolledlist.ScrolledList(elements)
    #scrolledlist.ScrolledList.pack()
    #scrolledlist.ScrolledList.grid(row=4, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    e1.grid(row=0, column=1,padx=5,pady=5,columnspan=2,ipadx=5)
    e2.grid(row=1, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    e3.grid(row=2, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    button1.grid(row=3, column=0,columnspan=1,ipadx=5,ipady=5,rowspan=10)
    button2.grid(row=3, column=2,columnspan=2,ipadx=5,ipady=5)
    leftFrame.grid(row=0, column=0)
    rightFrame.grid(row=0,column=4)
    e1.focus_set()
    root.grab_set()
    root.wait_window()
    #root.grab_set()
    #root.wait_window()
    #root.mainloop()
    #root.destroy()
    #focus_set()




def changeUser():
    global tab,root1,root
    root = Toplevel()
    leftFrame  = Frame(root)
    rightFrame = Frame(root)





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
    #print('mymain init)')
    global root1
    root1=Tk()
    root1.title('Администрирование БД')
    viewAllBooks    = Button (text='посмотреть список книг')
    creatLibrarian  = Button (text='Создать учетную запись библиотекаря',   command=(lambda:creatUser()) )
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


#print('librarian start now')
mymain()