# -*- coding: utf-8 -*-
import random
import math

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
        
        
class Algorithm:
    def __init__(self):
        self.frameCount = 50
        self.buttonCount = 116
        self.lastGenerated = (0.0, 0.0, 0.0)
        self.color = (0.0, 0.0, 0.0)
        self.displayTime = 0.05
        self.buttons = []
        
    def getName():
        return "[Unnamed]"
        
    def reset(self):
        for i in range(self.buttonCount):
            self.buttons.append(Key())
            
    def generate(self, frameNum, buttonNum):
        self.buttons[0].rgb2hex()
        
_registeredAlgorithms = []
def registerAlgorithm(alg):
    _registeredAlgorithms.append(alg)
       
class AlgDefault(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
    def getName():
        return "[default] sin()"
        
    def reset(self):
        Algorithm.reset(self)
        
    def generate(self, frameNum, buttonNum):
        f = math.sin((((math.pi*2)/self.frameCount)*frameNum)+buttonNum)
        b = self.buttons[buttonNum]
        f += 1 ; f /= 2 ; f *= 255;
        
        rgb = (f,f,f)

        b.setColor(rgb)
        
        return self.buttons[buttonNum].rgb2hex()
        
registerAlgorithm(AlgDefault)