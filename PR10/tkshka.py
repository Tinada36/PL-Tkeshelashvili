from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Checkbutton

def otkrit():
    file = filedialog.askopenfilename()

def knopka():
    if chk1.instate(['selected']) == True:
        lbl.configure(text="Вы выбрали первый вариант", font=("Times New Roman", 16))
    elif chk2.instate(['selected']) == True:
        lbl.configure(text="Вы выбрали второй вариант", font=("Times New Roman", 16))
    elif chk3.instate(['selected']) == True:
        lbl.configure(text="Вы выбрали третий вариант", font=("Times New Roman", 16))
    else:
        lbl.configure(text="Вы ничего не выбрали :(", font=("Times New Roman", 16))

window = Tk()
window.title("Tkeshelashvili VR")
window.geometry('720x600')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Первая")
tab_control.add(tab2, text="Вторая")
tab_control.add(tab3, text="Третья")
lbl = Label(tab2)
lbl.grid(column=2, row=1)

chk_state = BooleanVar()
chk_state1 = BooleanVar()
chk_state2 = BooleanVar()
chk1 = Checkbutton(tab2, text="Первый", var=chk_state)
chk2 = Checkbutton(tab2, text="Второй", var=chk_state1)
chk3 = Checkbutton(tab2, text="Третий", var=chk_state2)
chk1.grid(column=0, row=0)
chk2.grid(column=0, row=1)
chk3.grid(column=0, row=2)

btn = Button(tab2, text="нажми!", command=knopka)
btn.grid(column=1, row=1)

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label="Открыть", command=otkrit)
new_item.add_separator()
menu.add_cascade(label="Файл", menu=new_item)
window.config(menu=menu)

tab_control.pack(expand=1, fill="both")
window.mainloop()