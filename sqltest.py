__author__ = 'Вячеслав'


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























'''
if __name__ == '__main__':
    root = Tk()
    tab = Table(root)
    tab.pack()
    tab.cells[1][1].value.set('test')
    tab.cells[2][2].value.set( tab.cells[1][1].value.get() )

    root.mainloop()'''