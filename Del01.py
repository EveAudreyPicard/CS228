# -*- coding: cp1252 -*-

import sys
sys.path.insert(0, '/Users/Ève-Audrey/Documents/Leap_Motion_SDK_Windows_2.3.1/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x64')
import Leap


from pygameWindow import PYGAME_WINDOW
import constants
import random

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

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

def Handle_Frame(hand):
    global x,y,xMin,xMax,yMin,yMax
    hand = frame.hands[0]
    print(hand)

    fingers = hand.fingers
    indexFingerList = fingers.finger_type(Leap.Finger.TYPE_INDEX)
    indexFinger = indexFingerList[0]
    
    distalPhalanx = indexFinger.bone(Leap.Bone.TYPE_DISTAL)
    tip = distalPhalanx.next_joint
    x = int(tip[0])
    y = int(tip[1])
    print(tip)

    if ( x < xMin ):
        xMin = x
    if ( x > xMax ):
        xMax = x
    if ( y < yMin ):
        yMin = y
    if ( y > yMax ):
        yMax = y
    print xMin, xMax, yMin, yMax


def Scale_coordinate(var,new_min,new_max,old_min,old_max):
        return  var*((new_min-old_min)+(new_max-old_max))/300 + 400

        

    
pygameWindow = PYGAME_WINDOW()

x = constants.pygameWindowWidth/2
y = constants.pygameWindowDepth/2

controller = Leap.Controller()

while True:
       
    pygameWindow.Prepare()

    frame = controller.frame()
    if (len(frame.hands) > 0):
        Handle_Frame(frame)
        pygameX = Scale_coordinate(x,0,constants.pygameWindowWidth,xMin,xMax)
        print pygameX
        pygameY = Scale_coordinate(y,-constants.pygameWindowDepth,0,yMin,yMax)
        print pygameY
 
        pygameWindow.Draw_Black_Circle(pygameX,pygameY)
    #Perturb_Circle_Position()
    pygameWindow.Reveal()



    
    

