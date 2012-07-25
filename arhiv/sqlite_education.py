__author__ = 'Вячеслав'
import sqlite3
con = sqlite3.connect('catalog01.db')
cur = con.cursor()
def creatTable():
    sql = ('''
    CREATE TABLE user (
        id_user INTEGER PRIMARY KEY,
        email TEXT,
        passw TEXT
    )''',
    '''
    CREATE TABLE rubr (
        id_rubr INTEGER PRIMARY KEY AUTOINCREMENT,
        name_rubr TEXT
    )''',
    '''
    CREATE TABLE site (
        id_site INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER,
        id_rubr INTEGER,
        url TEXT,
        title TEXT,
        msg TEXT,
        iq INTEGER
    )
    ''')
    exsqlStep(sql)
def exsql(sql):
    try:
        if str(type(sql))=="<class 'str'>":
            cur.execute(sql)
        elif str(type(sql))=="<class 'tuple'>":
            for x in sql:
                cur.execute(x)
        else: print(type(sql)=="<class 'str'>", str(type(sql))=="<class 'tuple'>", type(sql) )
    except sqlite3.DatabaseError as err:
        print('Ошибка:',err)
    else:
        print('запрос успещно выполнен')
        con.commit()

def exsqlStep(sql):
    if str(type(sql))=="<class 'str'>":
        try:
            cur.execute(sql)
        except sqlite3.DatabaseError as err:
            print('Ошибка:',err)
        else:
            print('запрос успещно выполнен')
            con.commit()
    elif str(type(sql))=="<class 'tuple'>":
        for x in sql:
            try:
                cur.execute(x)
            except sqlite3.DatabaseError as err:
                print('Ошибка:',err)
            else:
                print('запрос успещно выполнен')
                con.commit()

    else: print(type(sql)=="<class 'str'>", str(type(sql))=="<class 'tuple'>", type(sql) )

def insertFieldINUser():
    sql='''\
    INSERT INTO user (email,passw)
    VALUES ('foo@spam.egg','password1')
    '''
    exsql(sql)
#creatTable()
#insertFieldINUser()
def filling():
    t1 = ('программирование',)
    t2 = (2, 'Музыка')
    t3 = ('rubr',2, 'Музыка')
    d = {'id':3, 'name': """Поисковые ' " порталы"""}
    sql_t1 = 'INSERT INTO rubr (name_rubr) VALUES (?)'
    sql_t2 = 'INSERT INTO rubr VALUES (?,?)'
    sql_t3 = 'INSERT INTO (?) VALUES (?,?)' #не работает таблица должна указываться явно
    sql_d  = 'INSERT INTO rubr VALUES (:id, :name)'
    try:
        cur.execute(sql_t1, t1)
        cur.execute(sql_t2, t2)
        cur.execute(sql_d,  d)
    except sqlite3.DatabaseError as err:
        print('Ошибка:',err)
    else:
        print('запрос успещно выполнен')
        con.commit()

#creatTable()
#filling()
def execMany():

    arr = [
        (1, 1, "http://wwwadmin.ru", "Название", "", 100),
        (1, 1, "http://python.org", "Python", "", 1000),
        (1, 3, "http://google.ru", "Гугль", "", 3000)
    ]
    arr2 = [
        (1,1, 'tralala','hna','msgmsg','-1'),
        (1,1, 'tralala','hna','msgmsg','-1'),
        (1,1, 'tralala','hna','msgmsg','-1')
    ]
    sql = """\
    INSERT INTO site (id_user, id_rubr, url, title, msg, iq)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    try:
        cur.executemany(sql, arr)
    except sqlite3.DatabaseError as err:
        print("Ошибка:", err)
    else:
        print("Запрос успешно выполнен")
        con.commit()
def test():
    cur.execute('select *from site')
    for x in cur:
        print(cur.fetchone())
    print('==')
    cur.execute('select *from rubr')
    for id_rubr, name in cur: print('{0},{1}'.format(id_rubr, name))
    print('==============')
    cur.execute('select *from site')
    for x in cur.fetchmany(0):
        print(x)
    print('==========================================')
    cur.execute('select *from site')
    cur.fetchall()


cur.execute('select *from site')
print('tatatata')
print(cur.fetchone())
print('sdfsdfsdf')
print(cur.fetchone())
print(cur.fetchall())
cur.execute('select *from site')
for x in cur.fetchall():
    print(x)