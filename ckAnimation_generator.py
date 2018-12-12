# -*- coding: utf-8 -*-
import ckAnimation_algorithms as aa

fileExt = ".ckAnimation"

description = "description"
filepath = ""
        
filepath = input("Filename > ")
description = input("Description > ")

if len(filepath) == 0:
    filepath = "animation"

if filepath[-len(fileExt):] != fileExt:
    filepath += fileExt
    
print("\nSelect the algorithm:")
for i in range(len(aa._registeredAlgorithms)):
    print(str(i) + " - " + str(aa._registeredAlgorithms[i].getName()))

algNum = 0
try:
    algNum = int(input("number > "))
except:
    algNum = 0

activeAlgorithm = aa._registeredAlgorithms[int(algNum)]()
activeAlgorithm.reset()
frameStrings = []
    
print("generation...")
for frame in range(activeAlgorithm.frameCount):
    num = frame+1
    tmpstr = "<Frame"+str(num)+"><ColorPicture>"
    
    for button in range(activeAlgorithm.buttonCount):
        tmpstr += activeAlgorithm.generate(frame, button)
        if button != activeAlgorithm.buttonCount-1:
            tmpstr += ","
            
    tmpstr += "</ColorPicture>\<DisplayTime>"+str(activeAlgorithm.displayTime)+"</DisplayTime>\n</Frame"+str(num)+">"
    frameStrings.append(tmpstr)
    
startString = "<Root><Description>"+description+" </Description><Time>0</Time><BackgroundColor>000000</BackgroundColor><FrameCount>"+str(activeAlgorithm.frameCount-1)+"</FrameCount>\n"
endString = "</Root>"

print("done...")

f = open(filepath, "w")
f.write(startString)
for i in range(activeAlgorithm.frameCount):
    f.write(frameStrings[i])
f.write(endString)
f.close()

input()