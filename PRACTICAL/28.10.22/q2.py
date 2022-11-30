from tkinter import *

def thbtousd():
    thb = float(e.get())
    usd = thb / 30
    
    newwindow = Toplevel(window)
    newwindow.title("THB -> USD")
    
    text = "{:2f} THB = {:2f} USD".format(thb, usd)
    lable = Label(newwindow, text=text)
    lable.pack()
    
    exitbutton = Button(newwindow, text="OK", command=newwindow.destroy)
    exitbutton.pack()
    
def usdtothb():
    usd = float(e.get())
    thb = usd * 30
    
    newwindow = Toplevel(window)
    newwindow.title("USD -> THB")
    
    text = "{:.2f} USD = {:.2f} THB".format(usd, thb)
    lable = Label(newwindow, text=text)
    lable.pack()
    
    exitbutton = Button(newwindow, text="OK", command=newwindow.destroy)
    exitbutton.pack()

window = Tk()
window.title("Currency converter")


e = Entry(window, width=50)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

Thbtousd = Button(window, text="THB -> USD", width=50, padx=10, pady=10, command=lambda: thbtousd())
Thbtousd.grid(row=1, column=0, columnspan=3)

Usdtothb = Button(window, text="USD -> THB", width=50, padx=10, pady=10, command=lambda: usdtothb())
Usdtothb.grid(row=2, column=0, columnspan=3)

window.mainloop()