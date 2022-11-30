import turtle

def distanceBetween(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def RobotBattle():
    robotList = []
    
    while True:
        turtle.clear()
        for robot in robotList:
            robot.draw()
        
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(f"{i}: {robot.displayStatus()}")
            i += 1
        
        print("===============")
        
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == 'q':
            break
        elif choice == "c":
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikeBot: ")
            if robotType == 'r':
                newRobot = Robot()
            elif robotType == 'm':
                newRobot = MedicBot()
            elif robotType == 's':
                newRobot = StrikeBot()
            
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)
            
        i = 0
        for robot in robotList:
            if(robot.health <= 0):
                del robotList[i]
            i += 1

class Robot(object):
    def __init__(self):
        self.health = 100
        self.energy = 100
        self.x = 100
        self.y = 100
    
    def move(self, newX, newY):
        if self.energy > 0:
            self.energy -= 10
            self.x = newX
            self.y = newY
        else:
            return
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.circle(10)
        turtle.penup()
        turtle.goto(self.x, self.y + 20)
        turtle.pendown()
        turtle.write(f"Health: {self.health}, Energy: {self.energy}")
    
    def displayStatus(self):
        return f"x={self.x}, y={self.y}, health={self.health}, energy={self.energy}"
    
    def command(self, robotList):
        print("Enter which command to execute")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)
    
class MedicBot(Robot):
    def __init__(self):
        super().__init__()
    
    def heal(self, r):
        if self.energy >= 20 and distanceBetween(self.x, self.y, r.x, r.y) <= 10:
            self.energy -= 20
            r.health += 10
        else:
            return
    
    def command(self, robotList):
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(f"{i}: {robot.displayStatus()}")
            i += 1
        
        print("===============")
        
        choice = input("'1' to move, '2' to heal other: ")
        if int(choice) == 1:
            super().command(robotList)
        elif int(choice) == 2:
            robotToHeal = int(input("Enter which robot to heal: "))
            self.heal(robotList[robotToHeal])

class StrikeBot(Robot):
    def __init__(self, missile = 5):
        super().__init__()
        self.missile = missile
    
    def strike(self, r):
        if self.energy >= 20 and distanceBetween(self.x, self.y, r.x, r.y) <= 10 and self.missile > 0:
            self.energy -= 20
            r.health -= 50
            self.missile -= 1
        else:
            return
    
    def displayStatus(self):
        return super().displayStatus() + f", missile={self.missile}"
    
    def command(self, robotList):
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(f"{i}: {robot.displayStatus()}")
            i += 1
        
        print("===============")
        
        choice = input("'1' to move, '2' to strike other: ")
        if int(choice) == 1:
            super().command(robotList)
        elif int(choice) == 2:
            robotToAttack = int(input("Enter which robot to attack: "))
            self.strike(robotList[robotToAttack])
        else:
            print("Invalid input")
            return
            
RobotBattle()