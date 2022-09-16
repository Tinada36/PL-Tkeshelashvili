import math
from tkinter import Y

x = float(input("Введите x "))
y = float(input("Введите y "))
z = float(input("Введите z "))
s = (math.pow((y + (math.pow((x - 1), 1./3))), 1./4))/(math.fabs(x - y) * (math.pow(math.sin(z), 2) + math.tan(z)))
print("s= {0:.6f}".format(s))