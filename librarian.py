#from main import e1

__author__ = 'Вячеслав'
from share_data import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from sys import exit as ext
import scrolledlist
import sqlite3
from hashlib import md5
import re
import random
import string
import time
from tkinter.filedialog   import asksaveasfilename
from tkinter.filedialog   import asksaveasfilename as openFile

b1  = '<Button-1>'
b1w = '<Double-1>'
b2  = '<Button-2>'
tab=''
specialty = ("Библиотекарь", "Читатель", "Администратор")
root1=True #кнопки
root=True #таблица
numberUser=0
NumberUserCur=0
'''
#сортировка строк, в sql запросе, без учете регистра
def sortTextInDb(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1==s2: return 0
    elif s1>s2: return  1
    else: return -1
def low(s):
    return s.lower()



try:
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    conn.create_collation('sort',sortTextInDb) #встраиваем сортировку
    conn.create_function("low", 1, low) #встраиваеваем функцию, 1 - кол-во аргмуентов
except sqlite3.OperationalError as dbLock:
    showerror('Ошибка', dbLock)
    exit()
'''
class ScrolledList(Frame):
    def __init__(self, options, parent=None,newBind=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                   # make me expandable
        self.makeWidgets(options)
        self.reBind = newBind

    def handleList(self, event):
        #if self.reBind == None:

        index = self.listbox.curselection()                # on list double-click
        label = self.listbox.get(index)                    # fetch selection text
        try:self.runCommand(label)                             # and call action here
        except:pass
        # or get(ACTIVE)
    def getCur(self):
        index = self.listbox.curselection()                # on list double-click
        try:
            label = self.listbox.get(index)
            return label
        except TclError:
            showerror('Ошибка',"Не выбран не один элемент из списка")
            return None

    def getCurNoHandle(self):
        index = self.listbox.curselection()                # on list double-click
        try:
            label = self.listbox.get(index)
            return label
        except TclError:
            return None



    def getIndexCur(self):
        index = self.listbox.curselection()
        return index[0]

    def setBind(self,object):
        self.listbox.bind('<Double-1>', object)

    def makeWidgets(self, options):
        sbar = Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)
        sbar.config(command=list.yview)                    # xlink sbar and list
        list.config(yscrollcommand=sbar.set)               # move one moves other
        sbar.pack(side=RIGHT, fill=Y)                      # pack first=clip last
        list.pack(side=LEFT, expand=YES, fill=BOTH)        # list clipped first
        pos = 0
        for label in options:                              # add to listbox
            list.insert(pos, label)                        # or insert(END,label)
            pos += 1                                       # or enumerate(options)
            #list.config(selectmode=SINGLE, setgrid=1)          # select,resize modes

        list.bind('<Double-1>', self.handleList,)           # set event handler

        self.listbox = list

    def runCommand(self, selection):                       # redefine me lower
        if self.reBind != None:
            self.reBind(selection)
        else:
            print( selection)

def execsql(req,values):
    if values ==None: request1 = req
    else: request1 = req + str(values) + '"'
    try:
        cur.execute(request1)
        for line in cur:
            yield line
            #userList.listbox.delete(userList.getIndexCur()) #удалить из списка
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        conn.commit()









def creatUserAct(e1,e2,e3,userBox):
    if e1.get()=='' or e2.get()=='' or e3.get()=='':
        showerror('Ошибка ввода', "Пожалуйста, заполните все поля ввода")
        return
    if len(e1.get())<4:
        showerror('Ошибка ввода', "Минимальная длина логина - 4 символов")
        return
    if len(e2.get())<6:
        showerror('Ошибка ввода', "Минимальная длина пароля - 6 символов")
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
    try:
        role = userBox.get( userBox.curselection() )
    except TclError as notSelect:
        showerror('Ошибка ввода', "Пожалуйста, выбирите тип учетной записи пользователя")
        return
    try:

        insUserValue = (name, hashpass, role )
        insUserComand = 'INSERT INTO users values (?,?,?,2)'
        cur.execute(insUserComand,insUserValue)
    except sqlite3.DatabaseError as err:
        errMsg = 'Ошиюбка выполнения запроса:\n"' + str(err) + '"'
        showerror('Ошибка', errMsg)
    else:
        conn.commit()
        root.destroy()#====== переставить строкой ниже, если научусь скрывать главное окно
        showinfo('Успех', "Новый пользователь создан")


