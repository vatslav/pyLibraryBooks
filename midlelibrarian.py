#from main import e1

__author__ = 'Вячеслав'
from tkinter import *
from tkinter.messagebox import *

from sys import exit as ext
from scrolledlist import *
import sqlite3,re,random,datetime, time
from hashlib import md5
from share_data import *
from copy import deepcopy

from tkinter.ttk import *

#поиск книг
flags ={'выдать_книги':False,'добавить_книгу':False}
fieldOfBooksRus = ('ISBN', 'ББК', 'Автор', 'Название', 'Год издания', 'Издательство', 'ключивые слова')
fieldOfBooks = ('ISBN','bbk', 'autors', 'title', 'years', 'publisher', 'keywords')
fieldOfBookD = {} #создадим словарь на оснве двух предыдущих картежей
if len(fieldOfBooks)!=len(fieldOfBooksRus):showerror('erroe','erroedict')
for x in range(len(fieldOfBooks)):
    fieldOfBookD[ fieldOfBooksRus[x] ] = fieldOfBooks[x]
#поиск читателя
rTableR = ('порядковый номер','Номер Абонемента', 'ФИО',"адресс","телефон","время создания") #имя для пользователя
rTableE = ('id',              'NomberAbonement' ,'fio', 'adress','telephone','create_time') #имя поля в бд
rTableS = [0,                   1,                  1,      1,      1,          0] #флаг, отвечающий за общедоступна ли это поле
rTableA = [0,1,1,1,0,0] #автивно ли это поле
rTableD = {}
readerT = {}
for x in range(len(rTableR)):
    rTableD[rTableR[x]]=list((rTableE[x],rTableA[x],rTableS[x],))
for x in range(len(rTableR))[1:-1]:
    readerT[rTableR[x]]=list((rTableE[x],rTableA[x]))
readermy = []
for x in range(len(rTableR))[1:-1]:
    readermy.append(list((rTableR[x],rTableE[x],rTableA[x])))

#имя для пользователя /\ в бд, для всех, поумолчанию тру?
#print(list(rTableD.items()))

b1  = '<Button-1>'
b1w = '<Double-1>'
b2  = '<Button-2>'
specialty = ("Библитекарь", "Читатель", "Адинистратор")
firstIn = True


#маска для поиска, индекс столбца в бд, по которому делаем поиск, сортируем по
def getBooks(mask=None,index=3,table='books', sortby='title',field={},state={}): #фильтр на книги
    global fieldOfBooks
    if mask:
        template = re.compile(mask)
    if not field or not state: #если запрос по всем стодбцам
        request = 'select ISBN,bbk,autors,title,years,publisher,keywords,city from ' + table + ' ORDER BY low(' +sortby+ ') COLLATE sort' #выводим, с сортировкой без учета регистра по столбцу name
    else:#оставляем толькоотмеченные столбцы
        request = 'select '
        tmp = list(fieldOfBooks)
        print(tmp)
        for key,value in field.items():
            if not state[key]:
                tmp.remove(value)
        tmp.insert(0,'ISBN') #полюому будет ISBN
        tmpstr = tuple2str(tmp)
        print(tmpstr)
        request = request + tmpstr + ' from '+table+' ORDER BY low(' +sortby+ ') COLLATE sort'
        try:
            index = tmp.index(sortby)
        except ValueError as er:
            showerror('Ошибка', er)
            return
    try:
        for row in cur.execute(request):
            if not mask:
                yield row
            else:
                #print(row)
                pb = template.search(str(row[index]).lower())
                if pb:
                    yield row[0],row[1:]
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        conn.commit()
#index=3,table='books', sortby='title',field={},state={}
def sqlmy(mask=None,req=None,r=[],table='', sortby='',shadow=''): #фильтр на книги
    global fieldOfBooks
    if mask:
        template = re.compile(mask)
    if req!=None:
        request=req
    else:
        if table=='' or sortby=='':
            showerror('Ошибка',"системная ошибка")
            print(table, 'table')
            print(sortby ,' sortby')
            return
        nfields = r
        nfieldstr = tuple2str(nfields)
        if shadow:
            nfieldstr = shadow + ',' + nfieldstr
        sortby = nfields[sortby]

        #select имена полей from имя_таблицы Order By low сортировать по полю
        request = 'select ' + nfieldstr + ' from ' + table + ' ORDER BY low(' +sortby+ ') COLLATE sort'
        print(request)
        try:
            index = nfields.index(sortby)
        except ValueError as er:
            showerror('Ошибка',er)
            return
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


