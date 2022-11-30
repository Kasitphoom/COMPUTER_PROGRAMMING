import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Robot omni-wheels Soccer Simulation")
window.geometry("1200x800")
window.resizable(False, False)

class Field:
    def __init__(self, window):
        self.window = window
        self.field = tk.Frame(self.window, width=448, height=782)
        self.field.pack(side="left", fill="both", padx=10, pady=10)
        self.field.grid_rowconfigure(0, weight=1)
        self.field.grid_columnconfigure(0, weight=1)
        
        self.canvas = tk.Canvas(self.field, width=448, height=782, bg="#0D8F03")
        
        # create border
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_rectangle(20, 20, 428, 762, outline="white", width=4)
        
        # create center circle
        self.canvas.create_oval(134, 301, 314, 481, outline="black", width=4)
        
        # create center point
        self.canvas.create_oval(222, 389, 226, 393, outline="black", width=4)
        
        # create enemy goal
        self.canvas.create_rectangle(147, 0, 301, 50, outline="", fill="#FF0000", width=4)
        
        # create player goal
        self.canvas.create_rectangle(147, 732, 301, 782, outline="", fill="#0000FF", width=4)
        self.field.tkraise()
        
    def getcanvas(self):
        return self.canvas
        

class Controller:
    def __init__(self, window):
        self.window = window
        self.controller = tk.Frame(self.window, width=700, height=782)
        self.controller.pack(side="bottom", fill="both", padx=10, pady=10)
        self.controller.grid_rowconfigure(0, weight=1)
        self.controller.grid_columnconfigure(1, weight=1)
        
        self.start = tk.Button(self.controller, text="Start Simulation", width=10, height=2, padx=20, pady=5, bg="#00B82B", font=("bahnschrift", 12), fg="white")
        self.start.grid(row=0, column=0, padx=10, pady=10)
        
        self.pause = tk.Button(self.controller, text="Pause Simulation", width=10, height=2, padx=20, pady=5, bg="#C5B90A", font=("bahnschrift", 12), fg="white")
        self.pause.grid(row=0, column=1, padx=10, pady=10)
        
        self.stop = tk.Button(self.controller, text="Stop Simulation", width=10, height=2, padx=20, pady=5, bg="#B80000", font=("bahnschrift", 12), fg="white")
        self.stop.grid(row=0, column=2, padx=10, pady=10)
        
        

field = Field(window)
controller = Controller(window)
window.mainloop()