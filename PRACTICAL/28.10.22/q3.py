from tkinter import *

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y
    
def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y
    
    

window = Tk()
window.title("Draw on canvas")

canvas = Canvas(window, width=500, height=500)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)


clear = Button(window, text="Clear", command=lambda: canvas.delete("all"))
clear.grid(column=0, row=1)

window.mainloop()