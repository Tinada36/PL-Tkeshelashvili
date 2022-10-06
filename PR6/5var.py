# 5 вариант

#1
a = []
b = []
for i in range(10):
	a.append(int(input('Введите числа\n')))
	print(a)
for i in range(10):
	if a[i]<0:
		b.append(a[i])
		b.sort()
print(b)

#2
c = []
for i in range(10):
	c.append(int(input('Введите числа\n')))
print(c)
for i in reversed(range(len(c)-1)):
	if c[i] in c[i+1:]:
		c.pop(i)
print(c)