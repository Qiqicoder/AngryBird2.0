from cmu_graphics import *

#-----------MODULE 1 Obstacles--------------------------------------------------
class Charactor:
    def __init__(self, fill, x = 100, y = 100):
        self.x = x
        self.y = y 
        self.vy = -15
        self.moving = False
        self.jump = False
        self.fill = fill

    def takeStep(self):
        self.y += self.vy

    def accelerate(self, ay):
        self.vy += ay

    def accelerateTowardsPoint(self):    
    # Accelerate (change velocity) towards point
        ay = 0.98
        self.accelerate(ay)

    def draw(self):    
        drawCircle(self.x, self.y, 15, fill = self.fill)