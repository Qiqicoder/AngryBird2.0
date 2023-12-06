from cmu_graphics import *
from PIL import Image


#-----------MODULE 3 Obstacles--------------------------------------------------
class Obstacles:
    def __init__(self, x = 100, y = 100, 
                 width = 200, height = 20, fill = 'brown'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill

    def drawObstacles(self): 
        chocolateColor = rgb(144,96,43)
        drawRect(self.x, self.y, self.width, self.height, fill = chocolateColor)

    def collisionField(self, character):
        if (self.x < character.x + character.imageWidth and
            character.x < self.x + self.width and
            self.y < character.y + character.imageHeight and
            character.y < self.y + self.height):
            return (self.x, self.x + self.width)
        else:
            return None
    # def randomObstaclesFunction(app):
    #     for 
#-----------MODULE 4 GameClearDoor----------------------------------------------
class GameClearDoor:
    def __init__(self, imagePath, x, y, fun, 
                 resizeFactor = 0.5,width = 50, height = 100, fill = ''):
        self.x = x
        self.y = y
        self.fun = fun
        self.width = width
        self.height = height
        self.fill = fill
        self.image = Image.open(imagePath)
        self.image = self.image.resize((int(self.image.width * resizeFactor), 
                                        int(self.image.height * resizeFactor)))
        self.imageWidth, self.imageHeight = self.image.width, self.image.height
        self.image = CMUImage(self.image)

    def drawDoor(self): 
        drawRect(self.x, self.y, self.width, self.height, fill = "red", opacity=0)
        drawImage(self.image, self.x, self.y)
    
def gameClearFunction(app):
    app.gameClearVisible = True

#-----------MODULE 5 Mechworks----------------------------------------------
class Mechworks:
    def __init__(self, imagePath, x, y, fun, 
                 resizeFactor = 0.2,width = 50, height = 100, fill = ''):
        self.x = x
        self.y = y
        self.fun = fun
        self.width = width
        self.height = height
        self.fill = fill
        self.image = Image.open(imagePath)
        self.image = self.image.resize((int(self.image.width * resizeFactor), 
                                        int(self.image.height * resizeFactor)))
        self.imageWidth, self.imageHeight = self.image.width, self.image.height
        self.image = CMUImage(self.image)

    def drawMechworks(self): 
        chocolateColor = rgb(144,96,43)
        drawRect(self.x-10, self.y+self.height-20, self.width+20, 20, fill = chocolateColor,opacity=0 )
        drawImage(self.image, self.x, self.y)

def MechworksOnFunction(app):
    app.MechworksOn = False