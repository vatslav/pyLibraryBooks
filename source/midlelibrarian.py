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
import webbrowser

from tkinter.ttk import *

#поиск книг
flags ={'выдать_книги':False,'добавить_книгу':False}
fieldOfBooksRus = ('ISBN', 'ББК', 'Автор', 'Название', 'Год издания', 'Издательство', 'ключевые слова')
fieldOfBooks = ('ISBN','bbk', 'autors', 'title', 'years', 'publisher', 'keywords')
fieldOfBookD = {} #создадим словарь на оснве двух предыдущих картежей
if len(fieldOfBooks)!=len(fieldOfBooksRus):showerror('erroe','erroedict')
for x in range(len(fieldOfBooks)):
    fieldOfBookD[ fieldOfBooksRus[x] ] = fieldOfBooks[x]
#поиск читателя
rTableR = ('порядковый номер','Номер Абонемента', 'ФИО',"адрес","телефон","время создания") #имя для пользователя
rTableE = ('id',              'NomberAbonement' ,'fio', 'adress','telephone','create_time') #имя поля в бд
rTableS = [0,                   1,                  1,      1,      1,          0] #флаг, отвечающий за общедоступна ли это поле
rTableA = [0,1,1,1,0,0] #автивно ли это поле
rf = [(rTableR[x],rTableR[x]) for x in range( len(rTableE) - 1 )]
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
def sqlmy(mask=None,req=None,r=[],table='', sortby='',shadow='',j='',rq=False): #фильтр на книги
    global fieldOfBooks
    if mask:
        template = re.compile(mask)
    if req!=None:
        request=req
    else:
        if table=='' or sortby=='':
            showerror('Ошибка',"системная ошибка")
            #print(table, 'table')
            #print(sortby ,' sortby')
            return
        nfields = r
        nfieldstr = tuple2str(nfields)
        if shadow:
            nfieldstr = shadow + ',' + nfieldstr
        try:
            sortby = nfields[sortby]
        except ValueError: #на случай если sortby задан словом, не спасет от IndexError
            pass
        except TypeError: #на случай если sortby задан словом, не спасет от IndexError
            pass

        #select имена полей from имя_таблицы Order By low сортировать по полю
        request = 'select ' + nfieldstr + ' from ' + table + ' ORDER BY low(' +sortby+ ') COLLATE sort'
        request = request + ' ' + j

        try:
            index = nfields.index(sortby)
            if shadow:
                index += 1
        except ValueError as er:
            showerror('Ошибка',er)
            return
    if rq:yield request #просто вернуть запрос который получился в результате
    else:
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


def ViewBooks():#выдача книг читателю #!dslfxf rybu rybub
    global flags,issueF,fieldOfBooksRus,firstIn
    isbns = []
    issb  = []
    row   = []
    rissb = []
    struct = {} #,isbns=isbns,issb=issb,row=row,struct
    def handlerPress(event):
        global firstIn
        nonlocal isbns,issb,row,struct,rissb
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
        # НЕ ВЫПОДИТЬ ТЕ КНИГИ КОТОРЫЕ НЕ ПОЛНОСТЬЮ ЗАПОЛНЕНЫ====
        for x in range(len(storageisbn)):storageisbn.pop()
        print(222)
        #a     = [x for x range(len(isbns))]
        print(isbns,len(isbns))
        [isbns.pop() for x in range(len(isbns)) ]
        [issb.pop()  for x in range(len(issb))]
        [row.pop()   for x in range(len(row))]
        [rissb.pop() for x in range(len(rissb))]
        struct.clear()
        for x in getBooks(txt,index=rb.reportIndex(),sortby=fieldOfBooks[rb.reportIndex()],state=chekLayers.reportDict(),field=fieldOfBookD):
            isbn = x[0]
            #isbns.append(x[0])
            x=x[1:]
            # не выводим книгу, если она не полностью заполнена
            wiki = True
            #[y=1 for y in x]# чото не разработало!
            for field in x:
                if field=='':
                    wiki=False
                    break
            if not wiki:continue
            storageisbn.append(isbn)
            isbns.append(isbn)
           # continue
            row.append( tuple2str(x) )

        for x in range(len(row)):
            issb.append( int(countBooksByISBN(isbns[x]))  )
        for x in range(len(row)):
            j = int( countBooksBeByISBN(isbns[x]) )
            rissb.append(j-issb[x])
            row[x] += ' ' + str(j-issb[x]) + 'из' + str(j)
        for x in row:
            bookList.listbox.insert('end',x)
        struct = {isbns[x]:(rissb[x],issb[x]) for x in range(len(row)) }
        #for x in struct.items():
            #print()


            #print(x,type(x),type(x[0]),type(x[4]))

    def nameOfrb():
        for x in fieldOfBooksRus:
            yield x