def ViewBooks():#выдача книг читателю
    global flags,issueF,fieldOfBooksRus,firstIn
    def handlerPress(event):
        global firstIn
        bookList.clearlist()#index=rb.reportIndex()


        if firstIn and event!='служебный поиск':
            firstIn = False
            text.set( text.get().replace('Найти','') )
            #text.set(tmp)
        txt =text.get().lower()#txt = txt.lower()
        if rb.reportIndex()==4:
            pass
        cursort = fieldOfBooksRus[rb.reportIndex()]
        #print('cursort',cursort)
        chekLayers.setFlag(cursort)
        if event=='служебный поиск':
            txt=''

        for x in range(len(storageisbn)):storageisbn.pop()
        for x in getBooks(txt,index=rb.reportIndex(),sortby=fieldOfBooks[rb.reportIndex()],state=chekLayers.reportDict(),field=fieldOfBookD):
            isbn = x[0]
            x=x[1:]
            x = tuple2str(x)
            bookList.listbox.insert('end',x)
            storageisbn.append(isbn)

            #print(x,type(x),type(x[0]),type(x[4]))

    def nameOfrb():
        for x in fieldOfBooksRus:
            yield x
#==== begin                                         ================================
    def iss(isbns,books):
        def inserbd():
            if not userlist.getCur():return
            #inscsql('INSERT INTO ')


        tf = Toplevel(getF)
        def handeofind(event=True):
            curelem = rb.reportIndex()
            chb.setFlagByIndex(curelem)
            txt = findtext.get()
            print(txt)
            userlist.clearlist()
            print(chb.getSetup())


            for x in sqlmy(mask=txt,r=chb.getSetup(),table='readers',sortby=rb.reportIndex(),shadow='NomberAbonement'):
                x = tuple2str(x)
                userlist.listbox.insert('end',x)

        centr,bottom,top,right = Frame(tf), Frame(tf), Frame(tf), Frame(tf)
        #userGen = (x for x in sqlmy(mask=txt,r=readermy,table='readers',sortby=r////b.reportIndex()))
        userlist = ScrolledList(parent=centr)
        userlist.listbox.config(height=25,width=120)
        #number = StringVar() #поле ввода имени
        findtext = StringVar()
        fent = Entry(bottom, textvariable=findtext)
        fent.grid(row=0,column=0)
        Button(bottom,text='Ok', command=lambda:inserbd() ).grid(row=1)
        Button(bottom,text='Отмена', command=lambda:tf.destroy()).grid(row=1,column=1)
        Button(bottom,text='Поиск', command=lambda:handeofind()).grid(row=1,column=2)
        subbotton = Frame(bottom)
        subbotton.grid(row=0,column=0,padx=25,pady=25)
        #Entry(bottom, textvariable=number).grid(row=1)
        options = (x[0] for x in readermy)
        print(options)
        print(list(options))
        #optchb = ( (x[0],x[1]) for x in readermy)

        chb = modernchekbutton(parent=top,title='отображать поля:',opt=( (x[0],x[1]) for x in readermy))
        rb = RadioBut(parent=right, titile='Сортировать и искать по:',opt=(x[0] for x in readermy),default=list((x[0] for x in readermy))[0])
        chb.setFlagByIndex(0)
        chb.setFlagByIndex(1)
        print(chb.getSetup())
        centr.grid(row=1,column=4)
        bottom.grid(row=2,column=4)
        top.grid(row=0,column=4)
        right.grid(row=1,column=5)
        handeofind()
        maxlenttitile = len(books[0])
        for x in books: # не работает т.к.список книг и юзеров в одном фрейме и размер по Х задается макс из двух
            if len(x)>maxlenttitile:
                maxlenttitile=len(x)
        selectbooks = ScrolledList(parent=centr)#книшки которые уже выбрали
        selectbooks.listbox.config(height=len(isbns),width=maxlenttitile)
        selectbooks.clearlist()
        #print('isbn=',isbns)
        for x in books:
            selectbooks.listbox.insert('end',x)

        #root.focus()
        handlecancel = lambda Event:tf.destroy()
        root.bind('<KeyPress>',handeofind)
        root.bind('<Return>',  handeofind)
        root.bind('<Escape>',handlecancel)




        fent.focus_set()
        #getF.grab_set()
        #getF.wait_window()



    #===================    end==========
    hideFrames();
    if flags['выдать_книги']==True:
        issueF.grid()
        return
    flags['выдать_книги'] = True
    issueF = Frame(root)
    midlle, bottom, right = Frame(issueF), Frame(issueF), Frame(issueF)
    def handlOk(Event=True):
        index, books = bookList.getCurMulti()
        tmp = []  #текущие выбранные тут тепер хранитяться, после ок
        for x in index:
            tmp.append(storageisbn[x-1]) #-1выведена эмпирически
        books = list(books)
        iss(tmp,books) #отправляеем индексы и названия
    Button(bottom, text='Ок',command=lambda:handlOk() ).grid(row=0)
    Button(bottom, text='Отмена',command=lambda:issueF.grid_remove()).grid(row=0,column=1)
    midlle.grid(column=4,row=0)
    submidle1, submidle2 = Frame(midlle),Frame(midlle)
    submidle1.grid(row=0)
    submidle2.grid(row=1)
    bottom.grid(column=4,row=1)
    right.grid(column=5,row=0)

    storageisbn = []

    rb = RadioBut(parent=right,opt=nameOfrb(),titile='Сортировать и искать по:',default=fieldOfBooksRus[3])
    #rb['command']=lambda:print('nhfnhf!!')

    text =StringVar()
    find = Entry(midlle,textvariable=text)

    chekLayers = chekbutton(parent=submidle1,title='Отображаемые поля:',opt=nameOfrb())
    def hand():handlerPress('служебный поиск')
    chekLayers.setComand(hand)
    titname = []
    titname = list(fieldOfBooksRus[2:4])
    titname.append(fieldOfBooksRus[6])
    for name in titname:
        chekLayers.setFlag(name)
    bookList = ScrolledList(parent=submidle2,options=getBooks( ) )
    handlerPress('чижика собаку, кошку забичку!')#убираем фигурные скобки и деактивизируем первыйfirstIn

    bookList.listbox.config(height=25,width=80,font=('courier'),selectmode=MULTIPLE)#EXTENDED    MULTIPLE SINGLE
    bookList.listbox.ff=lambda Event:print('tada')
    bookList.setAct(handlOk)
    #bookList.listbox.bind('<Double-1>', bookList.listbox.ff)
    bookList.grid(column=0,row=0)
    find.grid(column=0,row=2,padx=20,ipady=5)
    Button(bottom,text='Найти',command=lambda:handlerPress(1)).grid(column=2,row=0,padx=20,pady=5)
    issueF.grid(column=4,row=0)
    find.focus()
    def handlerCancel(event):issueF.grid_remove()

    #root.bind('<KeyPress>',handlerPress)
    root.bind('<Return>',  handlerPress)
    root.bind('<Escape>',handlerCancel)
    text.set('Найти')
    firstIn = True
    def rederforbook(row):
        pass

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
    for frame in [issueF,getF,insertF,delF, catalogingF, classificationF,addreaderF,delreaderF]:
        frame.grid_remove()

