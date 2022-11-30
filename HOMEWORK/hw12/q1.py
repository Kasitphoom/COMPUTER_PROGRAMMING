class Clock:
    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss
        
    def run(self):
        self.ss += 1
        if self.ss == 60:
            self.ss = 0
            self.mm += 1
        if self.mm == 60:
            self.mm = 0
            self.hh += 1
        if self.hh == 24:
            self.hh = 0
        
        print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
    
    def setTime(self, hh, mm, ss):
        if mm > 60:
            hh += mm // 60
            mm = mm % 60
        if ss > 60:
            mm += ss // 60
            ss = ss % 60
        
        self.hh = hh
        self.mm = mm
        self.ss = ss

class AlarmClock(Clock):
    def __init__(self, hh, mm, ss, alarm_hh, alarm_mm, alarm_ss, alarm_on_off):
        super().__init__(hh, mm, ss)
        self.alarm_hh = alarm_hh
        self.alarm_mm = alarm_mm
        self.alarm_ss = alarm_ss
        self.alarm_on_off = alarm_on_off
    
    def setAlarm(self, alarm_hh, alarm_mm, alarm_ss):
        self.alarm_hh = alarm_hh
        self.alarm_mm = alarm_mm
        self.alarm_ss = alarm_ss
    
    def alarm_on(self):
        self.alarm_on_off = True
        
    def alarm_off(self):
        self.alarm_on_off = False
    
    def run(self):
        while True:
            super().run()
            if self.alarm_on_off:
                if self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss:
                    print("Alarm!")
                    break

clock = AlarmClock(23, 59, 55, 0, 0, 0, False)
clock.alarm_on()
clock.run()