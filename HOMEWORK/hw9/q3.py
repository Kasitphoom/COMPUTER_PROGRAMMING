from tkinter import *

window = Tk()

def add_circle(event):
    canvas.create_oval(event.x-10, event.y-10, event.x+10, event.y+10, fill="")

def delete_circle(event):
    for i in canvas.find_overlapping(event.x-5, event.y-5, event.x+5, event.y+5):
        canvas.delete(i)
    

window.title("Click-remove circles")
window.geometry("600x400")
window.resizable(False, False)

canvas = Canvas(window, width=600, height=400, bg="white")
canvas.grid(row=0, column=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", add_circle)

canvas.bind("<Button-3>", delete_circle)


window.mainloop()