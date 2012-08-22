ctrl+ alt + a - выравниваем равенства выделенном отрезке
TERMINAL:
Open Terminal at File
    Press ctrl+shift+t on Windows and Linux, or cmd+shift+t on OS X 
Open Terminal at Project Folder
    Press ctrl+alt+shift+t on Windows and Linux, or cmd+alt+shift+t on OS X 
   http://wbond.net/sublime_packages/terminal

  


все читатели которые взяли книги

SELECT b.title,r.fio,r.NomberAbonement, g.idbook,g.idreader,r.id,b.id FROM getting as g JOIN books as b JOIN readers as r 
WHERE g.idbook=b.id AND g.idreader=r.id

упрощенный:
SELECT b.title,r.fio,r.NomberAbonement FROM getting as g JOIN books as b JOIN readers as r 
WHERE g.idbook=b.id AND g.idreader=r.id



вернул sqlmy()
['select NomberAbonement,NomberAbonement,fio from readers ORDER BY low(NomberAbonement) COLLATE sort ']


--SELECT COUNT(active) FROM getting as g ON g.idreader WHERE (SELECT g.id WHERE NomberAbonement="opi-5428")
--SELECT id FROM readers WHERE NomberAbonement="opi-5428"


книги по читательскому билету:
SELECT b.title, b.ISBN,b.ISBN,b.id FROM books AS b WHERE id 
IN ( SELECT idbook FROM getting JOIN readers WHERE idreader 
IN ( SELECT readers.id where readers.NomberAbonement='m-9'))

количество книг по чит. билету
SELECT COUNT(g.idreader) FROM getting as g WHERE idreader IN (SELECT r.id FROM readers AS r WHERE NomberAbonement='m-9')

ВСЕ ИЗ ДВУХ ТАБЛИЦ!
SELECT b.*, r.* FROM books as b, readers As r


книги по idreaders
SELECT b.autors,b.title FROM books as b WHERE id IN( SELECT idbook FROM getting as g JOIN readers as r WHERE idreader IN 
( SELECT r.id where r.NomberAbonement="opi-5428"))