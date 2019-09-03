from pygameWindow import PYGAME_WINDOW
import constants
import random

def Perturb_Circle_Position():
    global x, y
    fourSidedDieRoll = random.randint(1,4)
    if fourSidedDieRoll == 1:
        x = x - 1
    elif fourSidedDieRoll == 2:
        x = x + 1
    elif fourSidedDieRoll == 3:
        y = y - 1
    else:
        y = y + 1

pygameWindow = PYGAME_WINDOW()

x = constants.pygameWindowWidth/2
y = constants.pygameWindowDepth/2

while True:
    pygameWindow.Prepare()
    pygameWindow.Draw_Black_Circle(x,y)
    Perturb_Circle_Position()
    pygameWindow.Reveal()



    
    

