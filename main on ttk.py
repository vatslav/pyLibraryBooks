#__author__ = 'Вячеслав'
#коннект в бд
#выбор типа пользователя
#работа в нем
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from sys import exit as ext
import sqlite3
from hashlib import md5
master = Tk()
master.resizable(False,False)
#root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна===========
err = Label(master,text='')
b1  = '<Button-1>'
b1w = '<Double-1>'
b2  = '<Button-2>'
b2w = '<Double-2>'

try:
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
except:
    err['text'] = 'ошибка открытия базы данных'
    err.pack()
    err.mainloop()
    exit()
#cur.execute("")
#391 все из букс
#for row in cur.execute("select * from books"):
 #   print(row)

def okAct(event):
    #root1 = Tk()
    librarian = open('bibleotekar.py','r')
    hsh = md5()
    hsh.update( e1.get().encode('utf-8') )
    print( hsh.hexdigest() )
    e1.delete(0, END)
    e2.delete(0, END)
    #e1.insert(0,'same text')
    #exec(librarian)
    #master.quit()
    cur.execute('update users set pass=? where name=?', (hsh.hexdigest(), 'иван'))
    for row in cur.execute('select * from users where pass="1" '):
        print(row)
    for row in cur.execute('select * from users where name="иван" '):
        print(row)


def quit(event):
    ext()
    return

button1 = Button(text='Да')
button2 = Button(text='Отмена')

button1.bind(b1,okAct)
button2.bind(b1,quit)

label1 = Label()
label2 = Label()
entry1 = Entry()
entry2 = Entry()


Label(master, text="Логин").grid(row=0)
Label(master, text="Пароль").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)



e1.grid(row=0, column=1,padx=5,pady=5,columnspan=2,ipadx=5)
e2.grid(row=1, column=1,padx=5,pady=5,columnspan=5,ipadx=5)
button1.grid(row=2, column=0,columnspan=1,ipadx=5,ipady=5,rowspan=10)
button2.grid(row=2, column=2,columnspan=2,ipadx=5,ipady=5)
master.mainloop()
