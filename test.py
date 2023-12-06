from cmu_graphics import *
from Button import Button

def onAppStart(app):
    app.screen = 'startScreen'
    app.startButton = Button(100,200,50,startButtonFunction)
    app.endButton = Button(100,200,50,startButtonFunction)

def onKeyPress(app, key):
    if key == 'a':
        app.screen = 'startScreen'
    elif key == 'b':
        app.screen = 'playScreen'

def onmousepress(app, mouseX, mouseY):
    app.startButton.checkForPress(app, mouseX, mouseY)
    app.endButton.checkForPress(app, mouseX, mouseY)


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