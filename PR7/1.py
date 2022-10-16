# 1 вариант

# 1 номер
def fig(a,b,h):
	s1= 1/2 * a * h
	print('Площадь треугольника равна ', s1)
	s2 = a*a
	print ('Площадь квадрата равна ', s2)
	s3 = (a+b)/2 * h
	print ('Площадь трапеции равна ', s3)
	return s1, s2, s3
x = int(input('Введите сторону а:'))
y = int(input('Введите сторону y:'))
z = int(input('Введите сторону z:'))
print(fig(x,y,z))

# 2 номер
def zam(x):
	appa = 0
	for i in range(5):
		appa += x[i]
	print('Сумма элементов', appa)
	appa = appa/5
	print('Среднеарифметичсекое ', appa)
	return appa
def spam(y):
	appa = 0
	for i in range(5):
		appa += y[i]
	print('Сумма элементов', appa)
	appa = appa/5
	print('Среднеарифметичсекое ', appa)
	return appa
def cam(z):
	appa = 0
	for i in range(5):
		appa += z[i]
	print('Сумма элементов', appa)
	appa = appa/5
	print('Среднеарифметичсекое ', appa)
	return appa
A = []
for i in range(5):
	A.append(int(input('Введите элемент массива A ')))
B = []
for i in range(5):
	B.append(int(input('Введите элемент массива B ')))
C = []
for i in range(5):
	C.append(int(input('Введите элемент массива C ')))
print(zam(A))
print(spam(B))
print(cam(C))