def mkpass(size=10):
    chars = []
    chars.extend([i for i in string.ascii_letters])
    chars.extend([i for i in string.digits])
    chars.extend([i for i in '\'"!@#$%&*()-_=+[{}]~^,<.>;:/?'])

    passwd = ''

    for i in range(size):
        passwd += chars[random.randint(0,  len(chars) - 1)]
        random.seed = int(time.time())
        random.shuffle(chars)
    return passwd

def creatUser():
    def randPasAct():
        tmp = mkpass()
        e2.delete(0,last='end')
        e2.insert(0,tmp )
        e3.delete(0,last='end')
        e3.insert(0,tmp )
        e2.config(show='')
    def handlehideE2(event):
        e2.config(show='*')


    global tab,root1,root,specialty
    root = Toplevel()
    leftFrame  = Frame(root)
    rightFrame = Frame(root)
    button1 = Button(root,text='Подтвердить',command=(lambda: creatUserAct(e1,e2,e3,roleBox) ) )
    button2 = Button(root,text='Отмена' ,command=(lambda: root.destroy() ) )
    randPas = Button(root,text='Случайный пароль' ,command=(lambda: randPasAct() ) )
    Label(leftFrame, text="Логин").grid(row=0)
    Label(leftFrame, text="Пароль").grid(row=1)
    Label(leftFrame, text='Подтвердите пароль').grid(row=2)
    Label(rightFrame, text='Тип учетной записи').grid(column=3)
    e1 = Entry(leftFrame)
    e2 = Entry(leftFrame,show='*')
    e3 = Entry(leftFrame,show='*')

    roleBox = Listbox(rightFrame)
    [roleBox.insert('end',x) for x in specialty]
    roleBox.config(height=4,width=20)
    roleBox.grid(row=1,column=3)
    e1.grid(row=0, column=1,padx=5,pady=5,columnspan=2,ipadx=5)
    e2.grid(row=1, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    e3.grid(row=2, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
    randPas.grid(row=3, column=1,ipadx=5,rowspan=10)
    button1.grid(row=3, column=0,columnspan=1,ipadx=5,ipady=5,rowspan=10)
    button2.grid(row=3, column=2,columnspan=2,ipadx=5,ipady=5)
    leftFrame.grid(row=0, column=0)
    rightFrame.grid(row=0,column=4)
    e1.focus_set()
    e2.bind('<KeyPress>',handlehideE2)
    root.grab_set()
    root.wait_window()



def getUsers(mask): #фильтр на юзеров
    if mask:
        template = re.compile(mask)
    request = 'select * from users ORDER BY low(name) COLLATE sort' #выводим, с сортировкой без учета регистра по столбцу name
    try:
        for row in cur.execute(request):
            if not mask:
                yield (row[0],'||',row[2])
            else:
                pb = template.search(str(row[0]).lower())
                if pb:
                    yield (row[0],'||',row[2])
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        conn.commit()









def getSpeciality():
    global specialty
    for x in specialty:
        yield x

def delUser(userList): #удалить выбранного юзера
    indexUser = userList.getCur()
    request  = "delete from users where name=?" #====НЕ МОГУ ПОНЯТЬ ПОЧЕМУ не работает если знак вопроса, и потом замена
    #вероятно он заменяет ? на 1 символ
    request1 = 'delete from users where name="' + str(indexUser[0]) + '"'
    try:
        cur.execute(request1)
        userList.listbox.delete(userList.getIndexCur()) #удалить из списка
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        conn.commit()

def viewBooks(): #=============================================================== ==================== ======!!!!
    pass
    def getBooks():
        execsql('select * from books COLLATE sort')
    booksList = ScrolledList



def changeUser():#изменить юзеров 1 окно

    def changeOneuser(user): #интерфейс изменить пользователя
        if not user: #если не выбран не один юзер, была ошибка, ее перехватили и вернули None
            return
        def okAct(Event=None):
            ptr=0
            if e1.get()=="":
                showerror("Ошибка","Заполните имя учетной записи")
                return

            if roleList.getCurNoHandle()==None:
                showerror("Ошибка","Выбирите тип пользователя")
                return
            if len(e1.get())<4:
                showerror("Ошибка","Минимальная длина имени 4 символов")
                return

            request1 = 'update users set name=? where name=?'
            request2 = 'update users set role=? where name=?'
            try:
                cur.execute(request1,(e1.get(),user[0]) ) # можно было бы через один запрос " ; "
                cur.execute(request2,(roleList.getCurNoHandle(),e1.get()   ) ) #
                roleList.listbox.delete(roleList.getIndexCur()) #удалить из списка

            except sqlite3.OperationalError as dbLock:
                showerror('Ошибка', dbLock)
            else:
                conn.commit()

            root1.destroy()
            root.destroy()
            showinfo("Успех","Пользователь изменен")

        global tab,root1,root
        root1 = Toplevel()
        root1.title(string='Изменение учетеной записи Пользователя')
        leftFrame  = Frame(root1)
        rightFrame = Frame(root1)
        title = Label(leftFrame,text='Изменение учетеной записи Пользователя')
        Login = Label(leftFrame,text='Изменить, на логин:')
        roleL = Label(rightFrame,text='Новый тип пользователя')
        e1 = Entry(leftFrame)

        roleList = ScrolledList(getSpeciality(),parent=rightFrame)
        roleList.listbox.config(height=4,width=20)
        okB     = Button(root1,text='Ок',command=(lambda: okAct() ))
        cancelB = Button(root1,text='Отмена!!',command=(lambda: root1.destroy() ) )
        title.grid()
        Login.grid(row=1)
        roleL.grid()
        e1.grid(row=2,column=0)
        roleList.grid(row=1)
        ptr=0
        '''
        for spec in specialty:
            if spec==user[2]:
                roleList.listbox.activate(ptr)
                #print(ptr, spec,'===tada')
            ptr += 1
        '''

        #roleList.listbox.activate() ##===*-
        leftFrame.grid()
        rightFrame.grid(column=1,row=0)
        okB.grid(row=2)
        cancelB.grid(row=2,column=1)
        e1.insert(0,user[0])
        def handkerEnter(event):
            okAct()
        def handkerEscape(event):
            root1.destroy()
        root1.bind('<Return>',handkerEnter)
        root1.bind('<Escape>',handkerEscape)
        ptr = 0
        '''
        for spec in specialty:
            if spec==user[2]:
                roleList.listbox.activate(ptr)
                print(ptr, spec)
            ptr += 1
        '''
        roleList.config(height=4,width=5)
        e1.focus_set()
        root1.grab_set()
        root1.wait_window()


    def resetPasAct():
        request = 'update users set pass=? where name=?'
        tmp = mkpass()

        hsh = md5()
        hsh.update( tmp.encode('utf-8') )
        hashpass = hsh.hexdigest()
        tmpmsg = 'Пароль сброшен, на ' + tmp
        #
        try:
            cur.execute(request,(hashpass,userList.getCur()[0] ) ) #
            showinfo('Успех', tmpmsg)
        except sqlite3.OperationalError as dbLock:
            showerror('Ошибка', dbLock)
        except TypeError as te:
            pass
        else:
            conn.commit()





    global tab,root1,root
    root = Toplevel()
    root.title(string='Выбирети учетную запись для изменения')
    leftFrame  = Frame(root)
    rightFrame = Frame(root)
    options = getUsers(None)
    title = Label(root,text='Выбирети учетную запись для изменения')
    title.pack()
    userList = ScrolledList(options,parent=leftFrame,newBind=changeOneuser )
    #userList.setBind(changeOneuser())

    findE   = Entry(rightFrame, text='Найти')
    resetPas = Button(rightFrame, text='Сбросить пароль',command=(lambda:resetPasAct() ) )
    changeB = Button(rightFrame, text='Изменить',command=(lambda:changeOneuser(userList.getCur()) ) )
    delB    = Button(rightFrame, text='Удалить', command=(lambda:delUser(userList)       ) )
    changeB.pack()
    delB.pack()
    findE.pack()
    resetPas.pack()
    #options = ( ('Lumberjack-%s' % x) for  x in range(20))
    findE.delete(0,last='end')
    findE.insert(0,'Найти')
    #findE.bind('<KeyPress>',  test('as' ) )
    def handleFindPress(event):
        try:
            userList.listbox.delete(0,99999)
        except StopIteration:
            pass
        try:
            for x in getUsers(findE.get().lower() ):
                #print(x)#тут делать вставку в лист
                userList.listbox.insert('end',x)

        except StopIteration:
            pass

    #findE.bind('<KeyPress>',  handleFindPress )
    root.bind('<KeyPress>',  handleFindPress ) #==!!!===аргументы передаются в контексте,а мне нужно передать аргумент не
    #из контекста события (не то что вызвало событие, а то что находиться в соседнем виджите!), решение только так, как выше.???

    leftFrame.pack()
    rightFrame.pack()
    def handkerEnter(event):
        try:
            changeOneuser(userList.getCur())
        except TclError:
            pass
    def handkerEscape(event):
        root.destroy()
    root.bind('<Return>',handkerEnter)
    root.bind('<Escape>',handkerEscape)
    findE.focus_set()
    userList.listbox.config(height=15,width=30)
    root.grab_set()
    root.wait_window()
    #root.mainloop()

def exportDb():
    filename = asksaveasfilename()
    msg = "Не возможно сохранить файл, попробуйте выбрать другое местоположение"
    if not filename:
        showerror('Ошибка', msg)
        return
    try:
        file = open(filename,'w')
    except:
        showerror('Ошибка', msg)
        return
    for line in conn.iterdump():
        print(line)
    showinfo("Успех",'База данных успешно экспортировано')
    file.close()

def  importDb():
    filename = openFile()
    msg = "Не возможно сохранить файл, попробуйте выбрать другое местоположение"
    if not filename:
        showerror('Ошибка', msg)
        return
    try:
        file = open(filename,'r')
    except:
        showerror('Ошибка', msg)
        return
    req = ''
    for line in file.read():
        req += line
    try:
        cur.execute(req)
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        conn.commit()




def mymain():
    #print('mymain init)')
    global root1
    root1=Tk()

    root1.title(string='Администрирование БД Библиотека')
    viewAllBooks    = Button (text='посмотреть список книг')
    creatLibrarian  = Button (text='Создать учетную запись библиотекаря',   command=(lambda:creatUser() )  )
    changeLibrarian = Button (text='Изменить  учетную запись библиотекаря', command=(lambda:changeUser())  )
    viewLibrarian   = Button (text='Посмотреть статистику')
    exportdb        = Button (text='Экспорт базы данных в файл',            command=(lambda:exportDb()  )  )
    importdb        = Button (text='Импорт базы данных в файл',             command=(lambda:importDb()  )  )

    viewAllBooks.grid(padx=20,ipady=5)
    creatLibrarian.grid(columnspan=5,padx=20,ipady=5)
    changeLibrarian.grid(columnspan=5,padx=20,ipady=5)
    viewLibrarian.grid(ipady=2)
    exportdb.grid(columnspan=5,padx=20,ipady=5)
    #importdb.grid(columnspan=5,padx=20,ipady=5)

    root1.mainloop()


mymain()