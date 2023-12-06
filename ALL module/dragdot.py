from cmu_graphics import *

def onAppStart(app):
    # This sets the initial position of the dot:
    app.cx = 20
    app.cy = 20

def redrawAll(app):
    drawLabel('Drag the mouse to move the dot', 200, 30, size=16)
    drawLabel('Also move the mouse while not pressed', 200, 50, size=12)
    drawLabel('and the dot will not move then.', 200, 70, size=12)
    drawCircle(app.cx, app.cy, 50, fill='yellow')

def onMouseDrag(app, mouseX, mouseY):
    # This is called when the user moves the mouse
    # while it IS pressed:
    app.cx = mouseX
    app.cy = mouseY

def main():
    runApp()

main()