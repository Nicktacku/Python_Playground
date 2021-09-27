from tkinter import *

root = Tk()
root.title("Basic Calculator")

title = Label(root, text="Calculator")
title.grid(row=0, column=0)

seperate = Label(root, text=" ")
seperate.grid(row=1, column=0)

def add_num():
    added = float(a1.get()) + float(a2.get())
    label = Label(root, text=added)
    label.grid(row=6, column=0)

add_title = Label(root, text="Add 2 numbers")
add_title.grid(row=2, column=0)

a1 = Entry(root, width=10, borderwidth=5)
a1.grid(row=3, column=0)
a2 = Entry(root, width=10, borderwidth=5)
a2.grid(row=4, column=0)

add_button = Button(root, command=add_num, text="Add", fg="white", bg="black")
add_button.grid(row=5, column=0)

space = Label(root, text=" ")
space.grid(row=7, column=0)


def subtract_num():
    subtracted = float(s1.get()) - float(s2.get())
    label = Label(root, text=subtracted)
    label.grid(row=12, column=0)

subtract_title = Label(root, text="Subtract 2 numbers")
subtract_title.grid(row=8, column=0)

s1 = Entry(root, width=10, borderwidth=5)
s1.grid(row=9, column=0)
s2 = Entry(root, width=10, borderwidth=5)
s2.grid(row=10, column=0)

subtract_button = Button(root, command=subtract_num, text="Subtract", fg="white", bg="black")
subtract_button.grid(row=11, column=0)

space1 = Label(root, text=" ")
space1.grid(row=13, column=0)

def multiply_num():
    multiplied = float(m1.get()) * float(m2.get())
    label = Label(root, text=multiplied)
    label.grid(row=18, column=0)

multiply_title = Label(root, text="Multiply 2 numbers")
multiply_title.grid(row=14, column=0)

m1 = Entry(root, width=10, borderwidth=5)
m1.grid(row=15, column=0)
m2 = Entry(root, width=10, borderwidth=5)
m2.grid(row=16, column=0)


multiply_button = Button(root, command=multiply_num, text="Multiply", fg="white", bg="black")
multiply_button.grid(row=17, column=0)

space3 = Label(root, text=" ")
space3.grid(row=19, column=0)

def divide_num():
    divided = float(d1.get()) / float(d2.get())
    label = Label(root, text=divided)
    label.grid(row=24, column=0)

divide_title = Label(root, text="Divide 2 numbers")
divide_title.grid(row=20, column=0)

d1 = Entry(root, width=10, borderwidth=5)
d1.grid(row=21, column=0)
d2 = Entry(root, width=10, borderwidth=5)
d2.grid(row=22, column=0)


divide_button = Button(root, command=divide_num, text="Divide", fg="white", bg="black")
divide_button.grid(row=23, column=0)


root.mainloop()