#==== begin       выдачакниг непосредственно          ================================
    gna = [] #recursiv acronim from GNA is Nomber of Abonement
    def iss(isbns,books):
        def inserbd():
            if len(books)>5: #дописать - чтобы сумма от желаемых и текущех была
                showerror('Ошибка','Одному читателю нелья выдать более 5 книг за раз')
                return
            for isbn in isbns:
                if struct[isbn][0]<1:
                    showerror('Ошибка',"Одной из книг нет в наличии")
                    return
            na = gna[int(userlist.getIndexCur())] # NomberAbonement текущего выбраного
            if int(countBooksByNA(na))>5:
                showerror("Ошибка","У читателя уже более 5 книг")
                return
            if int(countBooksByNA(na))+len(isbns)>5:
                print('kоличество книг взятых читателем ', countBooksByNA(na))
                showerror("Ошибка","Суммарное количество книг взятых читателем и отобранных для выдачи превышает 5 штук")
                return

            try:
                deltat = int(timeget.get())
                if deltat<1:
                    showerror('Ошибка','количество дней должно быть больше 0')
                    return
                if deltat>100:
                    if askyesno('Внимание','Вы уверено что хотите выдать книгу на больше чем на 3 месяца?'):
                        pass
                    else:return
            except ValueError:
                showerror('Ошибка','Неверно задано количество дней')
                return
            if not userlist.getCur():return #проверить возвращает ли 0, при не выделенном
            for number in verifybooks:
                if number<1:
                    showerror('Ошибка','Одной из книг нет в наличии')
                    return
            request = '''INSERT INTO getting (active,datestart,dateend,idbook,idreader) VALUES (?,?,?,?,?)'''

            idcurreader=[] #ID текущего ридера

            idbooks=[] # ID книг
            for x in execsql('SELECT id FROM readers WHERE NomberAbonement="%s"' % na):
                idcurreader.append(x)
            for isbn in isbns:
                for row in execsql('SELECT id FROM books WHERE ISBN=?',(isbn,)):
                    idbooks.append(row)

            try:idcurreader = [x[0] for x in idcurreader][0] # делаем из списка картежей список чисел (строк)
            except IndexError:
                print('idcurreader =', idcurreader)
                print(na)
                showerror('Ошибка',"Произошла непредвиденная ошибка")
                return
            print('IDBOOKS=',idbooks)
            print('idcurreader=',idcurreader)
            idbooks = [x[0] for x in idbooks]
            idbooks[0] = int(idbooks[0]) #-1   #=====УМА НЕПРЕЛОЖУ КАК ВЫХОДИТ, ТАК ЧТО id, на 1 больше!????!!!!!======
            print('IDBOOKS=',idbooks)
            #узнать id текущего ридера и ид всех книг - список
            #print('na,userlist.getIndexCur(),gna = %s, %s - %s' % (na,userlist.getIndexCur(),gna))
            td = datetime.date.today()
            tr = datetime.date.fromordinal(td.toordinal()+deltat )
            print(request,(True,td,tr,idbooks,idcurreader) )
            trast = True
            for idbook in idbooks:
                if not inscsql(request,(True,td,tr,idbook,idcurreader)):
                    return
            showinfo('Успех','Книги добавлены')
            handlerPress(1)
            tf.destroy()
            #handlecancel() ##!==

            #print('SELECT id FROM readers WHERE NomberAbonement='+na)
            #aa=2
        ptr = 0
            #inscsql(request,())
        def handleDCUL(any,ptr=ptr):
            #@ind = userlist.getIndexCur()
            if userlist.getIndexCur()==-1:
                numberbooks.set('не определено %s' % ptr)
                ptr += 1
                return
            ind = gna[int(userlist.getIndexCur() )]
            ex = execsql('SELECT COUNT(active) FROM getting JOIN readers WHERE idreader IN ( SELECT readers.id where readers.NomberAbonement="%s")' % ind)
                          #SELECT COUNT(g.idre) FROM getting as g WHERE idreader IN (SELECT r.id FROM readers AS r WHERE NomberAbonement='m-9')
            print('gna=%s' % gna)
            print('index = %s' % str(userlist.getIndexCur() ) )
            #userlist.getCur()
            numberbooks.set(list(ex)[0][0] ) #NA cur user
            for x in ex:
                print(x,'ex==')




        def handlecancel():
            root.bind('<KeyPress>',no)
            tf.destroy()
        tf = Toplevel(getF)
        tf.title(string='Выдача книг читателю - СУБД Библиотека')
        # поиск для верхнего листа - юзеры
        def handeofind(event=True):
            curelem = rb.reportIndex()
            chb.setFlagByIndex(curelem)
            txt = findtext.get()
            userlist.clearlist()
            rows = [] #строки которые потом будут добавлены
            auxcount = [] # то что допишем в конец строки
            # в gna - NA, rows - content строк
            for x in sqlmy(mask=txt,r=chb.getSetup(),table='readers',sortby=rTableE[1:5][curelem],shadow='NomberAbonement'):
                y = tuple2str(x[1:]) #сама строка
                gna.append(x[0]) #скрытый id
                rows.append(y)
            # для каждого НА в гна получить количество книг, на этот НА
            for x in gna:
                msg = '''SELECT COUNT(active) FROM getting JOIN readers WHERE active=1 AND idreader IN
                ( SELECT readers.id where readers.NomberAbonement="%s")''' % x
                auxcount.append(str(list(execsql( msg) )[0][0] ) )
            #
            for x in range(len(rows)):
                userlist.listbox.insert('end',rows[x] + ' ~Книг на_руках:' + auxcount[x])

        centr,bottom,top,right = Frame(tf), Frame(tf), Frame(tf), Frame(tf)
        #sdfsdf
        userlist = ScrolledList(parent=centr)
        userlist.listbox.config(height=25,width=120)
        def handleDCinuserlist():
            try:

                ind = userlist.getIndexCur()
            except IndexError:
                return
            userlist.listbox.delete(ind)

        userlist.setActOneClick(handleDCUL)
        userlist.setAct(handleDCUL)
        findtext = StringVar()
        timeget  = StringVar()
        fent = Entry(bottom, textvariable=findtext)
        fent.grid(row=1,column=0)
        Label(bottom, text='Поиск читателя').grid(row=0,column=0)
        Label(bottom, text='Кол-во дней, на которые выдается книга').grid(row=0,column=1)
        ee = Entry(bottom,textvariable=timeget)
        ee.grid(row=1,column=1)
        timeget.set('31')#


        Button(bottom,text='Ok!', command=lambda:inserbd() ).grid(row=3)


        Button(bottom,text='Отмена', command=lambda:handlecancel()).grid(row=3,column=1)
        Button(bottom,text='Поиск', command=lambda:handeofind()).grid(row=3,column=2)
        subbotton = Frame(bottom)
        subbotton.grid(row=0,column=0,padx=25,pady=25)
        #Entry(bottom, textvariable=number).grid(row=1)
        options = (x[0] for x in readermy)

        #optchb = ( (x[0],x[1]) for x in readermy)

        chb = modernchekbutton(parent=top,title='отображать поля:',opt=( (x[0],x[1]) for x in readermy))
        handle = lambda:handeofind(event='servseach')
        chb.setComand(handle)
        rb = RadioBut(parent=right, titile='Сортировать и искать по:',opt=(x[0] for x in readermy),default=list((x[0] for x in readermy))[0])
        chb.setFlagByIndex(0)
        chb.setFlagByIndex(1)
        subright = Frame(right)
        subright.pack()
        Label(subright,text="Количество книг у данного пользователя").grid(row=0,column=0)
        numberbooks = StringVar()
        Label(subright,textvariable=numberbooks).grid(row=1,column=0)
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
        def handlerDC_selbooks(event=1):
            i = int ( selectbooks.getIndexCur() )
            print('i=',i)
            selectbooks.listbox.delete( i)
        selectbooks.listbox.config(height=len(isbns),width=maxlenttitile)
        selectbooks.clearlist()
        selectbooks.setAct(handlerDC_selbooks)
        selectbooks.listbox.bind('<Double-1>', handlerDC_selbooks)
        #print('isbns %s' % isbns)
        # нижний лист - книги
        verifybooks = []
        for x in range(len(books)):

            selectbooks.listbox.insert('end',books[x])

        def handleDCinuserlist(td):
            try:
                ind = int(selectbooks.getIndexCur())

                verifybooks.pop(ind)
                #isbns=list(isbns)
                isbns.pop(ind)
                #books=list(books)
                books.pop(ind)
            except IndexError:
                return

            selectbooks.listbox.delete(ind)
        selectbooks.setAct(handleDCinuserlist)
        # handlecancel handleDCinuserlist
    #userlist.setAct(handlecancel)



        #for number in verifybooks:
        #    if number<1:
        #        show
        #root.focus()
        #handlecancel = lambda Event:tf.destroy()
        root.bind('<KeyPress>',handeofind)
        root.bind('<Return>',  handeofind)
        root.bind('<Escape>',handlecancel)




        fent.focus_set()
        #getF.grab_set()
        #getF.wait_window()



    #===================    end==========
    def delread():
        pass
    hideFrames();
    if flags['выдать_книги']==True:
        issueF.grid()
        #bookList.clearlist()
        try:handlerPress(99)
        except NameError:pass
        return
    flags['выдать_книги'] = True
    issueF = Frame(root)
    midlle, bottom, right = Frame(issueF), Frame(issueF), Frame(issueF)
    def handlOk(func,Event=True,):
        index, books = bookList.getCurMulti()
        if not len(index):
            showerror('Ошибка',"Не выбрана не одна книга")
            return #iss([0],[0]) #можно была бы вызывать окно
        tmp = []  #текущие выбранные тут тепер хранитяться, после ок
        for x in index:
            tmp.append(storageisbn[x]) #-1выведена эмпирически
        books = list(books)
        #print('tmp=isbns %s tmp')
        try:func(tmp,books) #отправляеем индексы и названия
        except TypeError:iss(tmp,books)

    Button(bottom, text='Ок',command=lambda:handlOk(iss) ).grid(row=1)
    Button(bottom, text='Отмена',command=lambda:issueF.grid_remove()).grid(row=1,column=1)

    midlle.grid(column=4,row=0)
    submidle1, submidle2 = Frame(midlle),Frame(midlle)
    submidle1.grid(row=0)
    submidle2.grid(row=1)
    bottom.grid(column=4,row=1)
    right.grid(column=5,row=0)

    storageisbn = []

    rb = RadioBut(parent=right,opt=nameOfrb(),titile='Сортировать и искать по:',default=fieldOfBooksRus[3])
    Label(right,text='Количество экземпляров: ').pack()
    Label(right,text='   20').pack()

    text =StringVar()
    find = Entry(bottom,textvariable=text)

    chekLayers = chekbutton(parent=submidle1,title='Отображаемые поля:',opt=nameOfrb())
    def hand():handlerPress('служебный поиск')
    chekLayers.setComand(hand)
    titname = []
    titname = list(fieldOfBooksRus[2:4])
    titname.append(fieldOfBooksRus[6])
    for name in titname:
        chekLayers.setFlag(name)
    bookList = ScrolledList(parent=submidle2,options=getBooks( ) )
    #sbx = Scrollbar( submidle2, orient=HORIZONTAL, command=bookList.listbox.xview)
    #bookList.listbox.configure(xscrollcommand=sbx.set)
    #sbx.pack(side=BOTTOM, fill=X)
    #sbx.grid()
    sbx = Scrollbar( submidle1, orient=HORIZONTAL, command=bookList.listbox.xview)
    bookList.listbox.configure(xscrollcommand=sbx.set)
    #sbx.pack(side=BOTTOM, fill=X)
    handlerPress('чижика собаку, кошку забичку!')#убираем фигурные скобки и деактивизируем первыйfirstIn

    bookList.listbox.config(height=25,width=65,font=('courier'),selectmode=MULTIPLE)#EXTENDED    MULTIPLE SINGLE
    bookList.setAct(handlOk)

    #bookList.listbox.bind('<Double-1>', bookList.listbox.ff)
    bookList.grid(column=0,row=0)
    find.grid(column=0,row=0,padx=20,ipady=5)
    Button(bottom,text='Найти1',command=lambda:handlerPress(1)).grid(column=1,row=0)
    Button(bottom,text='Найти выбранные книги на Ozon.ru',command=lambda:ozon()).grid(column=2,row=0)
    ms = 'http://www.google.ru/search?hl=ru&tbo=p&tbm=bks&q=isbn:'
    Button(bottom,text='Найти выбранные книги на Google.com',command=lambda:ozon(msg=ms)).grid(column=2,row=1)
    def ozon(msg="http://www.ozon.ru/?context=search&text="):
        i,s = bookList.getCurMulti()
        t = [storageisbn[x] for x in i]
        if len(t)>5:
            if askyesnocancel('Внимание',"Каждая книга откроется в новой вкладке, хотите открыть %s вкладок" % len(t)):
                pass
            else:return
        for x in t:
            webbrowser.open(msg+x)
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
            #showerror('Ошибка',"Пожалуйста, заполните все поля ввода данных")
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

