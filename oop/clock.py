class Time:
    def __init__(self, t=-1, hours=-1, minutes=-1, seconds=-1):
        self.time = t
        self.m = minutes
        self.h = hours
        self.s = seconds
        
        if t != -1:
            self.update_by_seconds()

        if minutes != -1 or hours != -1 or seconds != -1:
            self.convert(minutes, hours, seconds)

    def update_by_normal(self):
        self.time = self.m * 60 + self.h * 3600 + self.s

    def update_by_seconds(self):
        self.h = self.time // 3600
        self.m = (self.time - self.h * 3600) // 60
        self.s = (self.time - self.h * 3600 - self.m * 60)
        if self.h > 24 or self.h < 0:
            self.h = abs(self.h % 24)

    def convert(self, minutes, hours, seconds):
        if minutes != -1:
            self.m = minutes
        else:
            self.m = 0
        if hours != -1:
            self.h = hours
        else:
            self.h = 0
        if seconds != -1:
            self.s = seconds
        else:
            self.s = 0
        self.update_by_normal()

    def __add__(self, other):
        return Time(self.time + other.time)
    
    def __sub__(self, other):
        return Time(self.time - other.time)

    def get(self):
        return self.h, self.m, self.s

    def __str__(self):
        return f"{str(self.h).zfill(2)}:{str(self.m).zfill(2)}:{str(self.s).zfill(2)}"
    
t1 = Time(0)
t2 = Time(86399)
t3 = Time(-1, 17, 35, 40)
breakpoint()