def viewreader():#!dslfxf
    #имя для пользователя /\ в бд, для всех, поумолчанию тру?
    hideFrames()
    if windows['прием_книг'][1]:
        windows['прием_книг'][0].grid()
        handlecancel = lambda event:getF.grid_remove()

        #root.bind('<KeyPress>',handeofind)
        #root.bind('<Return>',  handeofind)
        #root.bind('<Escape>',handlecancel)
        return
    windows['прием_книг'][1] = True



    def handeofind(event=True):
        curelem = rb.reportIndex()
        chb.setFlagByIndex(curelem)
        txt = findtext.get()
        print(txt)
        userlist.clearlist()
        for x in sqlmy(mask=txt,r=chb.getSetup(),table='readers',sortby=rb.reportIndex()):
            x = tuple2str(x)
            userlist.listbox.insert('end',x)
    centr,bottom,top,right = Frame(getF), Frame(getF), Frame(getF), Frame(getF)
    #userGen = (x for x in sqlmy(mask=txt,r=readermy,table='readers',sortby=r////b.reportIndex()))
    userlist = ScrolledList(parent=centr)
    userlist.listbox.config(height=25,width=120)
    userlist.setAct(handeofind)
    #number = StringVar() #поле ввода имени
    findtext = StringVar()
    fent = Entry(bottom, textvariable=findtext)
    fent.grid(row=0,column=0)
    Button(bottom,text='Ok', command=lambda:handeofind() ).grid(row=1)
    Button(bottom,text='Отмена', command=lambda:getF.grid_remove()).grid(row=1,column=1)
    #Entry(bottom, textvariable=number).grid(row=1)
    options = (x[0] for x in readermy)
    print(options)
    print(list(options))
    chb = modernchekbutton(parent=top,title='отображать поля:',opt=( (x[0],x[1]) for x in readermy) )
    rb = RadioBut(parent=right, titile='Сортировать и искать по:',opt=(x[0] for x in readermy),default=list((x[0] for x in readermy))[0])
    chb.setFlagByIndex(0)
    chb.setFlagByIndex(1)
    hand = lambda Event:handeofind
    chb.setComand(hand)

    centr.grid(row=1,column=4)
    bottom.grid(row=2,column=4)
    top.grid(row=0,column=4)
    right.grid(row=1,column=5)
    getF.grid(column=4,row=0)
    handeofind()
    handlecancel = lambda event:getF.grid_remove()

    #root.focus()

    root.bind('<KeyPress>',handeofind)
    root.bind('<Return>',  handeofind)
    root.bind('<Escape>',handlecancel)


