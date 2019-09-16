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

def Scale_coordinate(var,new_min,new_max,old_min,old_max):
    if old_min == old_max:
        return new_max/2
    else:
        return new_min + (var - old_min)*(new_max-new_min)/(old_max-old_min)

def Handle_Vector_From_Leap(v):
    global xMin,xMax,yMin,yMax
    x = int(v[0])
    y = int(v[2])
    if ( x < xMin ):
        xMin = x
    if ( x > xMax ):
        xMax = x
    if ( y < yMin ):
        yMin = y
    if ( y > yMax ):
        yMax = y
        
    x = Scale_coordinate(x,0,constants.pygameWindowWidth,xMin,xMax)
    y = Scale_coordinate(y,0,constants.pygameWindowDepth,yMin,yMax)
    return x, y

def Handle_Bone(bone,b):
    base = bone.prev_joint
    tip = bone.next_joint
    x_base, y_base = Handle_Vector_From_Leap(base)
    x_tip,y_tip = Handle_Vector_From_Leap(tip)
    pygameWindow.Draw_Black_Line(x_base,y_base,x_tip,y_tip, 5-b)

def Handle_Finger(finger):
    for b in range(0,4):
        Handle_Bone(finger.bone(b),b)
    

def Handle_Frame(hand):
    pass
    fingerList = []
    hand = frame.hands[0]

    fingers = hand.fingers
    for finger in fingers:
        fingerList.append(finger)
        Handle_Finger(finger)

pygameWindow = PYGAME_WINDOW()

x = constants.pygameWindowWidth/2
y = constants.pygameWindowDepth/2

controller = Leap.Controller()

while True:
       
    pygameWindow.Prepare()

    frame = controller.frame()
    if (len(frame.hands) > 0):
        Handle_Frame(frame)
    
    pygameWindow.Reveal()



    
    

