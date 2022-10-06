# 4 вариант

from random import randint

#1
s = [randint(1, 10) for i in range(10)]
max_s = max(s)
print(s)
print('Порядковый номер наибольшего числа', s.index(max_s))

#2
a = [] #[randint(1, 10) for i in range(10)]
b = []
for i in range(10):
	a.append(int(input('Введите числа\n')))
print(a)
for i in range(10):
	if a[i] % 2 != 0:
		b.append(a[i])
if b == []:
	print('Нечётных чисел нет')
else:
	b.sort(reverse=True)
	print(b)