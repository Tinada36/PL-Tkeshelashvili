N = int(input("Введите кол-во чисел для ряда Фибоначчи "))
A = 0
B = 0
C = 1
E = 0

if N == 1:
    print(0)
elif N == 0:
    print("Введите количество!!!")
else:
    while A != N-2:
        if A == N-2:
            break
        else:
            D = B + C
            E += D
            A += 1
        if A == N-2:
            break
        else:
            B = C + D
            E += B
            A += 1
        if A == N-2:
            break
        else:
            C = D + B
            E += C
            A += 1
    print(E+1)