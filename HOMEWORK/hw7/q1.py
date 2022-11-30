class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def setTime(self, hour, minute, second):
        if minute >= 60:
            hour += minute // 60
            minute %= 60
        if second >= 60:
            minute += second // 60
            second %= 60
            
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def getTime(self):
        return self.hour, self.minute, self.second
    
    def tick(self):
        self.second += 1
        if self.second >= 60:
            self.minute += self.second // 60
            self.second %= 60
        if self.minute >= 60:
            self.hour += self.minute // 60
            self.minute %= 60
        if self.hour >= 24:
            self.hour %= 24
            
    def display(self):
        # am pm format
        ampm = "PM"
        if self.hour < 12:
            ampm = "AM"
            
        hour = self.hour
        hour %= 12
        print("{:02d}:{:02d}:{:02d} {}".format(hour, self.minute, self.second, ampm))
        
c = Clock(23, 59, 59)

# print the time
print(c.getTime())
# set the time
c.setTime(23, 59, 59)
# print the time
print(c.getTime())
# tick
c.tick()
# print the time
print(c.getTime())
# display the time
c.display()
c.tick()
c.display()