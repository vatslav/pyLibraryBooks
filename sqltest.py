__author__ = 'Вячеслав'


#===Отлавливаем ошибку!
try:
    a=2/0
except ZeroDivisionError as zero:
    print(zero)


for row in cur.execute('select * from users where name="иван" '):
    print(row)

e1.delete(0, END)
e1.insert(0,'same text')
e1.grid_remove()


#cur.execute('update users set pass=? where name=?', (hsh.hexdigest(), 'иван')) #смена пароля
#conn.commit()



goodversion
cur.execute('update users set pass=? where name=?', (hsh.hexdigest(), 'иван')) #смена пароля
conn.commit()







def creatUsers():
    global tab,root1,root
    #root2 = Toplevel(root1)
    root = Toplevel(root1)
    #root1.withdraw(True)
    #root.title('table111')
    #root2.overrideredirect(True)
    tab = Table(root,3,2)
    tab.pack()
    setTitile(['Имя','Пароль','Тип пользователя'])
    com = Button(root,text='Подтвердить', command=(lambda: exBut() ) )
    com.pack()


def getTab(x=1,y=0):
    return tab.cells[x][y].value.get()
def setTab(x=1,y=0, val=None):
    global tab
    tab.cells[x][y].value.set(val)
def setTitile(val):
    global tab
    for i in range( len(val) ):

        tab.cells[0][i].value.set(val[i])

class Cell(Entry):
    def __init__(self, parent):
        self.value = StringVar()
        Entry.__init__(self, parent, textvariable = self.value)

class Table(Frame):
    def __init__(self, parent, columns = 4, rows = 10):
        Frame.__init__(self, parent)
        self.cells = [[Cell(self) for i in range(columns)] for j in range(rows)]
        [self.cells[i][j].grid(row = i, column = j) for i in range(rows) for j in range(columns)]


def viewTable(x,y,r1,title=1):
    global root1,root
    y=y+1
    root = Toplevel(r1)
    tab = Table(root,x,y)
    tab.pack()
    com = Button(root,text='Подтвердить')
    com.pack()


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




def exBut():
    root1.title('Создание нового пользователя')
    if getTab(1,0)=='' or getTab(1,2)=='' or getTab(1,1)=='':
        showerror('Ошибка ввода', "Пожалуйста, заполните все поля ввода")
    else:
        hsh = md5()
        hsh.update( getTab(1,1).encode('utf-8') )
        global root1,root,tab
        cur.execute("insert into users values (?,?,?)", (getTab(1,0).lower(),hsh.hexdigest() ,getTab(1,2)))
        conn.commit()
        #showinfo('Готово', 'Пользователь создан')
        setTab(0,0,'');setTab(0,1,'');setTab(0,2,'')
        root.destroy()







'''
if __name__ == '__main__':
    root = Tk()
    tab = Table(root)
    tab.pack()
    tab.cells[1][1].value.set('test')
    tab.cells[2][2].value.set( tab.cells[1][1].value.get() )

    root.mainloop()'''