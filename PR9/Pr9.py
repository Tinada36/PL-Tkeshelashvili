with open('PR9\TkeshelashviliVR_ub22_vvod.txt', 'r+') as f:
	line = f.readlines()
	l = [element.replace ("\n", "").split() for element in line]
import math
n = len(l)
m = len(l[0])
a = l
for i in range(n):
	for k in range(m):
		a[i][k] = int(a[i][k])
	print()
k = 0
s = 0
for i in range(n):
	for j in range(n):
		if i < j:
			s = s + a[i][j]
			if a[i][j] > 0:
				k += 1
"""print('Сумма элементов над главной диагональю: ', s)
print('Кол-во положительных элементов', k)"""
with open('PR9\TkeshelashviliVR_ub22_vivod.txt', 'w', encoding='utf-8-sig') as f2:
	for i in range(n):
		for j in range(n):
			f2.write(str(a[i][j]))
			f2.write(' ')
		f2.write('\n')
	f2.write('Сумма элементов над главной диагональю: ')
	f2.write(str(s))
	f2.write('\n')
	f2.write('Кол-во положительных элементов: ')
	f2.write(str(k))
	f2.write('\n')
for i in range(n):
	for j in range(m):
		b = a[i].index(min(a[i]))
		tmp1 = a[i][0]
		a[i][0] = a[i][b]
		a[i][b] = tmp1
for i in range(n):
	for j in range(m):
		max_b = max(a[i])
		c = a[i].index(max(a[i]))
		tmp2 = a[i][m-1]
		a[i][m-1] = a[i][c]
		a[i][c] = tmp2
with open('PR9\TkeshelashviliVR_ub22_vivod.txt', 'a+', encoding='utf-8-sig') as f2:
	f2.write('Найти в каждой строке матрицы максимальный и минимальный элементы и поменять их с первым и последним элементами строки соответственно.')
	f2.write('\n')
	for i in range(n):
		for k in range(n):
			f2.write(str(a[i][k]))
			f2.write(' ')
		f2.write('\n')
for i in range(m):
	if i % 2 != 0:
		mmin = min(a[i])
		"""print('min элемент чётных строк', mmin)"""
with open('PR9\TkeshelashviliVR_ub22_vivod.txt', 'a+', encoding='utf-8-sig') as f2:
	f2.write('min элемент чётных строк')
	f2.write('\n')
	f2.write(str(mmin))
	f2.write('\n')
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
with open('PR9\TkeshelashviliVR_ub22_vivod.txt', 'a+', encoding='utf-8-sig') as f2:
	f2.write('min=')
	f2.write(str(minn))
	f2.write('\n')
	f2.write('max=')
	f2.write(str(maxx))
	f2.write('\n')
	for i in range(n):
		for k in range(n):
			f2.write(str(a[i][k]))
			f2.write(' ')
		f2.write('\n')