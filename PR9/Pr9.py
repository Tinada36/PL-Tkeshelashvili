with open('PR9\TVR_ub22_vvod.txt', 'r') as f:
	line = f.readlines()
	l = [element.replace ("\n", "").split() for element in line]
n = len(l)
a = l
for i in range(n):
	for k in range(n):
		a[i][k] = int(a[i][k])
for i in range(n):
	for k in range(n):
		print(a[i][k], end=' ')
	print()
k = 0
s = 0
for i in range(n):
	for j in range(n):
		if i < j:
			s = s + a[i][j]
			if a[i][j] > 0:
				k += 1
print('Сумма элементов над главной диагональю: ', s)
print('Кол-во положительных элементов', k)
with open('PR9\TVR_ub22_vivod.txt', 'w', encoding='utf-8-sig') as f2:
	for i in range(n):
		for k in range(n):
			f2.write(str(a[i][k]))
			f2.write(' ')
		f2.write('\n')
	f2.write('Сумма элементов над главной диагональю: ')
	f2.write(str(s))
	f2.write('\n')
	f2.write('Кол-во положительных элементов: ')
	f2.write(str(k))