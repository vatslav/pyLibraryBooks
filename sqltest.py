__author__ = 'Вячеслав'


for row in cur.execute('select * from users where name="иван" '):
    print(row)



#cur.execute('update users set pass=? where name=?', (hsh.hexdigest(), 'иван')) #смена пароля
#conn.commit()
