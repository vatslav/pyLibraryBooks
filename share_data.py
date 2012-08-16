__author__ = 'Вячеслав'
import sqlite3,re,random,datetime, time

from tkinter.messagebox import showerror
from tkinter.ttk import *
def sortTextInDb(s1,s2):
    s1=str(s1);  s2 = str(s2)
    s1 = s1.lower()
    s2 = s2.lower()
    if s1==s2: return 0
    elif s1>s2: return  1
    else: return -1
def low(s):
    s = str(s)
    return s.lower()
try:
    conn = sqlite3.connect('mydb1.sqlite', isolation_level='DEFERRED')
    cur = conn.cursor() 
    conn.create_collation('sort',sortTextInDb)
    conn.create_function("low", 1, low)

    con2 = sqlite3.connect('mydb1.sqlite', isolation_level='DEFERRED')
    cur2 = conn.cursor()
    con2.create_collation('sort',sortTextInDb)
    con2.create_function("low", 1, low)


except:
    showerror('Ошибка', 'Ошибка при рабое с базой данных, возможно ее кто-то уже использует.')
    exit()
def no(Event=True):
    pass
def dest(r1,r2):
    r1.bind('<KeyPress>',no)
    r2.destroy()

def tuple2str(t):
    tmp = ''
    for x in t:
        tmp = tmp + str(x) +','
    tmp = tmp[0:-1]
    return tmp

def funcGet(*values):
    tmp=[]
    #print(values,type(values),len(values))
    for obj in values[0]:
        if str(type(obj)) == "<class 'tkinter.Entry'>":
            tmp.append(obj.get())
        else:
            tmp.append(obj)
    return tuple(tmp)

def inscsql(request1,*values):
    trace=False

    #if not isinstance(values,tuple):
        #values = funcGet(*values)
    if len(values)==1:
        values = values[0]
    try:
        if not len(values):cur.execute(request1)
        if trace:
            print(request1,values)
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
def inscsql2(request1,*values):
    trace=False

    #if not isinstance(values,tuple):
        #values = funcGet(*values)
    if len(values)==1:
        values = values[0]
    try:
        if not len(values):cur.execute(request1)
        if trace:
            print(request1,values)
        else:
            cur2.execute(request1,values)
            for obj in cur2:
                print(obj)
    except sqlite3.IntegrityError as NoUn:
        showerror('Ошибка', NoUn)
        return None
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
        return None

    else:
        con2.commit()
        return True


#крутяцкая функция!:)
def execsql( request1,*values):
    #if cr=='':cr=cur

    if len(values):
        values = funcGet(*values)
    try:
        if not len(values):cur.execute(request1)
        else:
            cur.execute(request1,values)
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        conn.commit()
        for line in cur:
            yield line

def execsql2( request1,*values):
    #if cr=='':cr=cur

    if len(values):
        values = funcGet(*values)
    try:
        if not len(values):cur.execute(request1)
        else:
            cur2.execute(request1,values)
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        con2.commit()
        for line in cur:
            yield line

"create a group of radio buttons that launch dialog demos"

from tkinter import *                # get base widget set
#from dialogTable import demos        # button callback handlers
#from quitter import Quitter          # attach a quit object to "me"

class RadioBut(Frame):
#opt=['1','2','3']
    def __init__(self, parent=None, opt=['1','2','3'],titile=None,trans=None,default=None,**options):
        Frame.__init__(self, parent, **options)
        self.pack()
        if titile:
            Label(self, text=titile).pack(side=TOP)
        self.var = StringVar()
        self.cursize = 0
        self.index = {}
        self.scelet = []

        for key in opt:
            rb = Radiobutton(self, text=key,
                command=self.onPress,
                variable=self.var,
                value=key)
            rb.pack(anchor=NW)
            self.scelet.append(rb)
            self.index[key]=self.cursize
            self.cursize += 1
        if not default:default=key
        self.var.set(default) # select last to start
        #Button(self, text='State', command=self.report).pack(fill=X)

        #Quitter(self).pack(fill=X)
    def view(self):
        return self.index
    def getbyname(self,name):
        return self.index[name]


    def onPress(self):#действие по нажатии кнопки
        pick = self.var.get()
        print('you pressed', pick)
        #print('result:', demos[pick]())
        print(self.index,self.getbyname(pick) )
    def reportIndex(self):
        return self.getbyname(self.var.get())
    def report(self):
        return self.var.get()

