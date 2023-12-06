from cmu_graphics import *

#-----------MODULE 3 Obstacles--------------------------------------------------
class Obstacles:
    def __init__(self, recLeft, recTop, recWidth, recHeight, reccolor):
        self.recLeft = recLeft
        self.recTop = recTop
        self.recWidth = recWidth
        self.recHeight = recHeight
        self.reccolor = reccolor

def onAppStart(app):
    #make one of the Obstacles moving
    app.Obstacles = [ Obstacles(300, 700, 800, 20, 'red'),
                 Obstacles(0, 800, 250, 20, 'red'),
                 Obstacles(200, 900, 350, 20, 'pink'),
                 Obstacles(100, 500, 100, 20, 'darkSlateGray'),
                 Obstacles(0, 350, 500, 20, 'darkSlateGray'),
                 Obstacles(200, 550, 100, 20, 'darkSlateGray'),
                 Obstacles(300, 600, 300, 20, 'darkSlateGray'),
               ]
    
def redrawAll(app):

    drawLabel('Obstacles Example', 120, 50, size=25)
    drawLabel('Obstacles need to collide with the characters', 258, 80, size=25)
    # draw the Obstacles:
    for Obstacles in app.Obstacles:
        drawRect(Obstacles.recLeft, Obstacles.recTop, Obstacles.recWidth, Obstacles.recHeight, fill=Obstacles.reccolor)
        #drawLabel(str(Obstacles.count), Obstacles.rectLeft, Obstacles.rectTop)

# def onStep(app):
#     gravity = 0.98
#     app.playerSpeed += gravity
#     app.playerY += app.playerSpeed
#     for Obstacles in app.Obstacles:
#         if (app.playerY + app.playerHeight <= Obstacles.getplatformY()) and\
#            (app.playerY + app.playerHeight + app.playerSpeed > Obstacles.getPlatformY()) and\
#            (app.playerX + app.playerwidth > Obstacles.getplatformX()) and\
#            (app.playerX < Obstacles.getplatformX() + app.platformwidth):
#             app.playerY = Obstacles.getplatformY() - app.playerHeight
#             app.playerSpeed = -10

def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5


def main():
    runApp(width=800,height=500)

main()