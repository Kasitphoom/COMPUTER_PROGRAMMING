class Time():
    def __init__(self, hour, minute, second):
        if minute > 60:
            hour += minute // 60
            minute %= 60
        if second > 60:
            minute += second // 60
            second %= 60
        
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def print(self):
        print(f"{self.hour:02}:{self.minute:02}:{self.second:02} Hrs.")
        
time1 = Time(9, 30, 10)
time1.print()