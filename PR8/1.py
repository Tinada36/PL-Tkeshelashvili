# 1 вариант

#1 номер
N = int(input('Введите размер матрицы '))
a = []
for i in range(N):
	b = []
	for j in range(N):
		print('Введите [',i,',',j,'] элемент')
		b.append(int(input()))
	a.append(b)
print('Исходный массив:')
for i in range(N):
	for j in range(N):
		print(a[i][j], end=' ')
	print()
k = 0
s = 0
for i in range(N):
	for j in range(N):
		if i < j:
			s = s + a[i][j]
			if a[i][j] > 0:
				k += 1
print('Сумма элементов над главной диагональю: ', s)
print('Кол-во положительных элементов', k)

#2 номер
n = int(input('Введите кол-во строк '))
m = int(input('Введите кол-во столбцов '))
B = []
for i in range(n):
	b = []
	for j in range(m):
		print('Введите [',i,',',j,'] элемент')
		b.append(int(input()))
	B.append(b)
print('Исходный массив:')
for i in range(n):
	for k in range(m):
		print(B[i][k], end=' ')
	print()
for i in range(n):
	for j in range(m):
		min_b = min(B[i])
		a = B[i].index(min(B[i]))
	tmp1 = B[i][0]
	B[i][0] = B[i][a]
	B[i][a] = tmp1
for i in range(n):
	for j in range(m):
		max_b = max(B[i])
		b = B[i].index(max(B[i]))
	tmp2 = B[i][m-1]
	B[i][m-1] = B[i][b]
	B[i][b] = tmp2
print(B)