import math
x = 0

n = int(input("Введите n "))
for i in range(1, n+1):
    x = x + pow(i, 3)
print(x)