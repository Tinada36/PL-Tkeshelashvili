# 6 вариант

from random import randint

#1
a = [randint(0, 10) for i in range(10)]
b = []
c = []
print(a)
for i in range(10):
    if a[i] > a[9]:
        b.append(a[i])
    elif a[i] < a[9]:
        c.append(a[i])
print('Элементы больше последнего', b)
print('Элементы меньше последнего', c)

#2
a = []
b = 0
for i in range(10):
    a.append(int(input('Введите число ')))
print(a)
for i in range(10):
    if a[i] > 5:
        b += a[i]
print(b)