def addBook():
    global insertF
    def OkAct(event=True):
        ts = datetime.datetime.today()
        args = (ISBN.get(),bbk.get(),author.get(),title.get(),years.get(),publisher.get(),keywords.get(),sity.get(),ts)

        #args = (random.randint(0,9999),20,3,4,5,6,7,8,ts)
        if not testCompair(args):return
        ptr = spinval.get()
        try:
            ptr = int(ptr)
        except ValueError as ve:
            showerror('Error','Количество экзмепляров должно быть натуральным числом')
            return
        if ptr<1:
            showerror('Error','Количество экзмепляров должно быть больше нуля')
            return
        if ptr>100:
            #showwarning('Опсно!','Вы не ошиблись нулем?')
            msg = 'Количество экземпляров ' + str(ptr) + '\nОперация ввода такого количество экземпляров может занять некоторое время\nВы ввели все верно?'
            if askyesno('Проверка', msg):
                pass
            else:
                return

        request = 'INSERT INTO books (ISBN,autors,title,years,publisher,keywords,city,bbk,createTime) values(?,?,?,?,?,?,?,?,?)'
        print()
        if inscsql(request,args):
            showinfo('Успех',"Книги добавлена")
        else:
            return
        ts = datetime.datetime.today()
        #у меня не вышло два следующих запроса объединить в один, лист используется для преообразования генератора
        #получается список в котором кортеж в котором число, поэтому так:


        tmp = list(execsql('SELECT (id) FROM books WHERE ISBN=?',(ISBN.get(),) ) )[0][0]
        for x in range(ptr):
            if not inscsql('INSERT INTO exemplars (classbook,create_time) VALUES (?,?) ',(tmp,ts) ):
                return #None вернется когда в inscql возникнет ошибка, и потоу здесь только return

        if ptr > 0:
            msg = "Экземпляров добавлено: " + str(ptr)
            showinfo('Успех', msg)
            #print(list(inscsql))
        #s=sqlmy('SELECT * FROM EXEMPLARS')
        s = cur.execute('SELECT * FROM EXEMPLARS')
        for x in s:
            print(x)
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
    Label(leftFrame, text='Количество экземпляров').grid(row=8)



    ISBN = Entry(leftFrame)
    bbk      = Entry(leftFrame)
    author = Entry(leftFrame)
    title = Entry(leftFrame)
    years     = Entry(leftFrame)
    publisher = Entry(leftFrame)
    keywords  = Entry(leftFrame)
    sity      = Entry(leftFrame)
    exemplars = Entry(leftFrame)
    spinval = StringVar()
    Spinbox(leftFrame, from_=1.0, to=100.0, textvariable=spinval).grid(row=8,column=1,padx=5,pady=5,columnspan=2,ipadx=5)
    ISBN.grid(row=0, column=1,padx=5,pady=5,columnspan=2,ipadx=5)
    bbk.grid(row=1, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    author.grid(row=2, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    title.grid(row=3, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    years.grid(row=4, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    publisher.grid(row=5, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    keywords.grid(row=6, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    sity.grid(row=7, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    #exemplars.grid(row=8, column=1,padx=5,pady=5,columnspan=5,ipadx=5)

    button1.grid(row=3, column=0,columnspan=1,ipadx=5,ipady=5,rowspan=10)
    button2.grid(row=3, column=2,columnspan=2,ipadx=5,ipady=5)
    leftFrame.grid(row=0, column=4)
    rightFrame.grid(row=0,column=5)
    bottom.grid(row=1,column=4)
    insertF.grid(row=0,column=4)
    ISBN.focus_set()
    def handcancel(event):insertF.grid_remove()
    #root.bind('<KeyPress>',handlerPress)
    root.bind('<Return>',  OkAct)
    root.bind('<Escape>',handcancel)
def view():
    for x in getBooks():
        print(x)

def iterColumnBooks():
    i =execsql('''SELECT name FROM sqlite_master
    WHERE type='table'
    ORDER BY name;''')
    for x in i:
        print(x)

def delExemplars():
    pass

def addreader():
    hideFrames()
    if windows['добавить читателя'][1]:
        addreaderF.grid()
        return
    windows['добавить читателя'][1] = True
    addreaderF.grid(column=4,row=0,sticky='w')
    centr,bottom  = Frame(addreaderF),Frame(addreaderF)
    opt=[x[0] for x in readermy]
    txt = makeform(centr,fields=opt,w1=17,w2=30)

    Button(bottom,text="Ок",command=lambda:handl()).grid(column=0,row=1)
    Button(bottom,text="Отмена",command=lambda:addreaderF.grid_remove() ).grid(column=1,row=1)

    centr.grid(sticky='w')
    bottom.grid(sticky='w')
    def handl(event=True):
        for x in txt:
            if not x.get():
                showerror('Ошибка',"Не все поля заполнены")
                return
        val = [x.get() for x in txt]
        s=datetime.datetime.today()
        val.append(s)
        print(val)
        if inscsql('INSERT INTO readers (NomberAbonement ,fio, adress,telephone,create_time) values(?,?,?,?,?)',val):
            showinfo('Успех',"Читатель успешно добвален")


def delreader():
    pass
root=Tk()
root.title('Администрирование БД')
master = Frame(root)
#frame = Frame(content, borderwidth=5, relief="sunken",
accountingF = Frame(master)
getNdelF = Frame(master)
classifF = Frame(master)
readerAdmin = Frame(master)

#Dataset с полями CID, NAME, TYPE, NOTNULL, DFLT_VALUE, PK
state = ''
buttons = []


issueB            = Button (accountingF,text='Выдача книг чиателю', command=lambda: ViewBooks() );
getB              = Button (accountingF,text='Прием книг у читателя',command=lambda:viewreader() )
insertB           = Button (getNdelF,text='Добавление новой книги в фонд библиотеки',command=lambda:addBook() )
delB              = Button (getNdelF,text='Удаление книги')

addReader         = Button (readerAdmin,text='Добавление читателя',command=lambda:addreader()).grid(padx=20,ipady=5)
delReader         = Button (readerAdmin,text='Удаление читателя',command=lambda:delreader()).grid(padx=20,ipady=5)

cataloging        = Button (classifF,text='Каталогизация' )
classificationB   = Button (classifF,text='Классификация книг')
#фремы подфункций
issueF            = Frame(root)
getF              = Frame(root)
insertF           = Frame(root)
delF              = Frame(root)
catalogingF       = Frame(root)
classificationF   = Frame(root)
addreaderF        = Frame(root)
delreaderF        = Frame(root)
frames = (issueF,getF,addreaderF,delreaderF, insertF,delF, catalogingF, classificationF )
windows ={'добавить читателя':[addreaderF,0],'удалить читателя':[delreaderF,0], 'выдача_книг':[issueF,0],'прием_книг':[getF,0],'добавить_книгу':[insertF,0],"удаление_книг":[delF,0],"каталогизация":[catalogingF,0],"класссификация":[classificationF,0]}
print(windows)
issueB.grid(padx=20,ipady=5)
getB.grid(padx=20,ipady=5)
insertB.grid(padx=20,ipady=5)
delB.grid(padx=20,ipady=5)
cataloging.grid(padx=20,ipady=5)
classificationB.grid(padx=20,ipady=5)

master.grid()
accountingF.grid(padx=20,ipady=5)
getNdelF.grid(padx=20,ipady=5,row=2)
readerAdmin.grid(padx=20,ipady=5,row=1)
classifF.grid(padx=20,ipady=5,row=3)

#ViewBooks()
root.mainloop()
