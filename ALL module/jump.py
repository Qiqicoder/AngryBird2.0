from cmu_graphics import *
class Thing:    
    def __init__(self):
    x = 100
    y = 100
    vx = 0
    vy = 0
    def takeStep(self):
        x += vx
        y += vy

    def accelerate(self, ax, ay):
        vx += ax
        vy += ay


    def onAppStart(app):
        app.thing = Thing(200, 200) 

    def onStep(app): 
        app.thing.takeStep() 
    def onMousePress(app, mx, my):  
    # Accelerate towards mouseClick  
    # Scale it down to be resonable  
        scale = 0.01  
        app.thing.accelerateTowardsPoint(mx, my, scale) 
    def redrawAll(app):  
        app.thing.draw()

    #class Thing:  
    def __init__(self, x, y):    
        self.x = x    
        self.y = y    
        self.vx = 0    
        self.vy = 0  
    def takeStep(self):    
        self.x += self.vx    
        self.y += self.vy  
    def accelerate(self, ax, ay):    
        self.vx += ax    
        self.vy += ay  
    def accelerateTowardsPoint(self, x, y, scale):    
    # Accelerate (change velocity) towards point    
        ax = (x - self.x) * scale    
        ay = (y - self.y) * scale    
        self.accelerate(ax, ay)  
    def draw(self):    
        drawCircle(self.x, self.y, 15)

def redrawAll(app):
    for ball in app.ballList:
        ball.draw()

runApp(width = 600, height = 600)