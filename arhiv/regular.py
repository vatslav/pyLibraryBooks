__author__ = 'Вячеслав'
import re
a  = re.compile('cat{1,2}')
a1 = re.compile('cat{1}')
a2 = re.compile('cat')
a0 = re.compile('[a-z]+')
a3 = re.compile( '[cat]+ ')
a4 = re.compile('[cat]+')
w='ol0 cat olca cat tacc'
s = a.search(w)
'''
print(a.search(w).group(), a.search(w).span())
print(a1.search(w).group(), a.search(w).span())
print(a2.search(w).group(), a.search(w).span())
print(a0.search(w).group(), a.search(w).span())
print(a3.search(w).group(), a.search(w).span())
print(a4.search(w).group(), a.search(w).span())
'''
word = ('mather','fathe','galga','nest','set','pet','cat','mamblet','superjet','athlet','df a at')
def find(mask):
    temp = re.compile(mask)
    for x in word:
        m = temp.search(x)
        if m:
            print(m.group(),x,m.span() )
find('ga')