﻿import sqlite3
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showerror
#print('name=%s' % __name__)
#if __name__ == '__main__':


def tuple2str(t):
    tmp = ''
    for x in t:
        tmp = tmp + str(x) +','
    tmp = tmp[0:-1]
    return tmp
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


class ScrolledList(Frame):
    def __init__(self, options=testOpt(), parent=None,newBind=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                   # make me expandable
        self.makeWidgets(options)
        self.reBind = newBind
        actions='multi'

    def setHeight(height):
        pass
    #isinstance
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

        select = [int(x) for x in selections] #индексы
        print('\n====------------')
        print(selections)
        print(select)
        print([int(x) for x in selections])
        selecttxt = [self.listbox.get(x) for x in select]
        print(selecttxt)
        print('\n====------------')
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
        if not len(index):return -1
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
            #if isinstance(label,list): # выдает ошибка не понятно почему
            #if type(label)=="<class 'list'>" or type(label)=="<class 'tuple'>": # не пашет
                
            label = tuple2str(label)
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
    def setAct(self,newF):
        self.listbox.bind('<Double-1>', newF,)

    def setActOneClick(self,newF):
        self.listbox.bind('<Button-1>', newF,)

    def setActExist(self,event, handler):
        self.listbox.bind(event, handler)    

    def getContentGen(self):
        tmp = []
        i=0
        while True:    
            msg = self.listbox.get(i)
            i += 1
            if msg=='':
                break
            yield msg

    def getContent(self):
        tmp = []
        i=0
        while True:    
            msg = self.listbox.get(i)
            i += 1
            if msg=='':
                break
            return msg

           