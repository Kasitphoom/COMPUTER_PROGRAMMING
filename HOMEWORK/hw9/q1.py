from tkinter import *

called = False

def addnmbr(n):
    global teltext
    global called
    
    if called:
        teltext.set("")
        called = False

    temp = teltext.get() + n
    teltext.set(temp)
    
    
def delete():
    global teltext
    global called
    
    if called:
        teltext.set("")
        called = False

    temp = teltext.get()
    temp = temp[:-1]
    teltext.set(temp)
    
def call():
    global teltext
    global called
    
    teltext.set("Dailing <<" + teltext.get() + ">>")
    called = True

window = Tk()
window.title("KMITL Phone")

teltext = StringVar()

textout = Entry(window, width=50, bg="white", state="disable", textvariable=teltext)
textout.grid(row=0, column=0, columnspan=3,padx=5, pady=10, sticky=W)

one = Button(window, text="1", width=10, command=lambda: addnmbr("1")).grid(row=1, column=0, pady=10, sticky=W)
two = Button(window, text="2", width=10, command=lambda: addnmbr("2")).grid(row=1, column=1, pady=10, sticky=W)
three = Button(window, text="3", width=10, command=lambda: addnmbr("3")).grid(row=1, column=2, pady=10, sticky=W)
four = Button(window, text="4", width=10, command=lambda: addnmbr("4")).grid(row=2, column=0, pady=10, sticky=W)
five = Button(window, text="5", width=10, command=lambda: addnmbr("5")).grid(row=2, column=1, pady=10, sticky=W)
six = Button(window, text="6", width=10, command=lambda: addnmbr("6")).grid(row=2, column=2, pady=10, sticky=W)
seven = Button(window, text="7", width=10, command=lambda: addnmbr("7")).grid(row=3, column=0, pady=10, sticky=W)
eight = Button(window, text="8", width=10, command=lambda: addnmbr("8")).grid(row=3, column=1, pady=10, sticky=W)
nine = Button(window, text="9", width=10, command=lambda: addnmbr("9")).grid(row=3, column=2, pady=10, sticky=W)
star = Button(window, text="*", width=10, command=lambda: addnmbr("*")).grid(row=4, column=0, pady=10, sticky=W)
zero = Button(window, text="0", width=10, command=lambda: addnmbr("0")).grid(row=4, column=1, pady=10, sticky=W)
square = Button(window, text="#", width=10, command=lambda: addnmbr("#")).grid(row=4, column=2, pady=10, sticky=W)

talk = Button(window, text="Talk", width=10, command=lambda: call()).grid(row=5, column=0, pady=10, sticky=W)
delt = Button(window, text="<", width=10, command=lambda: delete()).grid(row=5, column=1, pady=10, sticky=W)


window.mainloop()