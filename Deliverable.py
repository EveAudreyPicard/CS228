# -*- coding: cp1252 -*-

import numpy as np
import pickle
import sys
sys.path.insert(0, '/Users/Ève-Audrey/Documents/Leap_Motion_SDK_Windows_2.3.1/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x64')
import Leap
import constants
from pygameWindow_Del03 import PYGAME_WINDOW

    
class DELIVERABLE:
    
    def __init__(self):
        pass
        self.g =0
        self.xMin = 1000.0
        self.xMax = -1000.0
        self.yMin = 1000.0
        self.yMax = -1000.0
        self.zMin = 1000.0
        self.zMax = -1000.0
        self.x = constants.pygameWindowWidth/2
        self.y = constants.pygameWindowDepth/2
        self.pygameWindow = PYGAME_WINDOW()
        self.controller = Leap.Controller()
        self.previousNumberOfHands = 0
        self.currentNumberOfHands = 0
        self.gestureData = np.zeros((5,4,6),dtype='f')

    def Scale_coordinate(self,var,new_min,new_max,old_min,old_max):
        if old_min == old_max:
            return new_max/2
        else:
            return new_min + (var - old_min)*(new_max-new_min)/(old_max-old_min)

    def Handle_Vector_From_Leap(self,v):
        self.x = int(v[0])
        self.y = int(v[2])
        if ( self.x < self.xMin ):
            self.xMin = self.x
        if ( self.x > self.xMax ):
            self.xMax = self.x
        if ( self.y < self.yMin ):
            self.yMin = self.y
        if ( self.y > self.yMax ):
            self.yMax = self.y
            
        self.x = self.Scale_coordinate(self.x,0,constants.pygameWindowWidth,self.xMin,self.xMax)
        self.y = self.Scale_coordinate(self.y,0,constants.pygameWindowDepth,self.yMin,self.yMax)
        return self.x, self.y

    def Handle_Bone(self,bone,b,frame,fingerIndex):
        base = bone.prev_joint
        tip = bone.next_joint
        x_base, y_base = self.Handle_Vector_From_Leap(base)
        x_tip, y_tip = self.Handle_Vector_From_Leap(tip)
            
        if self.currentNumberOfHands == 1:
            color = (0,255,0)
        else:
            color = (255,0,0)        
        self.pygameWindow.Draw_Line(x_base,y_base,x_tip,y_tip,5-b,color)

        hand = frame.hands[0]
        fingers = hand.fingers

        j = b
        i = fingerIndex
        if self.Recording_Is_Ending():
            self.gestureData[i,j,0]= base[0]
            self.gestureData[i,j,1]= base[2]
            self.gestureData[i,j,2]= base[1]
            self.gestureData[i,j,3]= tip[0]
            self.gestureData[i,j,4]= tip[2]
            self.gestureData[i,j,5]= tip[1]

    def Handle_Finger(self,finger,frame,fingerIndex):
        for b in range(0,4): 
            self.Handle_Bone(finger.bone(b),b,frame,fingerIndex)
        
    def Handle_Frame(self,frame):
        fingerList = []
        hand = frame.hands[0]
        fingers = hand.fingers
        j = 0
        for finger in fingers:
            fingerList.append(finger)
            self.Handle_Finger(finger,frame,j)
            j = j + 1
        if self.Recording_Is_Ending():
            print(self.gestureData)
            self.Save_Gesture(self.g)
            self.g = self.g + 1

    def Run_Once(self):
        self.pygameWindow.Prepare()
        frame = self.controller.frame()
        self.currentNumberOfHands = len(frame.hands)
        if (len(frame.hands) > 0):
            self.Handle_Frame(frame)
            
        self.pygameWindow.Reveal()
        self.previousNumberOfHands = self.currentNumberOfHands
        
    def Run_Forever(self):
        while True:
            self.Run_Once()

    def Recording_Is_Ending(self):
        if self.currentNumberOfHands == 1 and self.previousNumberOfHands == 2:
            return True
        else:
            return False
        
    def Save_Gesture(self,g):
        pickle_out = open("userData/gesture"+ str(g) +".p",'wb')
        pickle.dump(self.gestureData,pickle_out)
        pickle_out.close()
