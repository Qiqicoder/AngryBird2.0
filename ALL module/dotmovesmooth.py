from cmu_graphics import *
from PIL import Image
import os, pathlib
from Charactor import Charactor

def onAppStart(app):
    app.fireboy = Charactor('red', 100, 400)
    app.watergirl = Charactor('blue', 700, 400)

    app.move = 5
    app.r = 20

    app.dotBorder = None

#____________________________background_________________________________________
    def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))
    app.image = openImage("images/background.jpg")
    app.imageWidth,app.imageHeight = app.image.width,app.image.height
    app.image = CMUImage(app.image)
#____________________________background_________________________________________

def redrawAll(app):
    newWidth, newHeight = (app.imageWidth*2,app.imageHeight*2)
    drawImage(app.image,0,0,width=newWidth,height=newHeight,opacity=50)
    drawLabel("Fireboy&Watergirl", 100, 30, size=16)
    drawLabel("Press ↑↓←→ to move the Fireboy", 100, 50)
    drawLabel("Press wsad to move the Watergirl", 100, 70)

    app.fireboy.draw()
    app.watergirl.draw()

def defKeyName(app, charactor, keys, up, down, left, right):
    charactor.moving = False

    if up in keys:
        charactor.jump = True

    if right in keys and left not in keys:
        charactor.x += app.move
        charactor.moving = True
        if charactor.x > app.width - app.r:
            charactor.x = app.width - app.r

    elif left in keys and right not in keys:
        charactor.x -= app.move
        charactor.moving = True
        if charactor.x < app.r:
            charactor.x = app.r

def onKeyHold(app, keys):
    defKeyName(app, app.fireboy, keys, 'up', 'down', 'left', 'right')
    defKeyName(app, app.watergirl, keys, 'w', 's', 'a', 'd')

def onStep(app): 
    charactorJump(app, app.fireboy)
    charactorJump(app, app.watergirl)

def charactorJump(app, charactor):
    if charactor.jump:
        charactor.accelerateTowardsPoint()
        charactor.y -= 2
        if charactor.y < app.height - 100:
            charactor.takeStep()
        else:
            charactor.jump = False
            charactor.vy = -15

def main():
    runApp(width=800,height=500)

main()