from cmu_graphics import *

#-----------MODULE 2 Button-----------------------------------------------------
class Button:
    def __init__(self, x, y, r, fun, fill = "", text = None ,align = "center"):
        self.x = x
        self.y = y
        self.r = r
        self.fun = fun #this change to a certain screen
        self.flil = fill
        self.text = text
        self.align = align

    def draw(self):
        drawCircle(self.x, self.y, self.r, opacity=0)
        if self.text != None:
            drawLabel(self.text, self.x, self.y, size=20)

    def checkForPress(self, app, mX, mY):
        if ((mX - self.x)**2 + (mY - self.y)**2)**0.5 <= self.r:
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
