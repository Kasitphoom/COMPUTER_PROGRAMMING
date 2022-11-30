from tkinter import *
import random
    
def addLine(event):
    # random color
    r = lambda: random.randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())
    if event.x not in range(25, 365) or event.y not in range(25, 215):
        newwindow = Toplevel(window)
        newwindow.title("WARNING")
        
        text = "Mouse pointer is not in the rectangle"
        lable = Label(newwindow, text=text)
        lable.pack()
        
        exitbutton = Button(newwindow, text="OK", command=newwindow.destroy)
        exitbutton.pack()
    else:   
        canvas.create_oval(event.x - 5, event.y + 5, event.x + 5, event.y - 5, fill=color)

window = Tk()
window.title("Draw inside rectangle")

canvas = Canvas(window, width=500, height=500)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

canvas.create_rectangle(20,20,370,220)
canvas.bind("<Button-1>", addLine)

window.mainloop()