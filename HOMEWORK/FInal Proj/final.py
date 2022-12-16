import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import pickle
import numpy as np
import math
import time
import random

window = tk.Tk()
window.title("Robot omni-wheels Soccer Simulation")
window.geometry("1200x800")
window.resizable(False, False)

menu = tk.Menu(window)
filemenu = tk.Menu(menu, tearoff=0)
filemenu.add_command(label="Save Preferences", command= lambda: SavePreferences())
filemenu.add_command(label="Load Preferences", command= lambda: LoadPreferences())
filemenu.add_separator()
filemenu.add_command(label="Exit (No log saved)", command=window.quit)
menu.add_cascade(label="File", menu=filemenu)

logmenu = tk.Menu(menu, tearoff=0)
logmenu.add_command(label="Show log folder", command= lambda: ShowLogFolder())
menu.add_cascade(label="Log", menu=logmenu)

window.config(menu=menu)


ROBOT_WEIGHT = 1100
BALL_WEIGHT = 46

class IncrementPositiveError(Exception):
    pass

class IncrementValueError(Exception):
    pass

class IncrementStepError(Exception):
    pass

class ArgumentLengthError(Exception):
    pass

def checklength(arguments, length):
    if len(arguments) != length:
        raise ArgumentLengthError("Arguments must be of length {}".format(length))

def checkIncrement(increment):
    try:
        increment = float(increment)
    except ValueError:
        raise IncrementValueError("Increment must be a number")
    
    
    if increment <= 0:
        raise IncrementPositiveError("Increment must be positive")
    elif increment < 0.001:
        raise IncrementStepError("Increment must be greater than 0.001")
    
def checknegative(number):
    if number < 0:
        raise ValueError("Number must be positive")
    
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
        self.enemygoal = self.canvas.create_rectangle(147, 0, 301, 50, outline="", fill="#FF0000", width=4)
        
        # create player goal
        self.ourgoal = self.canvas.create_rectangle(147, 732, 301, 782, outline="", fill="#0000FF", width=4)
        self.field.tkraise()
        
    def getcanvas(self):
        return self.canvas
    
    def getsize(self):
        self.window.update()
        return self.canvas.winfo_width(), self.canvas.winfo_height()

    def getgoals(self):
        return self.ourgoal, self.enemygoal
        
class InfoScreen:
    def __init__(self, window):
        self.window = window
        self.screen = tk.Frame(self.window)
        self.screen.pack(side="right", fill="both", expand="true", padx=10, pady=10)
    
    def getframe(self):
        return self.screen
    
class Controller(InfoScreen):
    def __init__(self, window, frame):
        super().__init__(window)
        self.frame = frame
        self.controller = tk.Frame(self.frame, width=700)
        self.controller.pack(side="top", fill="both", padx=10, pady=10)
        self.controller.grid_rowconfigure(0, weight=1)
        self.controller.grid_columnconfigure(1, weight=1)
        
        self.start = tk.Button(self.controller, text="Start Simulation", width=10, height=2, padx=20, pady=5, bg="#00B82B", font=("bahnschrift", 12), fg="white", command= lambda: StartSim())
        self.start.grid(row=1, column=0, padx=10, pady=10)
        
        self.pause = tk.Button(self.controller, text="Pause Simulation", width=10, height=2, padx=20, pady=5, bg="#C5B90A", font=("bahnschrift", 12), fg="white", command= lambda: PauseSim())
        self.pause.grid(row=1, column=1, padx=10, pady=10)
        
        self.stop = tk.Button(self.controller, text="Stop Simulation", width=10, height=2, padx=20, pady=5, bg="#B80000", font=("bahnschrift", 12), fg="white", command= lambda: StopSim())
        self.stop.grid(row=1, column=2, padx=10, pady=10)
        
    def getframe(self):
        return self.controller
    
    def changePausebutton(self, text):
        newtext = "{} Simulation".format(text)
        self.pause.config(text=newtext, bg="#00B82B" if text == "Resume" else "#C5B90A", command= lambda: ResumeSim() if text == "Resume" else PauseSim())
        