def viewreader(serv=True,newcomand=[]):#!dslfxf
    #имя для пользователя /\ в бд, для всех, поумолчанию тру?
    if serv:
        hideFrames()
        if windows['прием_книг'][1]:
            windows['прием_книг'][0].grid()
            #userlist.clearlist()
            #handeofind()
            handlecancel = lambda event:getF.grid_remove()

            #root.bind('<KeyPress>',handeofind)
            #root.bind('<Return>',  handeofind)
            #root.bind('<Escape>',handlecancel)
            return
        windows['прием_книг'][1] = True


    gna = []#номер абонемента
    auxcount = [] # то что допишем в конец строки
    def handeofind(event=True):
        #curelem = rb.reportIndex()
        #chb.setFlagByIndex(curelem)
        #txt = findtext.get()
        #userlist.clearlist()#важно сортировать по динамическому элементу
        #for x in sqlmy(mask=txt,r=chb.getSetup(),table='readers',sortby=rTableE[1:5][curelem]):
        #    x = tuple2str(x)
        #    userlist.listbox.insert('end',x)

        curelem = rb.reportIndex()
        chb.setFlagByIndex(curelem)
        txt = findtext.get()
        userlist.clearlist()

        rows = [] #строки которые потом будут добавлены

        # в gna - NA, rows - content строк
        for x in sqlmy(mask=txt,r=chb.getSetup(),table='readers',sortby=rTableE[1:5][curelem],shadow='NomberAbonement'):
            y = tuple2str(x[1:]) #сама строка
            gna.append(x[0]) #скрытый id
            rows.append(y)
        # для каждого НА в гна получить количество книг, на этот НА
        for x in gna:
            msg = '''SELECT COUNT(active) FROM getting JOIN readers WHERE active=1 AND idreader IN
            ( SELECT readers.id where readers.NomberAbonement="%s")''' % x
            auxcount.append(str(list(execsql( msg) )[0][0] ) )
        #
        for x in range(len(rows)):
            userlist.listbox.insert('end',rows[x] + ' ~Книг на руках:' + auxcount[x])



    centr,bottom,top,right = Frame(getF), Frame(getF), Frame(getF), Frame(getF)
    #userGen = (x for x in sqlmy(mask=txt,r=readermy,table='readers',sortby=r////b.reportIndex()))
    userlist = ScrolledList(parent=centr)
    userlist.listbox.config(height=25,width=70,font=('courier'))
    #' ORDER BY low(' +sortby+ ') COLLATE sort'
    reg1=''' FROM books AS b WHERE id
    IN ( SELECT idbook FROM getting JOIN readers WHERE idreader
    IN ( SELECT readers.id where readers.NomberAbonement=?))'''

    #def find():


    cf = [(fieldOfBooksRus[x],fieldOfBooks[x]) for x in range(len(fieldOfBooks))]

    #
    def viewTopBooks (event):


        reg='''SELECT b.title, b.autors,b.years,b.keywords FROM books AS b  WHERE id
        IN ( SELECT idbook FROM getting JOIN readers WHERE idreader
        IN ( SELECT readers.id where readers.NomberAbonement=?)) ORDER BY low('title') COLLATE sort''' #% rb.report()
        if not int(auxcount[int(userlist.getIndexCur() )]):
            showerror("Ошибка",'У этого пользователя нет книг')
            return
        ind = gna[int(userlist.getIndexCur() )]

        bookrows = execsql(reg, (ind,) )
        #поиск
        idbooksFr= []
        def handlefind(event=True):
            mtl.toplist.clearlist()
            mtl.chb.setFlagByIndex(mtl.rb.reportIndex())
            r = 'SELECT b.id, ' # готовим запрос (учет текущих флагов)
            for x in mtl.chb.getSetup():
                r = r + ' b.%s,' % x
            r = r[:-1] # del запятая
            # old - оператор IN не возвращает только уникальные элементы, повторки нет
            reg=r + ''' FROM books AS b  WHERE id
            IN ( SELECT idbook FROM getting JOIN readers WHERE idreader
            IN ( SELECT readers.id where readers.NomberAbonement=?)) ORDER BY low(%s) COLLATE sort''' % mtl.rb.report()
            # запрос, новый, когда id отдельно
            r2 = r + ' FROM books AS b  WHERE id="%s"'
            idbooks = '''SELECT idbook FROM getting JOIN readers WHERE active=1 AND idreader
            IN ( SELECT readers.id where readers.NomberAbonement=?) '''

            idbooks = list(execsql(idbooks,(ind,)))
            idbooks = [x[0] for x in idbooks]
            print('___r2__==%s' %r2)
            [idbooksFr.pop() for x in range(len(idbooksFr))]
            print(r2,idbooks)
            for y in idbooks:
                bookrows = execsql(r2 % y )
                for x in bookrows:
                    idbooksFr.append(x[0])
                    x = tuple2str(x[1:])
                    mtl.toplist.listbox.insert('end',x)


        def h_dc_bl(event=True):
            i = int(mtl.toplist.getIndexCur())
            mtl.toplist.listbox.delete( i )
            idbooksFr.pop(i)
        def h_ungetting(event=True):
            #for x in range(20):
            #    msg = mtl.toplist.listbox.get(x)
            #    if msg =='':break
            #    print(msg,len(msg))

            #for x in mtl.toplist.getContent():
                #print(x,len(x))

            print('idbooksFr =%s' % idbooksFr )
            print('ind=%s' % ind)
            #req = 'DELETE FROM getting WHERE idbook=? AND idreader IN (SELECT id from readers WHERE NomberAbonement=?)'
            req = 'UPDATE getting set active=0 where idbook=? AND idreader IN (SELECT id from readers WHERE NomberAbonement=?)'
            s=1
            for id in idbooksFr:

                s = inscsql(req,(id,ind))
                if not s:
                    showerror('Ошибка','Произошла непредвиденная ошибка, причины неизвестны')

            if s:showinfo('Успех',"Книги возвращены")
            handeofind()

            #handeofind

            mtl.root.destroy()

        def delbooks():
            print('idbook ',idbooksFr)
            print('ind ',ind)

        print('cf = %s' % cf)
        mtl = MyTopLevel(configfields=cf, configcmd=handlefind,listcmd=h_dc_bl,okcmd=h_ungetting)
        #delbooks()

        mtl.rb.setAct(handlefind)
        mtl.chb.setFlagByIndex(2)
        mtl.chb.setFlagByIndex(3)
        mtl.chb.setFlagByIndex(6)
        mtl.root.title(string='Возврат книг - СУБД Библиотека')
        mtl.fent.grid_remove()
        #mtl.toplist


        handlefind()
        n = len(idbooksFr)
        if n<9:
            n=10
        mtl.toplist.listbox.config(height=n,width=70,font=('courier'))


        #mtl.start()


    def delread():
        i = int(userlist.getIndexCur())
        if i==-1:return
        na = gna[i]
        if countBooksByNA(na)>0:
            showerror('Ошибка',"Нельзя удалить читателя, который вернул не все книги")
            return
        print(na,len(na),userlist.getIndexCur())
        msg = "Вы уверены что хотите удалить пользователя за номером %s" %na
        if askyesnocancel("Предупреждение",msg):
            if inscsql('DELETE FROM readers where NomberAbonement="%s"' %na ):
                showinfo("Успешное выполнение операции",'Читатель за номером %s удален' % na)
                userlist.clearlist()
                handeofind()
            else:showerror("Ошибка","Читатель не удален")
        else:pass
    userlist.setAct(viewTopBooks )
    #useVTB = lambda:viewTopBooks()
    sbx = Scrollbar( centr, orient=HORIZONTAL, command=userlist.listbox.xview)
    userlist.listbox.configure(xscrollcommand=sbx.set)
    sbx.pack(side=BOTTOM, fill=X)
    #number = StringVar() #поле ввода имени
    findtext = StringVar()
    fent = Entry(bottom, textvariable=findtext)
    fent.grid(row=0,column=0)
    Button(bottom,text='Найти', command=lambda:handeofind() ).grid(row=0,column=1)
    Button(bottom, text='Удалить читателя',command=lambda:delread()  ).grid(row=0,column=2,columnspan=2)
    b = Button(bottom,text='Ok', command=lambda:viewTopBooks(1) )
    b.grid(row=1,ipadx=45,padx=10)
    if newcomand!=[]:
        b['command']=lambda:newcomand()
    Button(bottom,text='Отмена', command=lambda:getF.grid_remove()).grid(row=1,column=1)
    #Entry(bottom, textvariable=number).grid(row=1)

    chb = modernchekbutton(parent=top,title='отображать поля:',opt=( (x[0],x[1]) for x in readermy) )
    rb = RadioBut(parent=right, titile='Сортировать и искать по:',opt=(x[0] for x in readermy),default=list((x[0] for x in readermy))[0])
    # при кажом щелчке по радио кнопке перепоиск
    for x in rb.scelet:
        x['command']=handeofind
    chb.setAct(handeofind)

    chb.setFlagByIndex(0)
    chb.setFlagByIndex(1)
    hand = lambda Event:handeofind


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
        if ISBN.get()=='':
            showerror('Ошибка',"Поле  ISBN должно быть заполнено обезательно!")
            return
        #args = (random.randint(0,9999),20,3,4,5,6,7,8,ts)
        if not testCompair(args):
            if askyesnocancel('Внимание',"Книга будет недоступна для выдачи так как:\nНе все поля заполнены, "
                                         "вы можете заполнить их позже, продолжить?"):
                pass
            else:
                return

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
        if inscsql(request,args):
            showinfo('Успех',"Книга добавлена")
        else:
            return
        ts = datetime.datetime.today()
        #у меня не вышло два следующих запроса объединить в один, лист используется для преообразования генератора
        #получается список в котором кортеж в котором число, поэтому так:


        #tmp = list(execsql('SELECT (id) FROM books WHERE ISBN=?',(ISBN.get(),) ) )[0][0]
        tmp = ISBN.get()
        for x in range(ptr):
            if not inscsql('INSERT INTO exemplars (classbook,create_time) VALUES (?,?) ',(tmp,ts) ):
                return #None вернется когда в inscql возникнет ошибка, и потоу здесь только return

        if ptr > 0:
            msg = "Экземпляров добавлено: " + str(ptr)
            showinfo('Успех', msg)
        [x.delete(0,last='end') for x in (ISBN,bbk,author,title,years,publisher,keywords,sity)]
        spinval.set('1')

            #print(list(inscsql))
        #s=sqlmy('SELECT * FROM EXEMPLARS')
        #s = cur.execute('SELECT * FROM EXEMPLARS')
        #for x in s:
        #    print(x)
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
        if inscsql('INSERT INTO readers (NomberAbonement ,fio, adress,telephone,create_time) values(?,?,?,?,?)',val):
            showinfo('Успех',"Читатель успешно добвален")
            [field.set('') for field in txt]




