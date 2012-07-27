__author__ = 'Вячеслав'
import sqlite3
con = sqlite3.connect("catalog.db")
cur = con.cursor()        # Создаем объект-курсор
sql = """\
INSERT INTO user (email, passw)
VALUES ('unicross@mail.ru', 'password1')
"""
sql = 'INSERT INTO user (email, passw)
try:
    cur.execute(sql)      # Выполняем SQL-запрос
except sqlite3.DatabaseError as err:
    print("Ошибка:", err)
else:
    print("Запрос успешно выполнен")
    con.commit()          # Завершаем транзакцию
cur.close()               # Закрываем объект-курсор
con.close()               # Закрываем соединение
