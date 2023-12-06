#-----------MODULE 3 Movement-------------------------------------

def redrawAll(app):
    sprite = app.sprites[app.spriteCounter]
    drawImage(sprite,200, 200, align = 'center')
    drawLabel('obstacles Example', 200, 30, size=16)
    drawLabel('Click in obstacles to change their count', 200, 50)
    # draw the obstacles:
    for obstacles in app.obstacles:
        drawRect(obstacles.recLeft, obstacles.recTop, obstacles.recWidth, obstacles.recHeight, fill=obstacles.reccolor)
        #drawLabel(str(obstacles.count), obstacles.rectLeft, obstacles.rectTop)