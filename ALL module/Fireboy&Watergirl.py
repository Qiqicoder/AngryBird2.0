from cmu_graphics import *

#-----------MODULE 1 Players----------------------------------------------------
from PIL import Image
import os, pathlib

def openImage(fileName):
    return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def onStep(app):
    app.stepCounter += 1
    if app.stepCounter>= 8:
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)
        app.stepCounter = 0 


def onAppStart(app):
    spritestrip = openImage('images/spritestrip.png')
    background = openImage('images/background.jpg')
    app.background = 'grey'
    app.sprites = [ ]
    for i in range(6):
    # Split up the spritestrip into its separate sprites
    # then save them in a list
        frame = spritestrip.crop((30+260*i, 30, 230+260*i, 250))
        sprite = CMUImage(frame)
        app.sprites.append(sprite)
    
    # app.spriteCounter shows which sprite (of the list) 
    # we should currently display
    app.spriteCounter = 0
    app.stepCounter = 0
    app.stepsPerSecond = 50
    app.obstacles = [ obstacles(300, 700, 300, 20, 'darkSlateGray'),
                 obstacles(0, 900, 250, 20, 'darkSlateGray'),
                 obstacles(500, 500, 100, 20, 'darkSlateGray'),
                 obstacles(300, 300, 300, 20, 'darkSlateGray')
               ]

def redrawAll(app):
    sprite = app.sprites[app.spriteCounter]
    drawImage(sprite,200, 200, align = 'center')
    drawLabel('obstacles Example', 200, 30, size=16)
    drawLabel('Click in obstacles to change their count', 200, 50)
    # draw the obstacles:
    for obstacles in app.obstacles:
        drawRect(obstacles.recLeft, obstacles.recTop, obstacles.recWidth, obstacles.recHeight, fill=obstacles.reccolor)
        #drawLabel(str(obstacles.count), obstacles.rectLeft, obstacles.rectTop)

# def onkeyPress(app, keyX, keyY):
    

# def findcharacter(app, x, y):
#     # find the obstacles that contains this point
#     for obstacles in app.obstacles:
#         if (distance(x, y, obstacles.cx, obstacles.cy) <= obstacles.r):
#             return obstacles
#     return None

def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def main():
    runApp(width=1000, height=1000)

if __name__ == '__main__':
    main()