class GameInformation(InfoScreen):
    def __init__(self, window, frame):
        super().__init__(window)
        self.frame = frame
        self.currenttime = 0
        self.ourscore = 0
        self.enemyscore = 0
        self.formattedtime = tk.StringVar()
        self.formattedtime.set("00:00")
        
        self.formattedscore = tk.StringVar()
        self.formattedscore.set("0 - 0")
        
        self.infoframe = tk.Frame(self.frame, width=700, height=100)
        self.infoframe.pack(side="top", fill="both", padx=10, pady=10)
        
        self.scoreframe = tk.Frame(self.infoframe)
        self.scorelabel = tk.Label(self.scoreframe, text="Score: ", font=("bahnschrift", 12))
        self.scorelabel.pack(side="left", padx=10, pady=10)
        self.currentscore = tk.Label(self.scoreframe, textvariable=self.formattedscore, font=("bahnschrift", 40))
        self.currentscore.pack(side="left", padx=10, pady=10)
        
        self.timeframe = tk.Frame(self.infoframe)
        self.timelabel = tk.Label(self.timeframe, text="Time: ", font=("bahnschrift", 12))
        self.timelabel.pack(side="left", padx=10, pady=10)
        self.time = tk.Label(self.timeframe, textvariable=self.formattedtime, font=("bahnschrift", 40))
        self.time.pack(side="left", padx=10, pady=10)
        
        self.scoreframe.grid(row=0, column=0, sticky="w")
        self.window.update()
        self.timeframe.grid(row=0, column=1, padx=self.scoreframe.winfo_width(), sticky="e")
        
        self.horizontal = ttk.Separator(self.infoframe, orient="horizontal")
        self.horizontal.grid(row=1, column=0, columnspan=2, sticky="ew")
    
    def starttimer(self, time):
        self.currenttime = time
        self.time = int(self.currenttime - self.initialtime)
        
        self.formattedtime.set("{:02d}:{:02d}".format(self.time // 60, self.time % 60))
    
    def setinitialtime(self, initial_time):
        self.initialtime = initial_time
    
    def setscore(self, ourscore, enemyscore):
        self.ourscore = ourscore
        self.enemyscore = enemyscore
        self.formattedscore.set("{} - {}".format(self.ourscore, self.enemyscore))
    
    def reset(self):
        self.formattedtime.set("00:00")
        self.formattedscore.set("0 - 0")
        
    def getscores(self):
        return "{} - {}".format(self.ourscore, self.enemyscore)
    
    def gettimeelapsed(self):
        return self.formattedtime.get()
        
class FieldInfo(InfoScreen):
    def __init__(self, window, frame):
        super().__init__(window)
        self.frame = frame
        self.frictionval = tk.StringVar()
        self.frictionval.set(0.01)
        self.fieldinfoframe = tk.Frame(self.frame)
        self.fieldinfoframe.pack(side="top", fill="both", padx=10)
        
        self.fieldInfoTitle = tk.Label(self.fieldinfoframe, text="Field Settings", font=("bahnschrift", 20))
        self.fieldInfoTitle.pack(side="top", padx=10, pady=10)
        
        self.infoframe = tk.Frame(self.fieldinfoframe)
        
        self.frictioninfoframe = tk.Frame(self.infoframe)
        self.frictionlabel = tk.Label(self.frictioninfoframe, text="Current Field Friction: ", font=("bahnschrift", 12))
        self.frictionlabel.grid(row=0, column=0, padx=10, pady=10,sticky="w")
        self.friction = tk.Label(self.frictioninfoframe, textvariable=self.frictionval, font=("bahnschrift", 16))
        self.friction.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.frictioninfoframe.grid(row=0, column=0, sticky="w")
        
        self.frictioncontrolframe = tk.Frame(self.infoframe)
        self.frictioncontrollabel = tk.Label(self.frictioncontrolframe, text="Increment: ", font=("bahnschrift", 12))
        self.frictioncontrollabel.grid(row=0, column=0, padx=2, pady=10, sticky="w")
        self.increment = tk.Entry(self.frictioncontrolframe, width=3, font=("bahnschrift", 16), justify="center")
        self.increment.grid(row=0, column=1, padx=2, pady=10, sticky="w")
        self.addincrement = tk.Button(self.frictioncontrolframe, text="+", width=2, height=1, padx=10, pady=5, bg="#00B82B", font=("bahnschrift", 12), fg="white", command=lambda: self.changeFriction(self.increment.get(), True))
        self.addincrement.grid(row=0, column=2, padx=2, pady=10, sticky="w")
        self.decreaseincrement = tk.Button(self.frictioncontrolframe, text="-", width=2, height=1, padx=10, pady=5, bg="#B80000", font=("bahnschrift", 12), fg="white", command=lambda: self.changeFriction(self.increment.get(), False))
        self.decreaseincrement.grid(row=0, column=3, padx=2, pady=10, sticky="w")
        
        self.frictioncontrolframe.grid(row=0, column=1, padx=150, sticky="w")
        
        
        self.infoframe.pack(side="top", fill="both", padx=10, pady=10)
        self.horizontal = ttk.Separator(self.fieldinfoframe, orient="horizontal")
        self.horizontal.pack(side="top", fill="both")
    
    def changeFriction(self, increment, increase):
        try:
            checkIncrement(increment)    
        except IncrementPositiveError:
            self.increment.delete(0, "end")
            self.increment.insert(0, "0.0")
            return
        except IncrementStepError:
            messagebox.showerror("Increment Error", "Increment must be more Than 0.001")
            return
        except IncrementValueError:
            messagebox.showerror("Increment Error", "Increment must be a number")
            return
        
        if increase:
            self.frictionval.set(round(float(self.frictionval.get()) + float(increment), 3))
        else:
            self.frictionval.set(round(float(self.frictionval.get()) - float(increment), 3))
    
    def getfriction(self):
        return float(self.frictionval.get())
    
    def setfriction(self, friction):
        self.frictionval.set(friction)
    
    
class RobotSettings(InfoScreen):
    def __init__(self, window, frame):
        super().__init__(window)
        self.frame = frame
        self.PIDValue = {}
        self.PIDInputs = {}
        self.showpaths = {}
        self.robotsettingsframe = tk.Frame(self.frame)
        self.robotsettingsframe.pack(side="top", fill="both", padx=10, pady=10)
        
        self.settingstitle = tk.Label(self.robotsettingsframe, text="Robot Settings", font=("bahnschrift", 20))
        self.settingstitle.pack(side="top", padx=10, pady=10)
        
        self.controlframe = tk.Frame(self.robotsettingsframe)

        self.addRobotinfo(1)
        
        self.seperator = ttk.Separator(self.controlframe, orient="vertical")
        self.seperator.pack(side="left", fill="both", padx=5)
        
        self.addRobotinfo(2)
        
        self.controlframe.pack(side="top", fill="both", padx=10, pady=10)
        
        self.horizontal = ttk.Separator(self.robotsettingsframe, orient="horizontal")
        self.horizontal.pack(side="top", fill="both")
        
        
    def addRobotinfo(self, robotID):
        self.robotID = robotID
        self.PIDValue["Kp{}".format(self.robotID)] = tk.StringVar()
        self.PIDValue["Kd{}".format(self.robotID)] = tk.StringVar()
        self.PIDValue["Ki{}".format(self.robotID)] = tk.StringVar()
        
        self.Kpval = self.PIDValue["Kp{}".format(self.robotID)]
        self.Kival = self.PIDValue["Ki{}".format(self.robotID)]
        self.Kdval = self.PIDValue["Kd{}".format(self.robotID)]
        
        self.Kpval.set(0.0)
        self.Kdval.set(0.0)
        self.Kival.set(0.0)
        
        self.robot1controlframe = tk.Frame(self.controlframe)
        label = "Robot " + str(self.robotID)
        self.robot1label = tk.Label(self.robot1controlframe, text=label, font=("bahnschrift", 16))
        self.robot1label.pack(side="top", padx=10)
        
        self.PIDframe = tk.Frame(self.robot1controlframe)
        
        # PID label
        self.PIDlabel = tk.Label(self.PIDframe, text="PID: ", font=("bahnschrift", 12))
        self.PIDlabel.grid(row=1, column=0, padx=2, pady=5, sticky="w")
        
        # Kp label and values
        self.kpframe = tk.Frame(self.PIDframe)
        self.kplabel = tk.Label(self.kpframe, text="P: ", font=("bahnschrift", 12))
        self.kplabel.grid(row=0, column=0, sticky="w")
        self.kp = tk.Label(self.kpframe, textvariable=self.Kpval, font=("bahnschrift", 16))
        self.kp.grid(row=0, column=1, pady=2, sticky="w")
        
        self.kpframe.grid(row=0, column=1, padx=2, pady=2, sticky="w")
        
        # Ki label and values
        self.kiframe = tk.Frame(self.PIDframe)
        self.kilabel = tk.Label(self.kiframe, text="I: ", font=("bahnschrift", 12))
        self.kilabel.grid(row=0, column=0, sticky="w")
        self.ki = tk.Label(self.kiframe, textvariable=self.Kival, font=("bahnschrift", 16))
        self.ki.grid(row=0, column=1, pady=2, sticky="w")
        
        self.kiframe.grid(row=0, column=2, padx=2, pady=2, sticky="w")
        
        # Kd label and values
        self.kdframe = tk.Frame(self.PIDframe)
        self.kdlabel = tk.Label(self.kdframe, text="D: ", font=("bahnschrift", 12))
        self.kdlabel.grid(row=0, column=0, sticky="w")
        self.kd = tk.Label(self.kdframe, textvariable=self.Kdval, font=("bahnschrift", 16))
        self.kd.grid(row=0, column=1, pady=2, sticky="w")
        
        self.kdframe.grid(row=0, column=3, padx=2, pady=2, sticky="w")
        
        # set value inputs
        self.PIDInputs["inputKp{}".format(self.robotID)] = tk.Entry(self.PIDframe, width=5, font=("bahnschrift", 12))
        self.PIDInputs["inputKi{}".format(self.robotID)] = tk.Entry(self.PIDframe, width=5, font=("bahnschrift", 12))
        self.PIDInputs["inputKd{}".format(self.robotID)] = tk.Entry(self.PIDframe, width=5, font=("bahnschrift", 12))
        
        self.PIDInputs["inputKp{}".format(self.robotID)].grid(row=1, column=1, padx=2, pady=2, sticky="w")
        self.PIDInputs["inputKi{}".format(self.robotID)].grid(row=1, column=2, padx=2, pady=2, sticky="w")
        self.PIDInputs["inputKd{}".format(self.robotID)].grid(row=1, column=3, padx=2, pady=2, sticky="w")
        
        # all subtract buttons
        self.setKpButton = tk.Button(self.PIDframe, text="SET", width=2, height=1, bg="#B80000", font=("bahnschrift", 12), fg="white", command = lambda: self.setKp(robotID, float(self.PIDInputs["inputKp{}".format(robotID)].get())))
        self.setKpButton.grid(row=2, column=1, ipadx=10, pady=2, sticky="w")
        self.setKiButton = tk.Button(self.PIDframe, text="SET", width=2, height=1, bg="#B80000", font=("bahnschrift", 12), fg="white", command = lambda: self.setKi(robotID, float(self.PIDInputs["inputKi{}".format(robotID)].get())))
        self.setKiButton.grid(row=2, column=2, ipadx=10, pady=2, sticky="w")
        self.setKdButton = tk.Button(self.PIDframe, text="SET", width=2, height=1, bg="#B80000", font=("bahnschrift", 12), fg="white", command= lambda: self.setKd(robotID, float(self.PIDInputs["inputKd{}".format(robotID)].get())))
        self.setKdButton.grid(row=2, column=3, ipadx=10, pady=2, sticky="w")
        
        self.PIDframe.pack(side="top", fill="both", pady=10)
        
        # options
        self.optionframe = tk.Frame(self.robot1controlframe)
        self.showoptionlabel = tk.Label(self.optionframe, text="Show Path: ", font=("bahnschrift", 12))
        
        self.showoptionlabel.grid(row=0, column=0, padx=2, pady=2, sticky="w")
        
        self.showpaths["showpath{}".format(self.robotID)] = tk.BooleanVar()
        self.showpathradio = tk.Radiobutton(self.optionframe, text="Show", variable=self.showpaths["showpath{}".format(robotID)], value=True, font=("bahnschrift", 12))
        self.showpathradio.grid(row=0, column=1, padx=2, pady=2, sticky="w")
        
        self.hidepathradio = tk.Radiobutton(self.optionframe, text="Hide", variable=self.showpaths["showpath{}".format(robotID)], value=False, font=("bahnschrift", 12))
        self.hidepathradio.select()
        self.hidepathradio.grid(row=0, column=2, padx=2, pady=2, sticky="w")
        
        self.optionframe.pack(side="top", fill="both", padx=10, pady=5)
        self.robot1controlframe.pack(side="left", fill="both", padx=35, pady=10)
    
    def setKp(self, robotID, kp):
        try:
            checknegative(kp)
        except ValueError:
            messagebox.showerror("Error", "Value must be a positive number")
            return
        
        self.PIDValue["Kp{}".format(robotID)].set(kp)
    
    def setKi(self, robotID, ki):
        try:
            checknegative(ki)
        except ValueError:
            messagebox.showerror("Error", "Value must be a positive number")
            return
        
        self.PIDValue["Ki{}".format(robotID)].set(ki)
        
    def setKd(self, robotID, kd):
        try:
            checknegative(kd)
        except ValueError:
            messagebox.showerror("Error", "Value must be a positive number")
            return
        
        self.PIDValue["Kd{}".format(robotID)].set(kd)
    
    def getpidvalues(self):
        return self.PIDValue
    
    def loadpidvalues(self, pidvalues):
        for k, v in pidvalues.items():
            self.PIDValue[k].set(float(v))
        

class SimulationSetup(InfoScreen):
    def __init__(self, window, frame):
        super().__init__(window)
        self.frame = frame
        
        self.simsetupframe = tk.Frame(self.frame)
        self.simsetupframe.pack(side="top", fill="both", padx=10)
        
        self.simsetuptitle = tk.Label(self.simsetupframe, text="Simulation Setup", font=("bahnschrift", 16))
        self.simsetuptitle.pack(side="top", fill="both", padx=10, pady=10)
        
        self.fovframe = tk.Frame(self.simsetupframe)
        self.fovframe.pack(side="top", fill="both", padx=10)
        
        self.showfovlabel = tk.Label(self.fovframe, text="SHOW ROBOT FIELD OF VIEW: ", font=("bahnschrift", 12))
        self.showfovlabel.grid(row=0, column=0, padx=2, pady=2, sticky="w")
        
        self.showfov = tk.BooleanVar()
        
        self.showfovradio = tk.Radiobutton(self.fovframe, text="Show", variable=self.showfov, value=True, font=("bahnschrift", 12))
        self.showfovradio.grid(row=0, column=1, padx=2, sticky="w")
        
        self.hidefovradio = tk.Radiobutton(self.fovframe, text="Hide", variable=self.showfov, value=False, font=("bahnschrift", 12))
        self.hidefovradio.select()
        self.hidefovradio.grid(row=0, column=2, padx=2, sticky="w")
        
        self.horizontal = ttk.Separator(self.simsetupframe, orient="horizontal")
        self.horizontal.pack(side="top", fill="both", padx=10, pady=5)
        
    def showFov(self):
        return self.showfov.get()
    
    def loadFov(self, fov):
        self.showfov.set(fov)
                
class Football:
    def __init__(self, field, x, y):
        self.canvas = field.getcanvas()
        self.Canvaswidth = field.getsize()[0]
        self.Canvasheight = field.getsize()[1]
        self.x = x + self.Canvaswidth/2
        self.y = y
        self.r = 13
        self.createball()
    
    def createball(self):
        self.ball = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill="#424242", outline="white", width=2)
    
    def getbody(self):
        return self.ball
    
    def changePos(self, x, y):
        self.x = x
        self.y = y
        self.canvas.delete(self.ball)
        self.createball()
    
    def getPos(self):
        return (self.x, self.y)
    
    def move(self):
        if (self.x < 0 + self.r or self.x > self.Canvaswidth - self.r) or (self.y < 0 + self.r or self.y > self.Canvasheight - self.r):
            self.changePos(self.x, self.y)
            return

        xmove = math.sin(math.radians(self.heading)) * (self.velocity * (BALL_WEIGHT / ROBOT_WEIGHT))
        ymove = math.cos(math.radians(self.heading)) * (self.velocity * (BALL_WEIGHT / ROBOT_WEIGHT))
        self.x += xmove
        self.y += ymove
        self.canvas.delete(self.ball)
        self.createball()
        
    def setspeed(self, speed):
        self.velocity = speed
    
    def getspeed(self):
        return self.speed

    def momentum(self, args):
        try:
            checklength(args, 2)
        except ArgumentLengthError:
            print("!!Invalid number of arguments!!")
            return
        
        self.heading, self.speed = args
        self.velocityy = math.cos(math.radians(self.heading)) * (self.speed)
        self.velocityx = math.sin(math.radians(self.heading)) * (self.speed)
        
        self.velocity = math.sqrt(self.velocityx**2 + self.velocityy**2)
    
    def resetpos(self):
        self.x = field.getsize()[0]/2
        self.y = field.getsize()[1]/2
        
        messagebox.showinfo("Reset", "Ball has been reset to the center")
        
        self.canvas.delete(self.ball)
        self.createball()

class Robot:
    def __init__(self, field, x, y, speed, color, robotID):
        self.Canvaswidth = field.getsize()[0]
        self.Canvasheight = field.getsize()[1]
        self.color = color
        self.x = x + self.Canvaswidth/2
        self.y = y
        self.canvas = field.getcanvas()
        self.speed = speed
        self.velocity = 0
        self.deadend = False
        self.robotID = robotID
        
        self.showfov = False
        self.fovangle = 50
        self.fovbaselength = 200
        self.fovtriangle = 10000
        self.oldfov = None
        
        # create a hexagon that has center at x y
        self.width = 80
        self.height = 80
        self.createbody(self.width, self.height, self.color)
        
    def changePos(self, x, y):
        self.x = x
        self.y = y
        self.canvas.delete(self.body)
        self.createbody(self.width, self.height, self.color)
        
    def createbody(self, width, height, color):
       self.body = self.canvas.create_polygon(self.x, self.y - height / 2, self.x + width / 2, self.y - height / 4, self.x + width / 2, self.y + height / 4, self.x, self.y + height / 2, self.x - width / 2, self.y + height / 4, self.x - width / 2, self.y - height / 4, fill=color, outline="")
       
    def getbodyid(self):
        return self.body
    
    def momentum(self, heading, speed):
        velocityx = math.sin(math.radians(heading)) * (speed * 0.0005)
        velocityy = math.cos(math.radians(heading)) * (speed * 0.0005)
        
        self.velocity = math.sqrt(velocityx**2 + velocityy**2) * (ROBOT_WEIGHT / 9.81)
        return (heading, self.velocity)
        
    def setvelocity(self, velocity):
        self.velocity = velocity
    
    def getPos(self):
        return self.x, self.y
    
    def move(self, heading, speed, collision = False):
        xmove = math.sin(math.radians(heading)) * (speed * 0.0015)
        ymove = math.cos(math.radians(heading)) * (speed * 0.0015)
        
        if (self.x + xmove < 0 + self.width/2 or self.x + xmove > self.Canvaswidth - self.width/2) or (self.y + ymove < 0 + self.height/2 or self.y + ymove > self.Canvasheight - self.height/2):
            self.changePos(self.x, self.y)
            self.velocity = 0
            self.speed = 0
            self.deadend = True
            return
        
        if collision:
            return
        
        self.x += xmove
        self.y += ymove
        self.changePos(self.x, self.y)
    
    def resetpos(self):
        randx = random.randint(80, self.Canvaswidth - 80)
        randy = random.randint(80, self.Canvasheight - 80)
        
        self.x = randx
        self.y = randy
        
        self.changePos(self.x, self.y)
        self.velocity = 0
    
    def fov(self, ourrobot):
        
        SIDELENGTH = self.fovbaselength / (2 * math.cos(math.radians(self.fovangle)))

        if ourrobot:
            # isosceles triangle base at the center of the robot
            x1 = self.x - self.fovbaselength / 2
            y1 = self.y + SIDELENGTH
            x2 = self.x + self.fovbaselength / 2
            y2 = self.y + SIDELENGTH
            x3 = self.x
            y3 = self.y
            
            self.oldfov = self.fovtriangle
            self.fovtriangle = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="red", width=2)
            self.canvas.delete(self.oldfov)
        else:
            x1 = self.x - self.fovbaselength / 2
            y1 = self.y - SIDELENGTH
            x2 = self.x + self.fovbaselength / 2
            y2 = self.y - SIDELENGTH
            x3 = self.x
            y3 = self.y
            
            self.oldfov = self.fovtriangle
            self.fovtriangle = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="blue", width=2)
            self.canvas.delete(self.oldfov)
    
    def hidefov(self):
        if len(self.canvas.find_withtag(self.fovtriangle)) > 0:
            self.canvas.delete(self.fovtriangle)
        
        return

