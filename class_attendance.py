# 0 = False
# 1 = True

import time

has_checked = False

class Attendance:
    
    def __init__(self, name):
        self.name = name
        self.check()

    def check(self):
        if self.name == "Unknown":
            pass   
        elif self.name != "Unknown" and not has_checked:
            print(self.name)
            has_checked = True
            
