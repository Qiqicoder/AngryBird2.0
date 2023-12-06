from cmu_graphics import *


def onAppStart(app):
    app.playerwidth,
    app.playerHeight = 30,30
    app.playerSpeed = -10
    app.fireBullets = False
    app.platformwidth, app.platformHeight = 150,20
    app.background = 'cornSilk'
    app.stepsPerSecond = 60
    app.playerX = app.width//2 - app.playerwidth//2
    app.playerY = app.height//2 - app.playerHeight//2
    app.gameOver = False
    app.leftPressed = False
    app.rightpressed = False
    chance = lambda x: not random.randint(0,x)

def redrawAll(app):
    for platform in level.getplatforms():
        platform.draw(app)
    # drawRect(app.width/2 - app.platformwidth/2,
    # app.height*2/3 - app.platformHeight/2,
    # app.platformwidth, app.platformHeight, fill = 'darkCyan')
    drawRect(app.playerx,app.playerY,
            app.playerWidth,app.playerHeight, 
            fill = 'mediumAquamarine')
    if app.gameOver == True:
        drawLabel('Game Over', app.width/2,app.height/2,
                    fill = 'Grey',size = 40, bold = True)
def onStep(app):
    gravity = 0.98
    app.playerSpeed += gravity
    app.playerY += app.playerSpeed
    for platform in level.getplatforms():
        if (app.playerY + app.playerHeight <= platform.getplatformY()) and\
           (app.playerY + app.playerHeight + app.playerSpeed > platform.getPlatformY()) and\
           (app.playerX + app.playerwidth > platform.getplatformX()) and\
           (app.playerX < platform.getplatformX() + app.platformwidth):
            app.playerY = platform.getplatformY() - app.playerHeight
            app.playerSpeed = -10

    """detect if new platforms need to be generated while scrolling the camera"""
    if level.getPlatforms()[-1].getplatformY() > app.height:
        level.generateplatforms()

    if app.playerY < app.height // 2:
        scrollAmount = app.height // 2 - app.playerY
        app.playerY += scrollAmount
        for platform in level.getplatforms():
            platform.y += scrollAmount

    maxSpeed = 30
    if app.playerSpeed > maxSpeed:
        app.playerSpeed = maxSpeed
    if app.leftPressed:
        app.playerX -= 4
    elif app.rightPressed:
        app.playerX += 4
    if app.playerY + app.playerHeight > app.height:
        app.gameOver = True


def main():
    runApp()

main()