import math

a = int(input("Введите а "))
x = int(input("Введите х "))
if  a > 5 and x == 3:
	y = x + a
	print(y)
elif a == 4 or x < 2:
	y = x * a
	print(y)
else:
	y = math.pow(x, a)
	print(y)

f = int(input("Введите f "))
k = int(input("Введите k "))
if f < 5 and k > 2:
	R = f + k - 1
	print(R)
elif k < 2:
	R = k*k
	print(R)
elif k == 2:
	R = 1
	print(R)

b = int(input("Введите b "))
if a < b:
	C = a + b
	print(C)
elif a > b and a > 3:
	C = b*b-b
	print(C)
else:
	C = b*b-1
	print(C)