class EnryV(Frame):
    def __init__(self, parent=None,opt=[1,2,3],r=[], **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        #self.tools()
        self.system = []
        print(opt)
        for x in opt:
            nframe = Frame(self)
            var = StringVar()
            Entry(nframe).pack(side=RIGHT)
            Label(nframe,text=x[0]).pack(side=LEFT)
            self.system.append((var,x[0]))
            var.set(x[1])
            nframe.pack()
    def getState(self):
        return self.system
    def getOnlyStateEntry(self):
        return [x[0] for x in self.system]
    def getOnlyStateEntryGenerator(self):
        yield (x[0] for x in self.system)
    def getStateGenerator(self):
        yield [x[0] for x in self.system]

def makeform(root, fields,w1=15,w2=None):
    entries = []
    var = StringVar()
    for field in fields:
        #field=field[0]
        var = StringVar()
        row = Frame(root)                           # make a new row
        lab = Label(row, width=w1, text=field)       # add label, entry
        ent = Entry(row,textvariable=var)
        if w2!=None:
            ent.config(width=w2)
        row.pack(side=TOP, fill=X)                  # pack row on top
        lab.pack(side=LEFT,expand=YES,)
        ent.pack(side=RIGHT, expand=YES, fill=X)    # grow horizontal
        entries.append(var)
    return entries


class chekbutton(Frame):
    def __init__(self, parent=None, title=None, opt=[1,2,3], **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.tools()
        if title:
            Label(self, text=title).pack()
        self.vars = []
        self.sd={}
        self.allrb={}
        self.nn = {}
        ptr = 0
        for key in opt:
            var = IntVar()
            var.set(0)
            s = Checkbutton(self,
                text=key,
                variable=var,
                )#command=lambda:pass
            s.pack(side=LEFT) #command=demos[key]
            self.vars.append(var)
            self.sd[key]=var
            self.allrb[key]=s
            self.nn[ptr]=var
            ptr += 1
    def gettext(self):
        pass
        #for x in self.ss:
           # print(x['text'],self.vars[x])

    def setFlag(self,key,value=True):
        self.sd[key].set(value)

    def setFlagByIndex(self,index,value=True):
        self.nn[index].set(value)

    def setComand(self,com):
        for name, rb in self.allrb.items():
            rb['command']=lambda:com()
    #def setFlagsOne(self,key,value=True):



    def report(self):
        for x,y in self.sd.items():
            yield x, y.get()

    def reportDict(self):
        d={}
        for key,value in self.sd.items():
            d[key]=value.get()
        return d

    def act(self,key):
        print(key)
        self.report()
    def tools(self):
        frm = Frame(self)
        frm.pack(side=RIGHT)
        #Button(frm, text='State', command=self.report).pack(fill=X)
        #Quitter(frm).pack(fill=X)


def viewreader():
    root = Toplevel()
    root.title(string='Выбирети учетную запись для изменения')
    leftFrame  = Frame(root)
    rightFrame = Frame(root)
    options = ex
    title = Label(root,text='Выбирети учетную запись для изменения')
    title.pack()
    userList = ScrolledList(options,parent=leftFrame,newBind=changeOneuser )
    #userList.setBind(changeOneuser())

    nameText = StringVar()
    numText  = StringVar()
    findE   = Entry(rightFrame, textvariable=nameText)
    findNum = Entry(rightFrame,textvariable=numText)
    changeB = Button(rightFrame, text='Изменить',command=(lambda:changeOneuser(userList.getCur()) ) )
    delB    = Button(rightFrame, text='Удалить', command=(lambda:delUser(userList)       ) )
    changeB.pack()
    delB.pack()
    findE.pack()

    #options = ( ('Lumberjack-%s' % x) for  x in range(20))
    nameText.set('Поиск по ФИО читателя')
    numText.set('Поиск по Читательскому билету читателя')

    findNum.pack()
    findNum.pack()
    #findE.bind('<KeyPress>',  test('as' ) )
    def handleFindPress(event):
        userList.listbox.clear()
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
            print(userList.getCur())#changeOneuser(userList.getCur())
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


class modernchekbutton(Frame):
    def __init__(self, parent=None, title=None, opt=[1,2,3], **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.tools()
        if title:
            Label(self, text=title).pack()
        self.vars = []
        self.sd={}
        self.allrb={}
        self.nn = {}
        self.corent = []
        self.scelet = []

        ptr = 0
        for key in opt:
            var = IntVar()
            var.set(0)
            s = Checkbutton(self,
                text=key[0],
                variable=var) #,command=print('TATATAT!' )''' 
            s.pack(side=LEFT) #command=demos[key]
            self.vars.append(var)
            self.sd[key[0]]=var
            self.allrb[key[0]]=s
            self.nn[ptr]=var
            self.corent.append((key[1],var))
            self.scelet.append(s)
            ptr += 1

    def getSetup(self):
        tmp = [x[0] for x in self.corent if x[1].get()>0 ]
        return tmp
    def setAct(self,handler):
        for x in self.scelet:
            x['command']=handler

    def setFlag(self,key,value=True):
        self.sd[key].set(value)

    def setFlagByIndex(self,index,value=True):
        self.nn[index].set(value)

    def setComand(self,com):
        for name, rb in self.allrb.items():
            rb['command']=com
        #def setFlagsOne(self,key,value=True):



    def report(self):
        for x,y in self.sd.items():
            yield x, y.get()

    def reportDict(self):
        d={}
        for key,value in self.sd.items():
            d[key]=value.get()
        return d

    def act(self,key):
        print(key)
        self.report()
    def tools(self):
        frm = Frame(self)
        frm.pack(side=RIGHT)
        #Button(frm, text='State', command=self.report).pack(fill=X)
        #Quitter(frm).pack(fill=X)