#13 Вариант

import math

#1 номер

m = int(input('Введите кол-во строк '))
n = int(input('Введите кол-во столбцов '))

a = []

for i in range(m):
	b = []
	for k in range(n):
		print('Введите [',i,',',k,'] элемент')
		b.append(int(input()))
	a.append(b)
for i in range(m):
	for k in range(n):
		print(a[i][k], end=' ')
	print()
for i in range(m):
	if i % 2 != 0:
		mmin = min(a[i])
		print('min элемент чётных строк', mmin)

#2 номер

m = int(input('Введите кол-во строк '))
n = int(input('Введите кол-во столбцов '))

a = []

for i in range(m):
	b = []
	for k in range(n):
		print('Введите [',i,',',k,'] элемент')
		b.append(int(input()))
	a.append(b)
def vivod(a):
	for i in range(m):
		for k in range(n):
			print(a[i][k], end=' ')
		print()
	print()
vivod(a)
minn = float('inf')
maxx = float('-inf')
for i in range(m):
	for k in range(n):
		if a[i][k] < minn:
			minn = a[i][k]
	for j in range(n):
		if a[i][j] > maxx:
			maxx = a[i][j]
for i in range(m):
	for k in range(n):
		if a[i][k] == maxx:
			a[i][k] = minn
		elif a[i][k] == minn:
			a[i][k] = maxx
print('min=', minn, 'max=', maxx)
vivod(a)