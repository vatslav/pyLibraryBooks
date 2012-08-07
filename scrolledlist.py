import sqlite3
from tkinter import *
from tkinter.messagebox import showerror
def sortTextInDb(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1==s2: return 0
    elif s1>s2: return  1
    else: return -1
def low(s):
    return s.lower()

def testOpt():
    return( ('Lumberjack-%s' % x) for  x in range(20))
try:
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    conn.create_collation('sort',sortTextInDb) #встраиваем сортировку
    conn.create_function("low", 1, low) #встраиваеваем функцию, 1 - кол-во аргмуентов
except sqlite3.OperationalError as dbLock:
    showerror('Ошибка', dbLock)
    exit()

class ScrolledList(Frame):
    def __init__(self, options=testOpt(), parent=None,newBind=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                   # make me expandable
        self.makeWidgets(options)
        self.reBind = newBind
        actions='multi'

    def setHeight(height):
        pass
    isinstance
    def handleList(self, event):
        #if self.reBind == None:

        #index = self.listbox.curselection()                # on list double-click
        #label = self.listbox.get(index)                    # fetch selection text
        #print('label=',label, 'index=',index)
        #self.runCommand(label)                             # and call action here
        # or get(ACTIVE)


        selections = self.listbox.curselection()
        select = [int(x)+1 for x in selections] #индексы
        selecttxt = [self.listbox.get(x) for x in select] #содержание индексов (может быть совсепм маленьким
        print(select)
        print(selecttxt)
        return select
        #self.runCommand(select)
        #else:
            #selecttxt = (self.listbox.get(x) for x in list(select) )
            #select1 = (int(x)+1 for x in selections)
            #return selecttxt,select1


    def getCurMulti(self):
        selections = self.listbox.curselection()
        select = [int(x)+1 for x in selections] #индексы
        selecttxt = [self.listbox.get(x) for x in select]
        return  select,selecttxt
   #def getCurMulti(self):



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

    def clearlist(self):
        try:
            self.listbox.delete(0,99999999)
        except StopIteration:
            pass

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


           