# 10 вариант

# 1 номер
from random import randint

print('На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных из цифр а, b, с.')

def poisk(N):
    schet = 0
    b = []
    arr = [i for i in range(0, 10)]
    for i in arr:
        for k in arr:
            for s in arr:
                if s!=k and k!=i and s!= i:
                    z = s*100 + k * 10 + i
                    if z >= 100 and z < N:
                        schet += 1
    return schet
N = int(input('Введите 210 < N < 231 '))
while N < 210 or N > 231:
    print('Вы ввели неверное значение, попробуйте ещё раз')
    N = int(input())
print(poisk(N))

#2 номер
print('Составить программу, которая изменяет последовательность слов в строке на обратную.')
def razvorot(a):
    b = list(reversed(a.split(" ")))
    return b
c = input('Введите строку ')
print(razvorot(c))