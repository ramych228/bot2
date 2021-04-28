import tkinter as tk
import time
from tkinter import *
import random
x = 0
d = [0] * 101
XY = []
def sel():
    selection = "Кол-во = " + str((var.get()))
    label.config(text = selection)
    x = int(var.get())
    for i in range(x):
        x11 = random.random() * 850 
        y11 = random.random() * 500 
        r = random.random() * 100
        XY.append([x11 + (r), y11 + (r), r])
        c.create_oval(x11, y11, x11 + r * 2, y11 + r * 2)
    button.config(state='disabled')
root = Tk()
var = DoubleVar()
scale = Scale(root, variable = var, orient = HORIZONTAL, bg="white", cursor = "dot", font = "georgia", fg = "red", troughcolor = "red")
scale.pack(anchor = CENTER)

button = Button(root, text="Кол-во окружностей", command=sel, height=1, bg="white")
button.pack(anchor = CENTER)

label = Label(root, width=10, height=1, bg="white")
label.pack(expand = 1, fill = Y)

c_1 = c_2 = -1
 
def show():
    s = f'{var1.get()}, ' \
        f'{var2.get()}'
    #lab['text'] = s
    
def show2():
   # print(var1.get(), var2.get())
    if var1.get() and var2.get() == 0:
        #button3.config(state='disabled')
        showper()
        z = 0
        qq = 700 * 1000
        
        for i in range(len(d)):
            if d[i] != 0:
                z = i
        lab['text'] = "Максимальное количество \n пересечений:",z, "\n", "Площадь пересечения:", (sum(d) - d[1]) / 1000, "%", "\n", "Площадь объединения:", (sum(d)) / 1000, "%"
        #lab['text'] = "hooray"
    elif not var1.get() and var2.get() == 1:
        check()
        z = 0
        qq = 700 * 1000
        
        for i in range(len(d)):
            if d[i] != 0:
                z = i
        lab['text'] = "Максимальное количество \n пересечений:",z, "\n", "Площадь пересечения:", (sum(d) - d[1]) / 1000, "%", "\n", "Площадь объединения:", (sum(d)) / 1000, "%"
       # lab['text'] = "hooray2"
    elif var1.get() and var2.get() == 1:
        lab['text'] = "Выберите что-то одно"
    else:
        lab['text'] = "Выберите что-то"

def check():
   # d = [0] * 101
    ans = 0
    lab['text'] = "aaa"
    for i in range(100000):
        lab['text'] = str(i)
        z = random.random() * 1000
        w = random.random() * 700 
        res = 0
        for [x1, y1, r1] in XY:
            if(((z - x1) * (z - x1) + (w - y1) * (w - y1)) < r1 * r1):
                #print(x1, y1, r1, z, w)
                res += 1
        d[res] += 1
        if res >= 8:
            c.create_line(z, w, z+1, w, fill="orange")
        elif res >= 7:
            c.create_line(z, w, z+1, w, fill="yellow")
        elif res >= 6:
            c.create_line(z, w, z+1, w, fill="lightblue")
        elif res >= 5:
            c.create_line(z, w, z+1, w, fill="purple")
        elif res >= 4:
            c.create_line(z, w, z+1, w, fill="blue")
        elif res >= 3:
            c.create_line(z, w, z+1, w, fill="green")
        elif res >= 2:
            c.create_line(z, w, z+1, w, fill="red")
    d[0] = 0
def showper():
    ans = 0
    lab['text'] = "aaa"
    for i in range(100000):
        lab['text'] = str(i)
        z = random.random() * 1000
        w = random.random() * 700 
        res = 0
        for [x1, y1, r1] in XY:
            if(((z - x1) * (z - x1) + (w - y1) * (w - y1)) < r1 * r1):
                #print(x1, y1, r1, z, w)
                res += 1
        d[res] += 1
        if res == 1:
            c.create_line(z, w, z+1, w, fill="black")
frame = Frame()
frame.pack(side=LEFT)
 
var1 = BooleanVar()
var1.set(0)
c1 = Checkbutton(frame, text="Объединение",
                 variable=var1,
                 onvalue=1, offvalue=0,
                 command=show)
c1.pack(anchor=W, padx=10)
 
var2 = IntVar()
var2.set(-1)
c2 = Checkbutton(frame, text="Пересечение",
                 variable=var2,
                 onvalue=1, offvalue=0,
                 command=show)
c2.pack(anchor=W, padx=10)
 
lab = Label(width=25, height=5, bg="lightblue")
lab.pack(side=RIGHT)

button3 = Button(root, text="Подтвердить", command=show2, height=1, bg="white")
button3.pack(anchor = W, padx = 10)




c = Canvas(width = 1000, height = 700, bg = "white")


c.pack()




