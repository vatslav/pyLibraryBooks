__author__ = 'Вячеслав'
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from sys import exit as ext
import sqlite3

b1  = '<Button-1>'
b1w = '<Double-1>'
b2  = '<Button-2>'

class Cell(Entry):
    def __init__(self, parent):
        self.value = StringVar()
        Entry.__init__(self, parent, textvariable = self.value)

class Table(Frame):
    def __init__(self, parent, columns = 4, rows = 10):
        Frame.__init__(self, parent)
        self.cells = [[Cell(self) for i in range(columns)] for j in range(rows)]
        [self.cells[i][j].grid(row = i, column = j) for i in range(rows) for j in range(columns)]

'''
if __name__ == '__main__':
    root = Tk()
    tab = Table(root)
    tab.pack()
    tab.cells[1][1].value.set('test')
    tab.cells[2][2].value.set( tab.cells[1][1].value.get() )

    root.mainloop()'''
def viewTable(x,y,r1,title=1):
    root = Toplevel(r1)
    tab = Table(root,x,y)
    tab.pack()
    tab.cells[1][1].value.set('test')
    tab.cells[2][2].value.set( tab.cells[1][1].value.get() )
    #root.mainloop()


#def getinfo():


def mymain():
    #def cratuser():

    root1=Tk()
    viewAllBooks   = Button (text='посмотреть список книг')
    creatLibrarian = Button (text='Создать библиотекаря')
    viewLibrarian  = Button (text='Посмотреть информацию о библиотекаре')

    #viewAllBooks.bind(b1,)


    #viewAllBooks.pack(expand=False)
    #creatLibrarian.pack(expand=True)
    #viewLibrarian.pack()
    viewAllBooks.grid(padx=20,ipady=5)
    creatLibrarian.grid(columnspan=5,padx=20,ipady=5)
    viewLibrarian.grid(ipady=2)
    viewTable(5,5,root1)


    root1.mainloop()



mymain()