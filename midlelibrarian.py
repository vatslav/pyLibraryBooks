#from main import e1

__author__ = 'Вячеслав'
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from sys import exit as ext
from scrolledlist import *
import sqlite3,re,random,datetime, time
from hashlib import md5
from share_data import *

flags ={'выдать_книги':False,'добавить_книгу':False}
fieldOfBooksRus = ('ISBN', 'ББК', 'Автор', 'Название', 'Год издания', 'Издательство', 'ключивые слова', 'город' )
fieldOfBooks = ('ISBN','bbk', 'autors', 'title', 'years', 'publisher', 'keywords', 'city')
fieldOfBooksstr = 'ISBN,bbk,autors,title,years,publisher,keywords,city'
b1  = '<Button-1>'
b1w = '<Double-1>'
b2  = '<Button-2>'
specialty = ("Библитекарь", "Читатель", "Адинистратор")
firstIn = True


#маска для поиска, индекс столбца в бд, по которому делаем поиск, сортируем по
def getBooks(mask=None,index=3,table='books', sortby='title'): #фильтр на книги
    #print('mask=%s, index=%d, sort=%s' %(mask,index,sortby))
    #index += 1
    if mask:
        template = re.compile(mask)


    request = 'select ISBN,bbk,autors,title,years,publisher,keywords,city from '+ table + ' ORDER BY low(' +sortby+ ') COLLATE sort' #выводим, с сортировкой без учета регистра по столбцу name
    print(request)
    try:
        for row in cur.execute(request):
            if not mask:
                yield row
            else:
                pb = template.search(str(row[index]).lower())
                if pb:
                    yield row
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        conn.commit()



def ViewBooks():
    global flags,issueF,fieldOfBooksRus

    def xx():#вернет название всех полей
        for x in execsql('PRAGMA table_info("books")'):yield x[1]

    def handlerPress(event):
        global firstIn
        bookList.clearlist()#index=rb.reportIndex()
        if firstIn:
            firstIn = False
            tmp = (text.get())
            tmp = tmp.replace('Найти','')
            text.set(tmp)
        txt =text.get()
        txt = txt.lower()
        if rb.reportIndex()==4:
            pass

        for x in getBooks(txt,index=rb.reportIndex(),sortby=fieldOfBooks[rb.reportIndex()]):
            bookList.listbox.insert('end',x)


    def nameOfrb():
        for x in fieldOfBooksRus:
            yield x


    hideFrames();
    if flags['выдать_книги']==True:
        issueF.grid()
        return
    flags['выдать_книги'] = True
    issueF = Frame(root)
    midlle, bottom, right = Frame(issueF), Frame(issueF), Frame(issueF)

    Button(bottom, text='Ок',command=lambda:handlerPress(None)  ).grid(row=0)
    Button(bottom, text='Отмена',command=lambda:issueF.grid_remove()).grid(row=0,column=1)
    midlle.grid(column=4,row=0)
    bottom.grid(column=4,row=1)
    right.grid(column=5,row=0)

    sortFind = Frame(right)
    sortFind.grid()
    var  = IntVar(0)
    def qq():
        for x in ['q','w','z']:
            yield x

    rb = RadioBut(parent=sortFind,opt=nameOfrb(),titile='Сортировать и искать по',default=fieldOfBooksRus[3])
    print('======',rb.report())
    text =StringVar()
    find = Entry(midlle,textvariable=text)

    #print(rb.report())
    bookList = ScrolledList(parent=midlle,options=getBooks( ) )


    bookList.listbox.config(height=25,width=100)
    bookList.grid(column=0,row=0)
    find.grid(row=2,padx=20,ipady=5)
    issueF.grid(column=4,row=0)
    find.focus()
    root.bind('<KeyPress>',handlerPress)
    text.set('Найти')
    #root1.bind('<Return>',handkerEnter)
    #root1.bind('<Escape>',handkerEscape)
    #root.mainloop()

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
        return True

def tuple2str(t):
    tmp = ''
    for x in t:
        tmp = tmp + str(x) +','
    tmp = tmp[0:-1]
    return tmp
#тек. время в секунды
def time2sec(t):
    return time.mktime(t.timetuple())
#секунды в время
def sec2time(t):
    return datetime.datetime.fromtimestamp(float(t))
#дабавить скобки к запросу
def handlerBrackets(s):
    return '('+s+')'


def hideFrames():
    global issueF,getF,insertF,delF, catalogingF, classificationF
    for frame in [issueF,getF,insertF,delF, catalogingF, classificationF]:
        frame.grid_remove()

def addBook():
    global insertF
    def OkAct():
        ts = datetime.datetime.today()
        args = (ISBN,bbk,author,title,years,publisher,keywords,sity,ts)
        #args = (random.randint(0,9999),20,3,4,5,6,7,8,ts)
        if not testCompair(args):return
        request = 'INSERT INTO books (ISBN,autors,title,years,publisher,keywords,city,bbk,createTime) values(?,?,?,?,?,?,?,?,?)'
        print()
        if inscsql(request,args):
            showinfo('Успех',"Книги добавлена")
    hideFrames()
    if flags['добавить_книгу']==True:
        insertF.grid()
        return
    flags['добавить_книгу'] = True

    insertF = Frame(root)
    leftFrame  = Frame(insertF)
    rightFrame = Frame(insertF)
    bottom     = Frame(insertF)

    button1 = Button(bottom,text='Подтвердить',command=lambda: OkAct()  )
    button2 = Button(bottom,text='Отмена' ,command=lambda: insertF.grid_remove() )
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
    insertF.grid(row=0,column=4)
    ISBN.focus_set()
def view():
    for x in getBooks():
        print(x)

def iterColumnBooks():
    i =execsql('''SELECT name FROM sqlite_master
    WHERE type='table'
    ORDER BY name;''')
    for x in i:
        print(x)

root=Tk()
root.title('Администрирование БД')
master = Frame(root)
accountingF = Frame(master)
getNdelF = Frame(master)
classifF = Frame(master)

#view()
iterColumnBooks()

#Dataset с полями CID, NAME, TYPE, NOTNULL, DFLT_VALUE, PK
state = ''
buttons = []


issueB            = Button (accountingF,text='Выдача книг чиателю', command=lambda: ViewBooks() );
getB              = Button (accountingF,text='Прием книг у читателя',command=lambda:ViewBooks())
insertB           = Button (getNdelF,text='Добавление новой книги в фонд библиотеки',command=lambda:addBook() )
delB              = Button (getNdelF,text='Удаление книги')
cataloging        = Button (classifF,text='Каталогизация' )
classificationB   = Button (classifF,text='Классификация книг')
#фремы подфункций
issueF            = Frame(root)
getF              = Frame(root)
insertF           = Frame(root)
delF              = Frame(root)
catalogingF       = Frame(root)
classificationF   = Frame(root)
frames = (issueF,getF,insertF,delF, catalogingF, classificationF )



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
