a = input("Введите строку с точкой ")
b = 0

for i in range(len(a)):
    if a[i] == " ":
        b += 1
print("В этой строке", b+1, "слов")