#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    ckAnimation generator by Felucca24.
    https://github.com/Felucca24/ckAnimation-generator
"""

import random
import math

random.seed()

KEY_COUNT = 105

row0 = [i for i in range(0,16)]  # 0 - 15
row1 = [i for i in range(16,37)] # 21
row2 = [i for i in range(37,58)] # 21
row3 = [i for i in range(58,74)] # 16
row4 = [i for i in range(74,91)] # 17
row5 = [i for i in range(91,104)] # 13

buttonRows = []
def buttonRowsSet(br):
    buttonRows.clear()
    for b in br: buttonRows.append(b)
    
    
class AnimCurve:
    def __init__(self, anim):
        self.animation = anim

class Key:
    def __init__(self):
        self.startColor = (0.0, 0.0, 0.0)
        self.lastColor = (0.0, 0.0, 0.0)
        self.color = (0.0, 0.0, 0.0)
        self.number = 0

    def setColor(self, _color):
        self.lastColor = self.color
        self.color = _color

    def randomise(self):
        r = lambda: random.randint(0,255)
        self.setColor((r(), r(), r()))

    def rgb2hex(self):
        return str('%02x%02x%02x' % (int(self.color[2]), int(self.color[1]), int(self.color[0]) ) ).upper()

class Frame:
    def __init__(self, bg = (0.0,0.0,0.0)):
        self.buttons = []
        self.displayTime = 0.05
        self.number = 0

        for i in range(KEY_COUNT):
            k = Key()
            k.number = i
            k.startColor = bg
            k.color = bg
            k.lastColor = bg
            self.buttons.append(k)
            
    def fill(self, rgb, resetStart = False):
        for button in self.buttons:
            button.color = rgb
            if resetStart:
                button.startColor = rgb
                button.lastColor = rgb


class Algorithm:
    def __init__(self, _frameCount, _startFill = (0.0, 0.0, 0.0)):  # In legacy classes, the standard value
        self.frameCount = _frameCount # of _frameCount must be specified.
        self.lastGenerated = (0.0, 0.0, 0.0)
        self.color = (0.0, 0.0, 0.0)
        self.frames = []

        for i in range(self.frameCount):
            fr = Frame()
            fr.fill(_startFill, True)
            fr.number = i
            self.frames.append(fr)

    def getName(self):
        return "[Unnamed]"

    def start(self):
        pass

_registeredAlgorithms = []
def registerAlgorithm(alg):
    _registeredAlgorithms.append(alg)


class Alg_Whitewaves(Algorithm):
    def __init__(self):
        Algorithm.__init__(self, 50)

    def getName(self):
        return "White waves"

    def start(self):
        print("Starting algorithm \"" + self.getName() + "\"")
            
        for frame in self.frames:
            for button in frame.buttons:
                f = math.sin((((math.pi*2)/self.frameCount)*frame.number)+button.number)
                f += 1 ; f /= 2 ; f *= 255;
                button.setColor((f,f,f))
                
        print("Algorithm done.")

registerAlgorithm(Alg_Whitewaves)


class Alg_Starfall(Algorithm):
    def __init__(self):
        r = lambda: random.randint(0,15)
        self.bg = ( 10+r(), 30+r(), 215+r() ) # 215 + 10 = 225;    |||    225 + ~30(by sin()) = 255
        
        Algorithm.__init__(self, 100, self.bg)

        # Generate random sin() offset for each button
        r2 = lambda: random.randint(0,40)
        self.sinOffset = [r2() for i in range(KEY_COUNT)]
        
        
        """
            The buttons are not exactly aligned,
            we have to adjust the coordinates so
            that the animation plays correctly.
        """
        global row0, row5, buttonRows
        row0.insert(0,0)
        row0 = row0[:6]+[i-1 for i in row0[6:15]] + [None for i in row0[15:]]
        row5 = [i+1 for i in row5[:2]] + [None, None, None, None, None, None, None] + [i-1 for i in row5[5:]]
        buttonRows = [row0, row1, row2, row3, row4, row5]


    def getName(self):
        return "Starfall"

    def start(self):
        print("Starting algorithm \"" + self.getName() + "\"")
        orange = (255, 100, 120)
        yellow = (255, 255, 0)
        
        class _Star:
            def __init__(self, _ff, _pos):
                self.x = _pos
                self.row = 0
                self.startFrame = _ff
                
                self.step = 0
                
                self.buttons = [buttonRows[self.row][self.x]]
                
                for i in range(5):
                    if self.x-1 >= 0 and self.row+1 <= 6:
                        self.x -= 1
                        self.row += 1
                        self.buttons.append(buttonRows[self.row][self.x])
                
                self.tempFullButtons = [None, None, None] + self.buttons + [None, None, None]
                
                self.buttons = self.tempFullButtons[self.step:self.step+3]
                
                self.fallen = False
                
            def nextStep(self):
                maxstep = 9
                
                self.buttons = self.tempFullButtons[self.step:self.step+3]

                self.step+=1
                if self.step > maxstep:
                    self.step = 0
                    self.fallen = True
                    
        fc = self.frameCount / 3;
        stars = [_Star(fc, 5), _Star(0, 8), _Star(fc*2, 14)]
        
        for frame in self.frames:
            for button in frame.buttons:
                f = math.sin((((math.pi*2)/self.frameCount)*frame.number)+self.sinOffset[button.number])
                f2 = math.sin((((math.pi*2)/self.frameCount)*frame.number)+self.sinOffset[button.number]+2.125) # 2.125 just random offset
                
                f += 1 ; f /= 2 ; f *= 30; # color difference
                f2 += 1.2 ; f2 *= 0.45 # bright difference

                col = self.bg
                
                r = col[0] + (f*0.6)
                g = col[1] + (1.0-f)
                b = col[2]
                
                r *= f2
                g *= f2
                b *= f2
                
                button.setColor((r, g, b))
                
            # Now generate the falling stars
            for star in stars:
                if frame.number >= star.startFrame and not star.fallen:
                    frame.displayTime *= 0.8 # Let's speed up frames with falling stars
                    for button in star.buttons: 
                        if button is not None:
                            frame.buttons[button].setColor(yellow)
                    if star.buttons[-1] is not None:
                        frame.buttons[star.buttons[-1]].setColor(orange)
                    star.nextStep()
        
        print("Algorithm done.")

registerAlgorithm(Alg_Starfall)








# Если приплюсовывать b = col[2] + f, то получаются бегающие оранжевые
# В остальных слуачаях - возникающие среди темноты фиолетовые с переливанием
# class Alg_Starfall(Algorithm):
    # def __init__(self):
        # r = lambda: random.randint(0,15)
        # self.bg = ( 20+r(), 30+r(), 210+r() ) # 215 + 10 = 225;    |||    225 + ~30(by sin()) = 255
        # Algorithm.__init__(self, 100, self.bg)

        
        # r2 = lambda: random.randint(0,40)
        # self.sinOffset = []
        # for i in range(KEY_COUNT):
            # self.sinOffset.append(r2())
        

    # def getName(self):
        # return "Starfall"

    # def start(self):
        # print("Starting algorithm \"" + self.getName() + "\"")
        
        # for frame in self.frames:
            # for button in frame.buttons:
                
                # f = math.sin((((math.pi*2)/self.frameCount)*frame.number)+self.sinOffset[button.number])
                # f2 = math.sin((((math.pi*2)/self.frameCount)*frame.number)+self.sinOffset[button.number]+2.125)
                # f += 1 ; f /= 2 ; f *= 35;
                # # f2 += 1 ; f2 /=2 ; f2 *= 20
                # print(f2)
                # col = self.bg
                
                # r = col[0] + f
                # g = col[1] + (1.0-f)
                # b = col[2]
                
                # r *= f2
                # g *= f2
                # b *= f2
                
                # button.setColor((r, g, b))
            
        # # Мерцание готово, теперь надо нафигачить звёзды. Это будет сложно.
        
        # orange = (255, 255, 120)
        # yellow = (255, 255, 0)
        
        # fc = self.frameCount / 3;

        # class _Star:
            # def __init__(self, _ff, _pos):
                # self.row = 0
                # self.startFrame = _ff
                
                # self.buttons = [buttonRows[0]]
                    
                
        # stars = [_Star(0, 5), _Star(fc, 7), _Star(fc*2, 12)]
        
        # # for frame in self.frames:
            # # for star in stars:
                
                
        
        # print("Algorithm done.")


