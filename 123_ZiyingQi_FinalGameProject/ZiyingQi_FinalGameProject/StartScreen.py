from cmu_graphics import *
from Button import Button

class StartScreen:
    def __init__(self, button):
        self.startButton = Button(100,200,50,self.startButtonFunction)



def startButtonFunction(self):
    self.screen = PlayScreen

def playButtonFunction(app):

def endButtonFunction(app):


def onAppStart(app):
    app.screen = 'startScreen'
    app.buttList = [Button(100,200,50,startButtonFunction),
                    Button(100,200,50,playButtonFunction),
                    Button(100,200,50,endButtonFunction)]

def onKeyPress(app, key):
    if key == 'a':
        app.screen = 'startScreen'
    elif key == 'b':
        app.screen = 'playScreen'

def onMousePress(app, mouseX, mouseY):
    for butt in app.buttList:
        butt.checkForPress(app, mouseX, mouseY)


def redrawStartScreen(app):
    drawLabel('startScreen', 100, 100, size=100)

def redrawPlayScreen(app):
    drawLabel('playScreen', 100, 100, size=100)

def redrawAll(app):
    if app.screen == 'startScreen':
        redrawStartScreen(app)
    elif app.screen == 'playScreen':
        redrawPlayScreen(app)
    else:
        print('Ack, what happened?')


def main():
    runApp()

main()


from cmu_graphics import *
def onAppStart(app):
    app.count = 0

def start_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill ="blue")
    drawLabel('Start Screen',200,30,size=20,bold=True)

def start_onKeyPress(app, key):
    if key == 'n':
        setActiveScreen("next")
    if key == 'c':
        app.count += 1
        print(app.count)

def next_redrawAll(app):
    drawLabel("Next",200,30,size = 50)

def next_onKeyPress(app,key):
    if key == 's':
        setActiveScreen("start")

def main():
    runAppWithScreens("start")

main()