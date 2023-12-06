from cmu_graphics import *
from PIL import Image
import os, pathlib

#-----------MODULE 1 Obstacles--------------------------------------------------
# def openImage(fileName):
#     return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

class Character:
    def __init__(self, imagePath, x = 100, y = 100, resizeFactor = 0.5):
        self.x = x
        self.y = y 
        self.characterSpeed = 0
        self.moving = False
        self.drop = False
        self.win = False
        self.standField = None
        # self.imagePath = imagePath
        # self.image = CMUImage(self.imagePath)
        self.image = Image.open(imagePath)
        # Resize the image based on the resizeFactor
        self.image = self.image.resize((int(self.image.width * resizeFactor), int(self.image.height * resizeFactor)))
        self.imageWidth, self.imageHeight = self.image.width, self.image.height
        self.image = CMUImage(self.image)
        # print(self.imageWidth, self.imageHeight)

    # def sprites(app):
    #     app.sprites = [ ]
    #     if not app.moving:
    #         for i in range(6):
    #             # Split up the spritestrip into its separate sprites
    #             # then save them in a list
    #             sprite = CMUImage(spritestrip.crop((30+260*i, 30, 230+260*i, 250)))
    #             app.sprites.append(sprite)
    #         # app.spriteCounter shows which sprite (of the list) 
    #         # we should currently displgravity
    #         app.spriteCounter = 1
    #         app.stepsPerSecond = 5

    def takeStep(self):
        self.accelerateTowardsPoint()
        self.y += self.characterSpeed

    def accelerate(self, gravity):
        self.characterSpeed += gravity

    def accelerateTowardsPoint(self):
    # Accelerate (change velocity) towards point
        gravity = 2
        self.accelerate(gravity)

    def drawCharacter(self):
        # drawRect(self.x, self.y, 15, 30, fill = self.fill)
        # drawImage(self.imagePath, self.x, self.y)
        newWidth, newHeight = (self.imageWidth, self.imageHeight)
        drawImage(self.image, self.x, self.y,
                  width = newWidth, height = newHeight)

    def adjustMove(self):
        if self.characterSpeed > 0:
            self.drop = False
            print("stop", self.drop)
        else:
            self.characterSpeed = -self.characterSpeed * 0.9
    
    def jumping(self):
        self.y -= self.characterSpeed
        self.characterSpeed = -20
        self.drop = True
    