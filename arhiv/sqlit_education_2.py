__author__ = 'Вячеслав'
import sqlite3
def sortTextInDb(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1==s2: return 0
    elif s1>s2: return  1
    else: return -1
con = sqlite3.connect(':memory:',isolation_level=None)
con.create_collation('myfunc',sortTextInDb)
cur = con.cursor()
cur.execute("CREATE TABLE words (word TEXT)")
cur.execute("INSERT INTO words VALUES('единица1')")
cur.execute("INSERT INTO words VALUES('Единый')")
cur.execute("INSERT INTO words VALUES('Единица2')")
cur.execute('select * from words ORDER BY word')

for line in cur:
    print(line[0])
print('==')
cur.execute('select * from words ORDER BY word COLLATE myfunc')
for line in cur:
    print(line[0])