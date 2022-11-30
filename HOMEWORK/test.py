import tkinter as tk

def click():
    lablebutton = tk.Label(window, text=e.get())
    lablebutton.grid(row=1, column=1)

window = tk.Tk()
window.title("My first GUI")
window.geometry("500x500")

menutab = tk.Menu(window)
window.config(menu=menutab)

operation = tk.Menu(menutab, tearoff=0)
menutab.add_cascade(label="Operation", menu=operation)
operation.add_command(label="Add")
operation.add_command(label="Subtract")
operation.add_command(label="Multiply")

lablebutton = tk.Label(window, text="")

dropdown = tk.StringVar(window)
dropdown.set("Select a number")

nums = tk.OptionMenu(window, dropdown, "1", "2", "3", "4", "5")
nums.grid(row=2, column=0)

e = tk.Entry(window, width=50)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button = tk.Button(window, text="Click Me", padx=10, pady=10, command=click)
button.grid(row=1, column=0)
window.mainloop()