#from main import e1

__author__ = 'Вячеслав'
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from sys import exit as ext
import scrolledlist
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

class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                   # make me expandable
        self.makeWidgets(options)

    def handleList(self, event):
        index = self.listbox.curselection()                # on list double-click
        print(index)
        label = self.listbox.get(index)                    # fetch selection text
        self.runCommand(label)                             # and call action here
        # or get(ACTIVE)
    def getCur(self):
        index = self.listbox.curselection()                # on list double-click
        #print(index)
        label = self.listbox.get(index)
        return label

    def getIndexCur(self):
        index = self.listbox.curselection()
        #print('===',index, type(index), index[0],type(index[0]))
        return index[0]

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
        list.bind('<Double-1>', self.handleList)           # set event handler
        self.listbox = list

    def runCommand(self, selection):                       # redefine me lower
        print( selection)







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
    try:
        role = userBox.get( userBox.curselection() )
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

    global tab,root1,root,specialty
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

    roleBox = Listbox(rightFrame)
    [roleBox.insert('end',x) for x in specialty]
    roleBox.grid(row=1,column=3)
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

def pbTruly(mask,expression):
    template = re.compile(mask)
    return template.search(expression), template.search(expression).group(), template.search(expression).span()





def getUsers(mask,once=False): #фильтр на юзеров
    global numberUser
    #print(mask, mask==None)
    if mask == None:
        request = 'select * from users'
        aux=[]
        try:
            for row in cur.execute(request):
                #print(mask, mask==None)
                if not once:
                    numberUser += 1
                    yield (row[0],'||',row[2])
                else:
                    aux.append((row[0],'||',row[2]))



        except sqlite3.OperationalError as dbLock:
            showerror('Ошибка', dbLock)
        else:
            conn.commit()

def reDrawUser(mask,userList):
    print('reDrowStart')

    #print(str(mask), mask==None,'1str in test')
    request = 'select * from users'
    template = re.compile(mask)
    #print(mask, '---mask')
    #print(mask==None,'mask==none')

    try:
        userList.listbox.delete(0,last=9999)
    except:
        pass
    i=0
    try:
        for row in cur.execute(request):
            #print('use cycle!', i)
            i += 1
            pb = template.search(str(row[0]))
            if pb:
                print(row, type(row))
                yield (row[0],'||',row[2])
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:

        conn.commit()



def changeOneuser(): #интерфейс изменить пользователя
    global tab,root1,root
    root = Toplevel()
    leftFrame  = Frame(root)
    rightFrame = Frame(root)
    Login = Label(leftFrame,text='Лоигн')
    roleL = Label(rightFrame,text='Тип пользователя')
    e1 = Entry(leftFrame)
    roleList = ScrolledList(getSpeciality(),parent=rightFrame)
    okB     = Button(root,text='Ок')
    cancelB = Button(root,text='Отмена')

    Login.grid(row=0,column=0)
    roleL.grid()
    e1.grid(row=1,column=0)
    roleList.grid(row=1)
    leftFrame.grid()
    rightFrame.grid(column=1,row=0)
    okB.grid(row=2)
    cancelB.grid(row=2,column=1)
def ahtung(f):
    print('ahtung=',f)

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

def changeUser():
    global tab,root1,root
    root = Toplevel()

    leftFrame  = Frame(root)
    rightFrame = Frame(root)
    options = getUsers(None)
    print('===opt=',options)
    userList = ScrolledList(options,parent=leftFrame)
    findE   = Entry(rightFrame, text='Найти')
    changeB = Button(rightFrame, text='Изменить',command=(lambda:changeOneuser() ) )
    delB    = Button(rightFrame, text='Удалить', command=(lambda:delUser(userList)       ) )
    changeB.pack()
    delB.pack()
    findE.pack()
    #options = ( ('Lumberjack-%s' % x) for  x in range(20))

    findE.insert(0,'Найти')
    #findE.bind('<KeyPress>',  test('as' ) )
    print('in changeOne User^ find=',findE.get())
    #root.bind('<KeyPress>',  reDrawUser(findE.get() ) ) ##
    def handleFindPress(event):
        print('handler  use', findE.get())
        reDrawUser(findE.get(),userList ).__next__()
        reDrawUser( findE.get(),userList )
        #ahtung('ss00')
        #print('fin')
    #findE.bind('<KeyPress>',  handleFindPress )
    root.bind('<KeyPress>',  handleFindPress ) #==!!!===аргументы передаются в контексте,а мне нужно передать аргумент не
    #из контекста события (не то что вызвало событие, а то что находиться в соседнем виджите!), решение только так, как выше.???

    leftFrame.pack()
    rightFrame.pack()
    root.mainloop()



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



    root1.mainloop()


mymain()