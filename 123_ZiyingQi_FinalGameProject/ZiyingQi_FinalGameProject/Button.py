from cmu_graphics import *

#-----------MODULE 2 Button-----------------------------------------------------
class Button:
    def __init__(self, x, y, width, height, fun, fill = "red", text = None ,align = "center"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fun = fun #this change to a certain screen
        self.flil = fill
        self.text = text
        self.align = align

    def draw(self):
        drawRect(self.x - self.width/2, self.y - self.height/2, self.width, self.height, opacity=0)
        if self.text != None:
            drawLabel(self.text, self.x, self.y, size=20)

    def checkForPress(self, app, mX, mY):
        if (self.x - self.width/2 <= mX <= self.x + self.width/2) and (self.y -self.height/2 <= mY <= self.y +self.height):
            self.fun(app)
#_________Button Functions______________________________________________________
def gameScreen(app):
    setActiveScreen("next")

def muteButtonFunction(app):
    app.music = not app.music  # mute button

def helpMenuButtonFunction(app):
    app.textVisible = not app.textVisible

def pauseButtonFunction(app):
    app.pause = not app.pause
    