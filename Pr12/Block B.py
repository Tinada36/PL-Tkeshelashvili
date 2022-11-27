# номер 1

print('Вводим последовательность натуральных чисел (одно число в строке), завершающаяся числом 0 ')
def func():
    a = int(input('Введите число a: '))
    if a == 0:
        return 0
    else:
        return max(a, func())
print(func())