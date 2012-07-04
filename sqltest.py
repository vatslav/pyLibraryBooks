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

