
from share_data import *
__author__ = 'Вячеслав'
#from share_data import *
try:
    from source.share_data import MyTopLevel
    from source.share_data import *
    from source.share_data import *
except ImportError:pass
#import midlelibrarian.fieldOfBooksRus,midlelibrarian.fieldOfBooks
from tkinter import *
#from midlelibrarian import getBooks
fieldOfBooksRus = ('ISBN', 'ББК', 'Автор', 'Название', 'Год издания', 'Издательство', 'ключевые слова')
fieldOfBooks = ('ISBN','bbk', 'autors', 'title', 'years', 'publisher', 'keywords')
fieldOfBookD = dict(zip(fieldOfBooksRus,fieldOfBooks))

root = Tk()
cf = [(fieldOfBooksRus[x],fieldOfBooks[x]) for x in range(len(fieldOfBooks))]
def getBooks(mask=None,index=3,table='books', sortby='title',field={},state={}): #фильтр на книги
    global fieldOfBooks
    if mask:
        template = re.compile(mask)
    if not field or not state: #если запрос по всем стодбцам
        request = 'select ISBN,bbk,autors,title,years,publisher,keywords,city from ' + table + ' ORDER BY low(' +sortby+ ') COLLATE sort' #выводим, с сортировкой без учета регистра по столбцу name
    else:#оставляем толькоотмеченные столбцы
        request = 'select '
        tmp = list(fieldOfBooks)
        print(tmp)
        for key,value in field.items():
            if not state[key]:
                tmp.remove(value)
        tmp.insert(0,'ISBN') #полюому будет ISBN
        tmpstr = tuple2str(tmp)
        print(tmpstr)
        request = request + tmpstr + ' from '+table+' ORDER BY low(' +sortby+ ') COLLATE sort'
        try:
            index = tmp.index(sortby)
        except ValueError as er:
            showerror('Ошибка', er)
            return
    try:
        for row in cur.execute(request):
            if not mask:
                yield row
            else:
                #print(row)
                pb = template.search(str(row[index]).lower())
                if pb:
                    yield row[0],row[1:]
    except sqlite3.OperationalError as dbLock:
        showerror('Ошибка', dbLock)
    else:
        conn.commit()
isbns = []
def find():
    xw.toplist.clearlist()
    txt  = xw.findtext.get()
    [isbns.pop() for x in range(len(isbns))]
    row  = []
    issb = []
    #print('ISBNS=!!===++++', list(isbns))
    for x in getBooks(txt,index=xw.rb.reportIndex(),sortby=fieldOfBooks[xw.rb.reportIndex()],
        state=xw.chb.reportDict(),field=fieldOfBookD):
        isbns.append(x[0])
        row.append( tuple2str(x[1:]) )

    for x in range(len(row)):
        issb.append( int(countBooksByISBN(isbns[x]))  )
    for x in range(len(row)):
        j = int( countBooksBeByISBN(isbns[x]) )
        row[x] += ' ' + str(j-issb[x]) + 'из' + str(j)



        #x += ' выдано:'+str(countBooksByISBN(y))
    #print(2)
    for x in row:
        xw.toplist.listbox.insert('end',x)


#,listcmd=tl,okcmd=h_tl
tl = lambda:1
hfind = lambda event:find()
xw = MyTopLevel(parent=root,configfields=cf,configcmd=find)
xw.rb.var.set('title')
xw.chb.setFlagByIndex(3)
xw.chb.setFlagByIndex(2)
xw.chb.setFlagByIndex(0,value=False)


xw.root.grid(column=4,row=0)

root.bind('<KeyPress>',hfind)
xw.cmd_ = find
xw.cb['command']=lambda:quit()
xw.cb['text']='Выход'

xw.b.grid_remove()
root.title(string='Поиск книг')
find()
xw.fent.focus()

root.mainloop()