from cmu_graphics import *
from PIL import Image
import os, pathlib

# def openImage(fileName):
#         return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def onAppStart(app):
    #Sprite Strip: 'http://www.cs.cmu.edu/~112/notes/sample-spritestrip.png'
    
    spritestripF = Image.open('images/fireboyStanding.png')
    app.spritesF = [ ]
    for i in range(8):
        # Split up the spritestrip into its separate sprites
        # then save them in a list
        frameF = spritestripF.crop((100*i, 0, 100+100*i, 140))
        spriteF = CMUImage(frameF)
        app.spritesF.append(spriteF)
        
    # app.spriteCounter shows which sprite (of the list) 
    # we should currently display
    app.spriteCounter = 0
    app.stepCounter = 0
    app.stepsPerSecond = 50

def onStep(app):
    app.stepCounter += 1
    if app.stepCounter>= 8:
        app.spriteCounter = (1 + app.spriteCounter) % len(app.spritesF)
        app.stepCounter = 0 

def redrawAll(app):
    spriteF = app.spritesF[app.spriteCounter]
    drawImage(spriteF,200, 200, align = 'center')

def main():
    runApp(width=400, height=400)

if __name__ == '__main__':
    main()