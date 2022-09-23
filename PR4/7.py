x = 1
n = int(input("Введите n "))
s = 0

for i in range(1, n+1):
    x = x * i
    s = s + x
print("Сумма факториалов равна ", s)