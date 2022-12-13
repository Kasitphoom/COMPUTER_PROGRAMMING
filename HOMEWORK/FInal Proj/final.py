import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import math
import time

window = tk.Tk()
window.title("Robot omni-wheels Soccer Simulation")
window.geometry("1200x800")
window.resizable(False, False)

class IncrementPositiveError(Exception):
    pass

class IncrementValueError(Exception):
    pass

class IncrementStepError(Exception):
    pass

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
        self.canvas.create_rectangle(147, 0, 301, 50, outline="", fill="#FF0000", width=4)
        
        # create player goal
        self.canvas.create_rectangle(147, 732, 301, 782, outline="", fill="#0000FF", width=4)
        self.field.tkraise()
        
    def getcanvas(self):
        return self.canvas
    
    def getsize(self):
        self.window.update()
        return self.canvas.winfo_width(), self.canvas.winfo_height()
        
class InfoScreen:
    def __init__(self, window):
        self.window = window
        self.screen = tk.Frame(self.window)
        self.screen.pack(side="right", fill="both", expand="true", padx=10, pady=10)
    
    def getframe(self):
        return self.screen
    
class Controller:
    def __init__(self, window, frame):
        self.window = window
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
        

class GameInformation:
    def __init__(self, window, frame):
        self.window = window
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
        
class FieldInfo:
    def __init__(self, window, frame):
        self.window = window
        self.frame = frame
        self.frictionval = tk.StringVar()
        self.frictionval.set(0.0)
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
    
    
class RobotSettings:
    def __init__(self, window, frame):
        self.window = window
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
        

class SimulationSetup:
    def __init__(self, window, frame):
        self.window = window
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
    
    def getPos(self):
        return (self.x, self.y)
               

class Robot:
    def __init__(self, field, x, y, speed, color):
        self.Canvaswidth = field.getsize()[0]
        self.Canvasheight = field.getsize()[1]
        self.color = color
        self.x = x + self.Canvaswidth/2
        self.y = y
        self.canvas = field.getcanvas()
        self.speed = speed
        print(self.x, self.y)
        
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
    
    def getPos(self):
        return self.x, self.y
    
    def move(self, heading, speed):
        if (self.x < 0 + self.width/2 or self.x > self.Canvaswidth - self.width/2) or (self.y < 0 + self.height/2 or self.y > self.Canvasheight - self.height/2):
            self.changePos(self.x, self.y)
            return
        
        xmove = math.sin(math.radians(heading)) * (speed * 0.0005)
        ymove = math.cos(math.radians(heading)) * (speed * 0.0005)
        self.x += xmove
        self.y += ymove
        self.changePos(self.x, self.y)

def StartSim():
    global startsim
    global pausesim
    
    INITIALTIME = np.copy(time.time())
    gameinfo.setinitialtime(INITIALTIME)
    pausetime = lastpausetime = ourscore = enemyscore = 0
    startsim = True
    pausesim = False
    while startsim:

        while not pausesim:
            controller.changePausebutton("Pause")
            robot1.move(0, 50)
            print(field.getcanvas().find_overlapping(robot1.getPos()[0], robot1.getPos()[1], robot1.getPos()[0], robot1.getPos()[1]))
            window.update()
            gameinfo.starttimer(time.time() - (pausetime + lastpausetime))
            gameinfo.setscore(ourscore, enemyscore)
            
        lasttime = time.time()    
        lastpausetime = pausetime
        
        while pausesim:
            controller.changePausebutton("Resume")
            pausetime = time.time() - lasttime
            window.update()
        
        

def StopSim():
    global startsim
    global pausesim
    
    pausesim = True
    startsim = False
    controller.changePausebutton("Pause")
    gameinfo.reset()

def PauseSim():
    global pausesim
    pausesim = True
    
def ResumeSim():
    global pausesim
    pausesim = False

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
robot1 = Robot(field, 0, 75, 0, "#FF4E4E")
robot2 = Robot(field, 0, 300, 0, "#FF4E4E")
football = Football(field, 0, field.getsize()[1]/2)
    
window.mainloop()