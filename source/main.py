#__author__ = 'Вячеслав'
#коннект в бд
#выбор типа пользователя
#работа в нем
from share_data import *
from tkinter import *
from tkinter.messagebox import *
from sys import exit as ext
from hashlib import md5

master = Tk()
master.resizable(False, False)
#root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна===========
err = Label(master, text='')
b1 = '<Button-1>'
b1w = '<Double-1>'
b2 = '<Button-2>'
b2w = '<Double-2>'



def creatUser():
    cur.execute("insert into users values (?,?,?)", ('kola', 'qwer', 1))
    conn.commit()


def ViewUser(name):
    request = 'select * from users where name="' + str(name) + '"'
    i = 0
    buf = ""
    for s in cur.execute(request):
        buf = s
        i += 1
    if i > 1: print("users table is invalid")
    if buf != '':
        return buf
    else:
        print('не найдено не одного юзера')
        return buf

#s=ViewUser('kola')
#print(s)


def okAct(event):
    if e1.get() == '':
        showerror('Ошибка', "Пожалуйста, введите Логин")
        return
    if e2.get() == '':
        showerror('Ошибка', "Пожалуйста, введите Пароль")
        return


    hsh = md5()
    hsh.update(e2.get().encode('utf-8'))

    # print( hsh.hexdigest() )

    #exec(librarian)
    #master.quit()
    #cur.execute('update users set pass=? where name=?', (hsh.hexdigest(), '1')) #смена пароля
    #conn.commit()
    #tmplogin=
    passlower = e1.get().lower()
    request = 'select * from users where name="' + passlower + '"'
    hashtable = ''
    i = execsql('''SELECT name FROM sqlite_master
    WHERE type='table'
    ORDER BY name;''')
    i = list(i)

    for row in cur.execute(request):
        hashtable = row[1]
        #print(str(row[0])+str(row[1]),  str(e1.get())+ str (hsh.hexdigest() ))
    #print(str(row[0])+str(row[1]) ==   str(e1.get())+ str (hsh.hexdigest() ))

    if hashtable != '':
        #print('hsh msg 1')
        if str(row[0]) + str(row[1]) == str(passlower) + str(hsh.hexdigest()):  #проверка на правельность данных!!!
            #print(row, row[2])
            if row[2] == 'Администратор':
                master.destroy()
                import librarian
            elif row[2] == 'Библиотекарь':
                master.destroy()
                import midlelibrarian
            else:
                showerror('Ошибка', 'Ошибка роли, обратитесь в техподдержку')

                #import librarian
        else:
            showerror('Ошибка', 'Неверные пароль')
    else:
        showerror('Ошибка', 'Неверное сочитание логин/пароль')


def quit(event):
    ext()
    return

button1 = Button(text='Да')
button2 = Button(text='Отмена')

button1.bind(b1, okAct)
button2.bind(b1, quit)

label1 = Label()
label2 = Label()
entry1 = Entry()
entry2 = Entry()

Label(master, text="Логин").grid(row=0)
Label(master, text="Пароль").grid(row=1)

e1 = Entry(master)
e2 = Entry(master, show='*')

e1.grid(row=0, column=1, padx=5, pady=5, columnspan=2, ipadx=5)
e2.grid(row=1, column=1, padx=5, pady=5, columnspan=5, ipadx=5)
button1.grid(row=2, column=0, columnspan=1, ipadx=5, ipady=5, rowspan=10)
button2.grid(row=2, column=2, columnspan=2, ipadx=5, ipady=5)
e1.focus_set()
master.bind('<Return>', okAct)
master.bind('<Escape>', quit)
master.mainloop()