def StartSim():
    global startsim
    global pausesim
    
    INITIALTIME = time.time()
    
    ROBOT1_INITIAL_SPEED = 200
    ROBOT2_INITIAL_SPEED = 200
    
    ROBOT1_SPEED = 0
    ROBOT1_HEADING = 0
    
    ROBOT2_SPEED = 0
    ROBOT2_HEADING = 0
    
    OURGOAL, ENEMYGOAL = field.getgoals()
    
    gameinfo.setinitialtime(INITIALTIME)
    pausetime = lastpausetime = ourscore = enemyscore = ball_heading = ball_speed = lasterror1 = lasterror2 = ballstoptime = 0
    balllastpos = ballcurrentpos = (0, 0)
    startsim = True
    pausesim = False
    ballhit = False
    robotcolision = False
    ballreset = False
    
    while startsim:

        while not pausesim:
            controller.changePausebutton("Pause")
            if simsetup.showFov():
                robot1.fov(True)
                robot2.fov(False)
            else:
                robot1.hidefov()
                robot2.hidefov()
            # finding for ball
            currentballpos = football.getPos()
            currentrobot1pos = robot1.getPos()
            currentrobot2pos = robot2.getPos()
            
            kpr1 = float(settings.getpidvalues()["Kp1"].get())
            kir1 = float(settings.getpidvalues()["Ki1"].get())
            kdr1 = float(settings.getpidvalues()["Kd1"].get())
            
            kpr2 = float(settings.getpidvalues()["Kp2"].get())
            kir2 = float(settings.getpidvalues()["Ki2"].get())
            kdr2 = float(settings.getpidvalues()["Kd2"].get())
            
            xr1_diff = currentballpos[0] - currentrobot1pos[0]
            yr1_diff = currentballpos[1] - currentrobot1pos[1]

            xr2_diff = currentballpos[0] - currentrobot2pos[0]
            yr2_diff = currentballpos[1] - currentrobot2pos[1]
            
            # distance from ball to robot
            disr1 = math.sqrt(xr1_diff**2 + yr1_diff**2)
            disr2 = math.sqrt(xr2_diff**2 + yr2_diff**2)
            
            if disr1 < 55:
                ROBOT1_HEADING = math.degrees(math.atan2(xr1_diff, yr1_diff))
                ROBOT1_SPEED = ROBOT1_INITIAL_SPEED
            else:
                ROBOT1_HEADING = math.degrees(math.atan2(xr1_diff, yr1_diff - 50))
                res1, error1 = Pid(disr1, kpr1, kir1, kdr1, lasterror1)
                ROBOT1_SPEED = limit(ROBOT1_INITIAL_SPEED * ((disr1 + res1) * 0.01) + 0.85, -100, 120)
                lasterror1 = error1
                
            if disr2 < 55:
                ROBOT2_HEADING = math.degrees(math.atan2(xr2_diff, yr2_diff))
                ROBOT2_SPEED = ROBOT2_INITIAL_SPEED
            else:
                ROBOT2_HEADING = math.degrees(math.atan2(xr2_diff, yr2_diff + 50))
                res2, error2 = Pid(disr2, kpr2, kir2, kdr2, lasterror2)
                ROBOT2_SPEED = limit(ROBOT2_INITIAL_SPEED * ((disr2 + res2) * 0.01) + 0.85, -100, 120)
                lasterror2 = error2
            
            momentum_robot1 = robot1.momentum(ROBOT1_HEADING, ROBOT1_SPEED)
            momentum_robot2 = robot2.momentum(ROBOT2_HEADING, ROBOT2_SPEED)
            
            # check robot collision
            for i in field.getcanvas().find_overlapping(robot1.getPos()[0] - (robot1.width / 2) + 10, robot1.getPos()[1] - (robot1.height / 2) + 10, robot1.getPos()[0] + (robot1.width / 2) - 10, robot1.getPos()[1] + (robot1.height / 2) - 10):
                
                if i == robot2.getbodyid() and (not ballreset and ballcurrentpos == balllastpos):
                    print("robot collision")
                    # calculate new heading and speed using heading and speed of robot 1 and 2
                    ROBOT1_HEADING = math.degrees(math.atan((math.sin(math.radians(ROBOT1_HEADING)) * ROBOT1_SPEED + math.sin(math.radians(ROBOT2_HEADING)) * ROBOT2_SPEED) / (math.cos(math.radians(ROBOT1_HEADING)) * ROBOT1_SPEED + math.cos(math.radians(ROBOT2_HEADING)) * ROBOT2_SPEED)))
                    
                    ROBOT1_SPEED = math.sqrt((math.cos(math.radians(ROBOT1_HEADING)) * ROBOT1_SPEED + math.cos(math.radians(ROBOT2_HEADING)) * ROBOT2_SPEED)**2 + (math.sin(math.radians(ROBOT1_HEADING)) * ROBOT1_SPEED + math.sin(math.radians(ROBOT2_HEADING)) * ROBOT2_SPEED)**2)
                    
                    # set robot 2 speed and heading to the same as robot 1
                    ROBOT2_SPEED = ROBOT1_SPEED
                    ROBOT2_HEADING = ROBOT1_HEADING
                    
                    if robot1.deadend or robot2.deadend:
                        ROBOT1_SPEED = 50
                        ROBOT2_SPEED = 50
                        
                        ROBOT1_HEADING = -135
                        ROBOT2_HEADING = -45
                    
                    
                    break
            
            if (football.getPos()[1] - 50 < robot1.getPos()[1]) and (math.degrees(math.atan2(xr1_diff, yr1_diff)) > 25 or math.degrees(math.atan2(xr1_diff, yr1_diff)) < -25) and disr1 > 50:
                
                ROBOT1_HEADING = 180
                ROBOT1_SPEED = 125
            
            if (football.getPos()[1] + 50 > robot2.getPos()[1] and (math.degrees(math.atan2(xr2_diff, yr2_diff)) > 155 or math.degrees(math.atan2(xr2_diff, yr2_diff)) > -155) and disr2 > 50):

                ROBOT2_HEADING = 0
                ROBOT2_SPEED = 125
            
            for i in field.getcanvas().find_overlapping(robot1.getPos()[0] - (robot1.width / 2) + 20, robot1.getPos()[1] - (robot1.height / 2) + 20, robot1.getPos()[0] + (robot1.width / 2) - 20, robot1.getPos()[1] + (robot1.height / 2) - 20):
                
                if i == football.getbody():
                    ball_heading, ball_speed = momentum_robot1
                    ballhit = True
                    football.momentum((ball_heading, ball_speed))
                    break
            
            for i in field.getcanvas().find_overlapping(robot2.getPos()[0] - (robot2.width / 2) + 20, robot2.getPos()[1] - (robot2.height / 2) + 20, robot2.getPos()[0] + (robot2.width / 2) - 20, robot2.getPos()[1] + (robot2.height / 2) - 20):
                
                if i == football.getbody():
                    ball_heading, ball_speed = momentum_robot2
                    ballhit = True
                    football.momentum((ball_heading, ball_speed))
                    break
            
            # make robot 1 move
            robot1.move(ROBOT1_HEADING, ROBOT1_SPEED)
            
            # make robot 2 move
            robot2.move(ROBOT2_HEADING, ROBOT2_SPEED)
            print(ROBOT2_HEADING, ROBOT2_SPEED)
                  
            if ballhit:
                football.move()
                ball_speed -= fieldinfo.getfriction()
                football.setspeed(ball_speed)
                if ball_speed <= 0:
                    football.setspeed(0)
                    ballhit = False
            
            ballcurrentpos = football.getPos()

            if balllastpos == ballcurrentpos and not football.getPos() == (field.getsize()[0]/2, field.getsize()[1]/2):
                ballstoptime = int(time.time() - ballLastMovetime)
            else:
                ballreset = False
                ballstoptime = 0
                ballLastMovetime = time.time()
                
            if ballstoptime >= 5:
                football.resetpos()
                ball_speed = 0
                football.setspeed(0)
                ballreset = True
                ballstoptime = 0
            
            balllastpos = ballcurrentpos
            
            # check for goal
            for i in field.getcanvas().find_overlapping(football.getPos()[0] - (football.r), football.getPos()[1] - (football.r), football.getPos()[0] + (football.r), football.getPos()[1] + (football.r)):
                
                if i == ENEMYGOAL and football.getPos()[1] <= football.r:
                    ourscore += 1
                    football.resetpos()
                    robot1.resetpos()
                    robot2.resetpos()
                    ourgoal_log.append("Goal at " + str(gameinfo.gettimeelapsed()) + " (" + gameinfo.getscores() + ")")
                
                if i == OURGOAL and football.getPos()[1] >= field.getsize()[1] - football.r:
                    enemyscore += 1
                    football.resetpos()
                    robot1.resetpos()
                    robot2.resetpos()
                    enemygoal_log.append("Goal at " + str(gameinfo.gettimeelapsed()) + " (" + gameinfo.getscores() + ")")
                    
                
            
            window.update()
            gameinfo.starttimer(time.time() - (pausetime + lastpausetime))
            gameinfo.setscore(ourscore, enemyscore)
            
        lasttime = time.time()    
        lastpausetime = pausetime
        
        while pausesim:
            controller.changePausebutton("Resume")
            pausetime = time.time() - lasttime
            window.update()
    
    window.update()
        
