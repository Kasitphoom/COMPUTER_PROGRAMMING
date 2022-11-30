from tkinter import *

window = Tk()
global n
n = 0


def add():
    global n
    n += 1
    number = Label(window, text=n)
    number.grid(row=0, column=0, rowspan=3)

def subtract():
    global n
    n -= 1
    number = Label(window, text=n)
    number.grid(row=0, column=0, rowspan=3)

def reset():
    global n
    n = 0
    number = Label(window, text=n)
    number.grid(row=0, column=0, rowspan=3)

number = Label(window, text=n)
number.grid(row=0, column=0, rowspan=3)

addbtn = Button(window, text="+", padx=20, command=lambda: add())
addbtn.grid(row=0, column=1)
subbtn = Button(window, text="-", padx=20, command=lambda: subtract())
subbtn.grid(row=1, column=1)
resbtn = Button(window, text="Reset", padx=20, command=lambda: reset())
resbtn.grid(row=2, column=1)


window.mainloop()