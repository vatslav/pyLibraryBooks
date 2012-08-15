import datetime
from tkinter import *
from tkinter.simpledialog import *
s = datetime.MAXYEAR
td = datetime.date.today()
print(s,type(td),str(td)[0:4])
print(datetime.MINYEAR,datetime.date.today(),datetime.date.fromordinal(7635))
print(datetime.date(2012,1,5))
print(td.isocalendar())
print(td.ctime(),td.isoformat(),td)
print(td.toordinal())
print(datetime.date.fromordinal(td.toordinal()+31))
print(td)
ask