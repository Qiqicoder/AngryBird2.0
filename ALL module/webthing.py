from cmu_graphics import *
from PIL import Image
import os, pathlib

def onAppStart(app):
    app.fireboycx = 200
    app.fireboycy = 200
    app.watergirlcx = 200
    app.watergirlcy = 200
    app.move = 5
    app.r = 20
    app.dotBorder = None
    app.gravity = 1  # Gravity value for continuous updates
    app.margin = 5

    # defining a custom function to open images
    def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))
    
    app.image = openImage("images/background.jpg")
    app.imageWidth,app.imageHeight = app.image.width,app.image.height
    #app.imageFlipped = app.image.transpose(Image.FLIP_LEFT_RIGHT)
    app.image = CMUImage(app.image)
def updateBalls(app):
    # Apply gravity to Fireboy
    app.fireboycy += app.gravity
    # Check collision with ground for Fireboy
    if app.fireboycy > app.height - app.r:
        app.fireboycy = app.height - app.r

    # Apply gravity to Watergirl
    app.watergirlcy += app.gravity
    # Check collision with ground for Watergirl
    if app.watergirlcy > app.height - app.r:
        app.watergirlcy = app.height - app.r

def onTimerFired(app):
    updateBalls(app)

def redrawAll(app):
    newWidth, newHeight = (app.imageWidth*2, app.imageHeight*2)
    drawImage(app.image, 0, 0, width=newWidth, height=newHeight, opacity=50)
    drawLabel("Fireboy&Watergirl", 100, 30, size=16)
    drawLabel("Press ↑↓←→ to move the Fireboy", 100, 50)
    drawLabel("Press wsad to move the Watergirl", 100, 70)
    drawCircle(app.fireboycx, app.fireboycy, app.r, fill='red')
    drawCircle(app.watergirlcx, app.watergirlcy, app.r, fill='blue')

def onKeyHold(app, keys):
    if 'right' in keys and 'left' not in keys:
        app.fireboycx += app.move
        if app.fireboycx > app.width - app.r:
            app.fireboycx = app.width - app.r
    elif 'left' in keys and 'right' not in keys:
        app.fireboycx -= app.move
        if app.fireboycx < app.r:
            app.fireboycx = app.r
    
    if 'up' in keys and 'down' not in keys:
        app.fireboycy -= app.move
        if app.fireboycy < app.r:
            app.fireboycy = app.r
    elif 'down' in keys and 'up' not in keys:
        app.fireboycy += app.move
        if app.fireboycy > app.height - app.r:
            app.fireboycy = app.height - app.r
    
    if 'd' in keys and 'a' not in keys:
        app.watergirlcx += app.move
        if app.watergirlcx > app.width - app.r:
            app.watergirlcx = app.width - app.r
    elif 'a' in keys and 'd' not in keys:
        app.watergirlcx -= app.move
        if app.watergirlcx < app.r:
            app.watergirlcx = app.r
    
    if 'w' in keys and 's' not in keys:
        app.watergirlcy -= app.move
        if app.watergirlcy < app.r:
            app.watergirlcy = app.r
    elif 's' in keys and 'w' not in keys:
        app.watergirlcy += app.move
        if app.watergirlcy > app.height - app.r:
            app.watergirlcy = app.height - app.r

    updateBalls(app)  # Call the updateBalls function for continuous updates

def main():
    runApp(width=800, height=500)  # Set a timer delay for continuous updates

main()
