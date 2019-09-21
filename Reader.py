# -*- coding: cp1252 -*-

import pickle
import os
import constants
from pygameWindow_Del03 import PYGAME_WINDOW
import sys
sys.path.insert(0, '/Users/Ève-Audrey/Documents/Leap_Motion_SDK_Windows_2.3.1/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x64')
import Leap
import time

class READER:
    def __init__(self):
        self.xMin = 150.0
        self.xMax = -150.0
        self.yMin = 500.0
        self.yMax = -150.0
        self.pygameWindow = PYGAME_WINDOW()
        
    def Record_Files(self):
        path, dirs, files = next(os.walk('userData'))
        self.numGestures = len(files)

    def Print_Gestures(self):
        for p in range(0,self.numGestures):
            pickle_in = open("userData/gesture"+ str(p) +".p","rb")
            gestureData = pickle.load(pickle_in)
            print(gestureData)

    def Draw_Gestures(self):
        while True:
            self.Draw_Each_Gesture_Once()
        
    def Draw_Each_Gesture_Once(self):
        for current_gesture in range(0,self.numGestures):
            self.Draw_Gesture(current_gesture)

    def Draw_Gesture(self,current_gesture):
        self.pygameWindow.Prepare()
        pickle_in = open("userData/gesture"+ str(current_gesture) +".p","rb")
        gestureData = pickle.load(pickle_in)
        for i in range(0,5):
            for j in range(0,4):
                currentBone = gestureData[i,j,:]

                xBaseNotYetScaled = currentBone[0]
                yBaseNotYetScaled = currentBone[1]
                xTipNotYetScaled = currentBone[3]
                yTipNotYetScaled = currentBone[4]

                xBase = self.Scale_coordinate(xBaseNotYetScaled,0,constants.pygameWindowWidth,self.xMin,self.xMax)
                yBase = self.Scale_coordinate(yBaseNotYetScaled,0,constants.pygameWindowDepth,self.yMin,self.yMax)
                xTip = self.Scale_coordinate(xTipNotYetScaled,0,constants.pygameWindowWidth,self.xMin,self.xMax)
                yTip = self.Scale_coordinate(yTipNotYetScaled,0,constants.pygameWindowDepth,self.yMin,self.yMax)

                self.pygameWindow.Draw_Line(constants.pygameWindowWidth-xBase,constants.pygameWindowDepth-yBase,constants.pygameWindowWidth-xTip,constants.pygameWindowDepth-yTip,1,(0,0,255))
        self.pygameWindow.Reveal()
        time.sleep(0.5)

    def Scale_coordinate(self,var,new_min,new_max,old_min,old_max):
        if old_min == old_max:
            return new_max/2
        else:
            return new_min + (var - old_min)*(new_max-new_min)/(old_max-old_min)