def delexempl(): #rf! удаление экземпляров книги
    if windows['удаление_книг'][1]==1:
        hideFrames()
        delF.grid()
        windows['удаление_книг'][0].cmd_()
        #find()
        return
    windows['удаление_книг'][1]=1

    cf = [(fieldOfBooksRus[x],fieldOfBooks[x]) for x in range(len(fieldOfBooks))]
    hideFrames()
    isbns = []
    def find():
        xw.toplist.clearlist()
        txt  = xw.findtext.get()
        [isbns.pop() for x in range(len(isbns))]
        row  = []
        issb = []
        #print('ISBNS=!!===++++', list(isbns))
        for x in getBooks(txt,index=xw.rb.reportIndex(),sortby=fieldOfBooks[xw.rb.reportIndex()],
            state=xw.chb.reportDict(),field=fieldOfBookD):
            isbns.append(x[0])
            row.append( tuple2str(x[1:]) )

        for x in range(len(row)):
            issb.append( int(countBooksByISBN(isbns[x]))  )
        for x in range(len(row)):
            j = int( countBooksBeByISBN(isbns[x]) )
            row[x] += ' ' + str(j-issb[x]) + 'из' + str(j)



            #x += ' выдано:'+str(countBooksByISBN(y))
        #print(2)
        for x in row:
            xw.toplist.listbox.insert('end',x)
    def tl(event):
        def delb():

            try:x = int(count.get())
            except ValueError:
                showerror('Ошибка',"Введите целое число")
                return
            flag = True
            ptr = 0
            ids = list(execsql('SELECT id from exemplars  where classbook="%s"' % isbns[i]))
            ids = [x[0] for x in ids]
            if len(ids)<x:
                showerror('Ошибка',"""Вы хотите удалить экземпляров: %s - это больше
                    чем есть в наличии: %s """ % ( x, len(ids) ) )
                return
            numberissb = list( execsql('''SELECT COUNT(g.active) FROM getting as g WHERE
                g.idbook IN (SELECT id FROM books where ISBN="%s")''' % isbns[i]))
            numberissb = tuple2str( numberissb[0] )
            print('numberissb=%s' % numberissb)
            if int(numberissb)>0:
                showerror('Ошибка',"Одик из экземпляров это книги выдан пользователю,\nудаление невозможно")
                return
            ids = ids[0:x] #сколько будем выдавать
            for id in ids:
                ptr += 1
                if not inscsql('DELETE from exemplars where classbook="%s" and id="%s"' % (isbns[i],id)):
                    flag = False
            if flag:showinfo("Успех","Экземпляров удалено: %s" % x)
            else:showerror('Ошибка',"В процессе удаления произошла ошибка")
            r.destroy()
        i = int(xw.toplist.getIndexCur())
        if i == -1:
            return
        r = Toplevel()
        l, centr = Frame(r), Frame(r)
        l.grid(row=0,column=0)
        centr.grid(row=1,column=0)
        r.title(string='Удаление экземпляров книги_')
        lb = Listbox(l)
        lb.config(height=2,width=5+len(xw.toplist.getCur()),font=('courier'))
        lb.grid(row=0,column=0,columnspan=2)

        lb.insert('end',xw.toplist.getCur())
        count = IntVar()
        Label(centr,text='Количество экземпляров к удалению:').grid(row=1,column=0)
        s = Spinbox(centr, from_=1.0, to=100.0, textvariable=count)
        s.grid(row=2,column=0)
        Button(centr,text='Удалить',command=lambda:delb()).grid(row=2,column=1)
        Button(r,text='Отмена',command=lambda:r.destroy()).grid(row=3,column=0)
        #r.focus_set()

        #r.grab_set()
        #r.wait_window()
        r.focus_set()          # take over input focus,
        #r.grab_set()           # disable other windows while I'm open,
        r.wait_window()
        #r.mainloop()
    def cataloging():
        i = int ( xw.toplist.getIndexCur() )
        if i==-1:
            showerror('Ошибка',"Не выбрана не одна книга")
            return
        print(i,type(i),isbns[i])
        data = execsql('''SELECT ISBN, bbk, autors, title, years, publisher, keywords
            from books WHERE ISBN="%s" ''' % isbns[i])
        data=list(data)[0]
        isbn = data[0]

        r = Toplevel()
        centr, bottom, subcentr = Frame(r) , Frame(r),Frame(r)
        form = inform(centr, fieldOfBooksRus)
        form.setContent(data)
        Label(subcentr,text='Кол-во экземпляров ').grid(row=0,column=0)
        count = IntVar()
        Spinbox(subcentr,from_=1.0, to=1000.0, textvariable=count).grid(row=0,column=1)
        Button(bottom,text='Изменить',command=lambda:update()).grid(row=0,column=0)
        Button(bottom,text='Отмена',command=lambda:r.destroy()).grid(row=0, column=1)

        def update():
            print(form.getStr())
            req = inscsql('''UPDATE books set ISBN=?, bbk=?, autors=?, title=?, years=?,
                publisher=?, keywords=? where ISBN="%s"''' % isbn, form.getStr())
            if req:
                showinfo("Успех",'Запись успешно изменина')
                r.destroy()
            else:
                showerror('Ошибка',"Произошла непредвиденная ошибка")
        def handlerisbn(event=1):
            form.setContentByIndex(0,isbn)

        r.bind('<KeyPress>',handlerisbn)
        centr.grid()
        subcentr.grid(row=2)
        bottom.grid(row=3)

    xw = MyTopLevel(parent=delF,configfields=cf,configcmd=find,listcmd=tl)
    xw.rb.var.set('title')
    xw.chb.setFlagByIndex(3)
    xw.chb.setFlagByIndex(2)
    xw.chb.setFlagByIndex(0,value=False)
    xw.root.grid(column=4,row=0)
    xw.cat = Button(xw.bottom,text='Класификация книги',command=lambda:cataloging())
    xw.cat.grid(column=3,row=1)
    xw.cmd_ = find
    #xw.root.title(string='Удаление экземпляров книг')
    find()
    delF.grid(row=0,column=2)
    windows['удаление_книг'][0]=xw

def classif():
    pass


iterColumnBooks()
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


issueB            = Button (accountingF,text='Выдача книг чиателю / поиск книги в Интернет', command=lambda: ViewBooks() );
getB              = Button (accountingF,text='Прием книг у читателя / удаление читателя   ',command=lambda:viewreader() )
insertB           = Button (getNdelF,   text='      Добавление книг в фонд библиотеки     ',command=lambda:addBook() )
delB              = Button (getNdelF,   text='        Класификация/Удаление книг          ',command=lambda:delexempl() )

addReader         = Button (readerAdmin,text='Добавление читателя',command=lambda:addreader()).grid(padx=20,ipady=5)
delReader         = Button (readerAdmin,text='Удаление читателя',command=lambda:viewreader()).grid(padx=20,ipady=5)

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
#cataloging.grid(padx=20,ipady=5)
#classificationB.grid(padx=20,ipady=5)

master.grid()
accountingF.grid(padx=20,ipady=5)
getNdelF.grid(padx=20,ipady=5,row=2)
readerAdmin.grid(padx=20,ipady=5,row=1)
classifF.grid(padx=20,ipady=5,row=3)

#ViewBooks()
root.mainloop()
