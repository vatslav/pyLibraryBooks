﻿__author__ = 'Вячеслав'


#===Отлавливаем ошибку!
try:
    a=2/0
except ZeroDivisionError as zero:
    print(zero)


for row in cur.execute('select * from users where name="иван" '):
    print(row)

e1.delete(0, END)
e1.insert(0,'same text')
e1.grid_remove()


#cur.execute('update users set pass=? where name=?', (hsh.hexdigest(), 'иван')) #смена пароля
#conn.commit()



goodversion
cur.execute('update users set pass=? where name=?', (hsh.hexdigest(), 'иван')) #смена пароля
conn.commit()







def creatUsers():
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


def getTab(x=1,y=0):
    return tab.cells[x][y].value.get()
def setTab(x=1,y=0, val=None):
    global tab
    tab.cells[x][y].value.set(val)
def setTitile(val):
    global tab
    for i in range( len(val) ):

        tab.cells[0][i].value.set(val[i])

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







'''
if __name__ == '__main__':
    root = Tk()
    tab = Table(root)
    tab.pack()
    tab.cells[1][1].value.set('test')
    tab.cells[2][2].value.set( tab.cells[1][1].value.get() )

    root.mainloop()'''

'''
try:
    print(type(issueF))
    if issueF.winfo_viewable():
        print('+100')
        viewFrame(issueF)
        print('+100')
    return

except AttributeError:print('exc')
'''


#===НЕ МОГУ ПОЛУЧИТЬ ИМЕНА ВИДЖЕТОВ, т.е. тупo ISBN=>'ISBN, нужно наверно исподьзова base64 или еще что-то низкоуровневое
#req = 'INSERT INTO books ' + handlerBrackets( tuple2str(args) ) + 'values(?,?,?,?,?,?,?,?,?)'
#req = 'INSERT INTO books ' + str(args) + 'values(?,?,?,?,?,?,?,?,?)'


#print(req, args)
#print(req2, args)
#print(req==req2)  #'select * from users where name=?',('марк',


def cancelAct(*args):
    try:
        for x in args:
            x.grid_remove()
        return 1
    except UnboundLocalError:
        return 0
def viewFrame(name):
    global issueF,getF,insertF,delF, catalogingF, classificationF,flags
    if flags[name]==True:
        pass

#'PRAGMA table_info("books")'
fieldOfBooksRus = ('ISBN', 'ББК', 'Автор', 'Название', 'Год издания', 'Издательство', 'ключивые слова', 'город' )
fieldOfBooks = ('ISBN','bbk', 'autors', 'titile', 'years', 'publisher', 'keywords', 'city')
fieldOfBooksstr = 'ISBN,bbk,autors,titile,years,publisher,keywords,city




    def takeBooks(event=True, listcmd=[], configcmd=[],  listcontent=[], configfields=[]):
        if not listcontent:
            listcontent = (('Тестовая строка-%s' % x) for x in range(100) )

        root = Toplevel()
        centr,bottom,top,right = Frame(root), Frame(root), Frame(root), Frame(root) #frames
        #центральный лист
        toplist = ScrolledList(parent=centr,options=listcontent) #central LIST
        toplist.listbox.config(height=25,width=70,font=('courier'))
        sbx = Scrollbar( centr, orient=HORIZONTAL, command=userlist.listbox.xview)
        userlist.listbox.configure(xscrollcommand=sbx.set)
        sbx.pack(side=BOTTOM, fill=X)
        # поисковая полоска и кнопки ок отмена
        findtext = StringVar()
        fent = Entry(bottom, textvariable=findtext)
        fent.grid(row=0,column=0)
        Button(bottom,text='Ok', command=lambda:handeofind() ).grid(row=1)
        Button(bottom,text='Отмена', command=lambda:root.destroy()).grid(row=1,column=1)

        if not configfields:
            configfields=(x for x in [1,2,3,4])
        #[['Номер Абонемента', 'NomberAbonement', 1], ['ФИО', 'fio', 1], ['адрес', 'adress', 1], ['телефон', 'telephone', 0]]
            print(readermy)

        #радио и флажки
        chb = modernchekbutton(parent=top,title='отображать поля:',opt=configfields )
        rb = modernRadioBut(parent=right, titile='Сортировать и искать по:',opt=configfields,default=configfields[0][0] )
        


        #действия по нажатию кнопки
        if configcmd:
            for x in rb.scelet:
                x['command']=configcmd 
            chb.setAct(configcmd)
        if listcmd:
            userlist.setAct(listcmd)


        #взаиморасположение
        centr.grid(row=1,column=4)
        bottom.grid(row=2,column=4)
        top.grid(row=0,column=4)
        right.grid(row=1,column=5)
        getF.grid(column=4,row=0)

        root.mainloop()



        for x in range(len(books)):
            # количество экземпляров
            #SELECT count(e.classbook) FROM exemplars as e  WHERE e.classbook="5-9050"
            # количество книг по isbn
            count    = execsql('SELECT COUNT (classbook) FROM exemplars WHERE classbook=?', (isbns[x],))
            count    = list(count)[0][0]
            #id by isbn
            counttmp = execsql('SELECT (id) FROM books WHERE ISBN=?', (isbns[x],))
            counttmp = list(counttmp)[0][0]

            count2   = execsql('SELECT COUNT (idbook) FROM getting WHERE idbook =?', (counttmp,))
            count2   = list(count2)[0][0]
            realcountbook = int(count)-int(count2)
            #if realcountbook<1:
                #showerror()
            verifybooks.append(realcountbook)
            #row = str(books[x]) + ' всего экз.:('+str(count)+')'+ ' в наличии('+str(realcountbook)+')'
            selectbooks.listbox.insert('end',row)


            reg=r + ''' FROM books AS b  WHERE id 
            IN ( SELECT idbook FROM getting JOIN readers WHERE idreader 
            IN ( SELECT readers.id where readers.NomberAbonement=?)) ORDER BY low(%s) COLLATE sort''' % mtl.rb.report()