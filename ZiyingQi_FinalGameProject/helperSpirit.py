from cmu_graphics import *

class helperSpirit:
    def __init__(self, fill='yellow', cx=20, cy=20):
        # This sets the initial position of the dot:
        self.cx = cx
        self.cy = cy
        self.fill = fill

    def draw(self):
        drawLabel('Drag the mouse to move the spirit', 200, 30, size=16)
        drawLabel('If you put the spirit in the right place', 200, 50, size=12)
        drawLabel('it will help fireboy & watergirl to win the game.', 200, 70, size=12)
        drawCircle(self.cx, self.cy, 20, fill='yellow')

    def onMouseDrag(self, mouseX, mouseY):
        # This is called when the user moves the mouse
        # while it IS pressed:
        self.cx = mouseX
        self.cy = mouseY