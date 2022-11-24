def func(x, n):
    if n == 1:
        return x
    else:
        return(x * func(x, n-1) / n)

x = int(input('Введите х: '))
n = int(input('Введите n: '))
print(func(x, n))