def Pid(error, kp, ki, kd, lasterror, integral=0):
    
    PD = kp * error + kd * (error - lasterror)
    if error == 0:
        integral = 0
    else:
        integral = error + integral
    I = ki * integral
    res = PD + I
    return res, error

def limit(value, min, max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value

def StopSim():
    global startsim
    global pausesim
    global settings
    global fieldinfo
    global gameinfo
    global ourgoal_log
    global enemygoal_log
    
    pausesim = True
    startsim = False
    
    ourgoal = "\n".join(ourgoal_log)
    enemygoal = "\n".join(enemygoal_log)
    
    content = [
        "Game simulated at {}".format(time.strftime("%d-%m-%Y %H:%M:%S")),
        "Time elapsed: {}".format(gameinfo.gettimeelapsed()),
        "Score: {}\n".format(gameinfo.getscores()),
        "===============================================================\n",
        "Field Settings:",
        "|{:-<11}|{:-^11}|".format("", "Value"),
        "|{:<11}|{:<11}|".format("Friction", fieldinfo.getfriction()),
        "|-----------------------|\n",
        "Robot Settings:",
        "|{:-<11}|{:-^11}|{:-^11}|".format("", "Robot 1", "Robot 2"),
        "|{:<11}|{:<11}|{:<11}|".format("Kp", settings.getpidvalues()["Kp1"].get(), settings.getpidvalues()["Kp2"].get()),
        "|{:<11}|{:<11}|{:<11}|".format("Ki", settings.getpidvalues()["Ki1"].get(), settings.getpidvalues()["Ki2"].get()),
        "|{:<11}|{:<11}|{:<11}|".format("Kd", settings.getpidvalues()["Kd1"].get(), settings.getpidvalues()["Kd2"].get()),
        "|-----------------------------------|\n",
        "===============================================================",
        "Player's Goal:",
        ourgoal,
        "\nEnemy's Goal:",
        enemygoal,      
               ]
    
    dirname = "logs"

    if not os.path.exists(dirname):
        os.mkdir(dirname)
    
    formattedtime = time.strftime("%Y%m%d_%H%M%S")
    
    filepath = "logs/log_" + formattedtime + "_" + gameinfo.getscores() + ".txt"
    file = open(filepath, "w")
    
    for i in content:
        file.write(i + "\n")
    
    file.close()
    
    controller.changePausebutton("Pause")
    gameinfo.reset()

def PauseSim():
    global pausesim
    pausesim = True
    
def ResumeSim():
    global pausesim
    pausesim = False
    
def SavePreferences():
    global settings
    global fieldinfo
    global simsetup
    
    newpidval = {}
    
    for k,v in settings.getpidvalues().items():
        newpidval[k] = v.get()
    
    preferences = {
        "FRICTION": fieldinfo.getfriction(),
        "PIDVALUE": newpidval,
        "ROBOTFOV": simsetup.showFov(),
    }
    
    print(preferences)
    
    filepath = filedialog.asksaveasfilename(title = "Save Preferences", filetypes = [("all files","*.*")])
    print(filepath)
    if filepath == '':
        return
    else:
        file = open(filepath, "wb")
        pickle.dump(preferences, file)
        file.close()
    
    messagebox.showinfo("Preferences Saved", "Preferences saved to " + filepath)

def LoadPreferences():
    
    filepath = filedialog.askopenfile(title = "Load Preferences", filetypes = [("all files","*.*")])
    if filepath is None:
        return
    else:
        file = open(filepath.name, "rb")
        load = pickle.load(file)
        
        accept = messagebox.askokcancel("Load Preferences", "Do you want to load these content?\n\nField Friction: {}\n----Robot1----\nKp: {}\nKi: {}\nKd: {}\n----Robot2----\nKp: {}\nKi: {}\nKd: {}\nShow Robot FOV: {}".format(load["FRICTION"], load["PIDVALUE"]["Kp1"], load["PIDVALUE"]["Ki1"], load["PIDVALUE"]["Kd1"], load["PIDVALUE"]["Kp2"], load["PIDVALUE"]["Ki2"], load["PIDVALUE"]["Kd2"], load["ROBOTFOV"]))
        
        if accept:
            fieldinfo.setfriction(load["FRICTION"])
            settings.loadpidvalues(load["PIDVALUE"])
            simsetup.loadFov(load["ROBOTFOV"])
            
def ShowLogFolder():
    if os.path.exists("logs"):
        os.startfile("logs")
    else:
        messagebox.showerror("Error", "No log folder found!")
  
startsim = False
pausesim = False
    
field = Field(window)

infoscreen = InfoScreen(window)
infoframe = infoscreen.getframe()
gameinfo = GameInformation(window, infoframe)
fieldinfo = FieldInfo(window, infoframe)
settings = RobotSettings(window, infoframe)
simsetup = SimulationSetup(window, infoframe)
controller = Controller(window, infoframe)
robot1 = Robot(field, random.randrange(int(-field.getsize()[0]/2) + 80, int(field.getsize()[0]/2) - 80), random.randrange(0, field.getsize()[1] - 80), 0, "#ff5cd3", 1)
robot2 = Robot(field, random.randrange(int(-field.getsize()[0]/2) + 80, int(field.getsize()[0]/2) - 80), random.randrange(0, field.getsize()[1] - 80), 0, "#0ff279", 2)
football = Football(field, 0, field.getsize()[1]/2)

ourgoal_log = []
enemygoal_log = []
    
window.mainloop()