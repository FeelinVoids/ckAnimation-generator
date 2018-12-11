# -*- coding: utf-8 -*-
import random
import math

fileExt = ".ckAnimation"

description = "abc"
filepath = "firstAnim"
filepath = input("Filename > ")
description = input("Description > ")

displayTime = 0.1

if filepath[-len(fileExt):] != fileExt:
    filepath += fileExt
    
BUTTON_COUNT = 116
FRAMES_COUNT = 100

random.seed()
    
class Key:
    def __init__(self):
        self.startColor = (0.0, 0.0, 0.0)
        self.lastColor = (0.0, 0.0, 0.0)
        self.color = (0.0, 0.0, 0.0)
        
    def setColor(self, _color):
        self.lastColor = self.color
        self.color = _color
        
    def randomise(self):
        r = lambda: random.randint(0,255)
        self.setColor((r(), r(), r()))
        
    def rgb2hex(self):
        return str('%02x%02x%02x' % (int(self.color[0]), int(self.color[1]), int(self.color[2]) ) ).upper()

buttons = []

for i in range(BUTTON_COUNT):
    buttons.append(Key())


def generate_algorithm(frameNum, buttonNum):
    f = math.sin((((math.pi*2)/FRAMES_COUNT)*frameNum)+buttonNum)
    b = buttons[buttonNum]
    f += 1 ; f /= 2 ; f *= 255;
    
    rgb = (f,f,f)

    b.setColor(rgb)
    
    return buttons[buttonNum].rgb2hex()

frameStrings = []
    
for frame in range(FRAMES_COUNT):
    num = frame+1
    tmpstr = "<Frame"+str(num)+"><ColorPicture>"
    
    for button in range(BUTTON_COUNT):
        tmpstr += generate_algorithm(frame, button)
        if button != BUTTON_COUNT-1:
            tmpstr += ","
            
    tmpstr += "</ColorPicture>\<DisplayTime>"+str(displayTime)+"</DisplayTime>\n</Frame"+str(num)+">"
    frameStrings.append(tmpstr)
    
startString = "<Root><Description>"+description+" </Description><Time>0</Time><BackgroundColor>000000</BackgroundColor><FrameCount>"+str(FRAMES_COUNT-1)+"</FrameCount>\n"
endString = "</Root>"

f = open(filepath, "w")
f.write(startString)
for i in range(FRAMES_COUNT):
    f.write(frameStrings[i])
f.write(endString)
f.close()