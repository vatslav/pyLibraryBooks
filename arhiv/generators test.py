__author__ = 'Вячеслав'
def countdown(n):
    print('обратный отсчет, начиная с %d' % n)
    while n > 0:
        yield n
        n -= 1
    return

c=countdown(10)
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())

for n in countdown(10):
    print(n)
a=sum(countdown(10))