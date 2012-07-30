__author__ = 'Вячеслав'
import sqlite3,re,random,datetime, time
from tkinter.ttk import *
from tkinter.messagebox import showerror
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
    conn = sqlite3.connect('db6.sqlite')
    cur = conn.cursor()
    conn.create_collation('sort',sortTextInDb)
    conn.create_function("low", 1, low)
except:
    showerror('Ошибка', 'Ошибка при рабое с базой данных, возможно ее кто-то уже использует.')
    exit()


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

        for key in opt:
            Radiobutton(self, text=key,
                command=self.onPress,
                variable=self.var,
                value=key).pack(anchor=NW)
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


    def onPress(self):
        pick = self.var.get()
        print('you pressed', pick)
        #print('result:', demos[pick]())
        print(self.index,self.getbyname(pick) )
    def reportIndex(self):
        return self.getbyname(self.var.get())
    def report(self):
        return self.var.get()

#if __name__ == '__main__': Demo().mainloop()
