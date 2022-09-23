from calendar import c


D = int(input("Введите кол-во чисел "))
A = int()
C = 0

while A != D:
    B = int(input("Введите целое число "))
    A += 1
    C += B
print(C)