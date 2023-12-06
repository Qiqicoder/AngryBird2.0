from cmu_graphics import *
from PIL import Image
import os, pathlib

def onAppStart(app):
    app.margin = 5

    # defining a custom function to open images
    def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))
    
    app.image = openImage("images/background.jpg")
    app.imageWidth,app.imageHeight = app.image.width,app.image.height
    #app.imageFlipped = app.image.transpose(Image.FLIP_LEFT_RIGHT)
    app.image = CMUImage(app.image)
    #app.imageFlipped = CMUImage(app.imageFlipped)
def redrawAll(app):
    # drawPILImage takes in a PIL image object and the left-top coordinates
    #drawImage(app.image,0,0)

    # Scale image by defining new dimensions 
    newWidth, newHeight = (app.imageWidth*2,app.imageHeight*2)
    drawImage(app.image,0,0,width=newWidth,height=newHeight)

    #drawImage(app.imageFlipped,100,500)
    # Rotate image by a given angle (in degrees :/)
    #drawImage(app.image,500,500,rotateAngle=-60)
    # drawCaptions(app)

def main():
    runApp(width=800,height=500)

if __name__ == '__main__':
    main()