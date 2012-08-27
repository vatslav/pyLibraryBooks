__author__ = 'Вячеслав'
import sqlite3,re,random,datetime, time
#from scrolledlist import *
from tkinter.messagebox import showerror

from scrolledlist import ScrolledList
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
    conn = sqlite3.connect('mydb1.sqlite', isolation_level='IMMEDIATE')
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

class inform(Frame):
    """docstring for inform"""
    def __init__(self, root, fields,w1=15,w2=None):
        self.entries = []

        #self.vars = []
        for field in fields:
            #field=field[0]
            self.var = StringVar()
            self.row = Frame(root)                           # make a new self.row
            self.lab = Label(self.row, width=w1, text=field)       # add self.label, self.entry
            self.ent = Entry(self.row,textvariable=self.var)
            if w2!=None:
                self.ent.config(width=w2)
            self.row.pack(side=TOP, fill=X)                  # pack row on top
            self.lab.pack(side=LEFT,expand=YES,)
            self.ent.pack(side=RIGHT, expand=YES, fill=X)    # grow horizontal
            self.entries.append(self.var)
            #self.vars.append(self.var)
    def getContent(self):
        return self.entries
    def getStr(self):
        return [x.get() for x in self.entries]
    def setContent(self,rows):
        for x in range(len(self.entries)):
            self.entries[x].set( rows[x] )
    def setContentByIndex(self,index,row):
        self.entries[index].set( row )
                



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











class modernchekbutton(Frame):
    def __init__(self, parent=None, title=None, opt=[(1,2),(2,3),(3,4)], **options):
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


class modernRadioBut(Frame):
#opt=['1','2','3']
    def __init__(self, parent=None, opt=[(1,2),(2,3),(3,4)],titile=None,trans=None,default=None,**options):
        Frame.__init__(self, parent, **options)
        self.pack()
        if titile:
            Label(self, text=titile).pack(side=TOP)
        self.var = StringVar()
        self.cursize = 0
        self.index = {}
        self.scelet = []

        for key in opt:
            rb = Radiobutton(self, text=key[0],
                command=self.onPress,
                variable=self.var,
                value=key[1])
            rb.sinonnym = key[1]
            rb.pack(anchor=NW)
            self.scelet.append(rb)
            self.index[key[1]]=self.cursize
            self.cursize += 1
        if not default:default=key
        self.var.set(default) # select last to start
        #Button(self, text='State', command=self.report).pack(fill=X)

        #Quitter(self).pack(fill=X)
    def view(self):
        return self.index
    def getbyname(self,name):
        print(self.index)
        print('name=%s' %name)
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
    def setAct(self,handler):
        for rb in self.scelet:
            rb['command']=handler
    def getSinonym(self):
        return self.scelet[ self.getbyname(self.var.get()) ]

def coroutine(func):
    def start(*args,**kwargs):
        g = func(*args,**kwargs)
        g.next()
        return g
    return start

from tkinter.ttk import *
class MyTopLevel(ScrolledList):
     """docstring for MyTopLevel"""
     #super(MyTopLevel, self).__init__()

     def __init__(self, event=True, listcmd=[], configcmd=[],  listcontent=[], configfields=[],okcmd=[],parent=''):
        def clear(func):
            self.toplist.clearlist()
            return func
        #configcmd = clear(configcmd)
        def handlercmdconf():
            self.chb.setFlagByIndex(int(self.rb.reportIndex() ) )
            return configcmd()
            

        if not listcontent:
            listcontent = (('Тестовая строка-%s' % x) for x in range(100) )

        if parent: self.root = Frame(parent)
        else:      self.root = Toplevel()
        centr,self.bottom,top,right = Frame(self.root), Frame(self.root), Frame(self.root), Frame(self.root) #frames
        #центральный лист
        self.toplist = ScrolledList(parent=centr,options=listcontent) #central LIST
        self.toplist.listbox.config(height=25,width=70,font=('courier'))
        sbx = Scrollbar( centr, orient=HORIZONTAL, command=self.toplist.listbox.xview)
        self.toplist.listbox.configure(xscrollcommand=sbx.set)
        sbx.pack(side=BOTTOM, fill=X)
        # поисковая полоска и кнопки ок отмена
        self.findtext = StringVar()
        self.fent = Entry(self.bottom, textvariable=self.findtext)
        self.fent.grid(row=0,column=0)
        self.bfent = Button(self.bottom,text='Найти',command=lambda:handlercmdconf() )
        self.bfent.grid(row=0,column=1)
        if okcmd==[]:okcmd=lambda:1

        self.b =Button(self.bottom,text='Ok',command=lambda:okcmd() )
        self.b.grid(row=1)
        Button(self.bottom,text='Отмена', command=lambda:self.root.destroy()).grid(row=1,column=1)


        if not configfields:
            configfields=[(x,x) for x in ['1','2','3','4']]
        #[['Номер Абонемента', 'NomberAbonement', 1], ['ФИО', 'fio', 1], ['адрес', 'adress', 1], ['телефон', 'telephone', 0]]

    #радио и флажки
        self.chb = modernchekbutton(parent=top,title='отображать поля:',opt=configfields )
        self.rb  = modernRadioBut(parent=right, titile='Сортировать и искать по:',opt=configfields,default=configfields[0][0] )
        self.chb.setFlagByIndex(self.rb.reportIndex())
    

    #действия по нажатию кнопки
        if configcmd:
            for x in self.rb.scelet:
                x['command'] = handlercmdconf 
            self.chb.setAct(handlercmdconf)
            #root.titile(string=)
        if listcmd:
            self.toplist.setAct(listcmd)


         #взаиморасположение
        centr.grid(row=1,column=4)
        self.bottom.grid(row=2,column=4)
        top.grid(row=0,column=4)
        right.grid(row=1,column=5)
        #showerror('ТАДА','ТАДА')
    #def start(self,a=2):
    #    self.root.mainloop()


def countBooksByNA(na):
    return list(execsql('''SELECT COUNT(active) FROM getting JOIN readers WHERE active=1 AND idreader IN 
        ( SELECT readers.id where readers.NomberAbonement="%s")''' % na))[0][0]

def countBooksByISBN(isbn):
     return list(execsql('''SELECT COUNT(g.active) FROM getting as g WHERE g.active=1 and g.idbook IN 
        (SELECT id FROM books where ISBN="%s" )''' % isbn))[0][0]   

def countBooksBeByISBN(isbn):
     return list(execsql('''SELECT COUNT(classbook) FROM exemplars WHERE classbook="%s"''' % isbn))[0][0]   