from math import *
from graphics import *
from operator import *

import numpy as np
import matplotlib.pyplot as plt

#graph window initialisation
width, height = 600, 400
    
win = GraphWin('Graphics', width, height)
win.setCoords(-width/2, -height/2, width/2, height/2)    
win.setBackground(color_rgb(0,0,255))

#draw axii
xAxisLine = Line(Point(-width/2,0),Point(width/2,0))
xAxisLine.setOutline('lightgray')
xAxisLine.draw(win)
xAxisLine = Line(Point(0,-height/2),Point(0,height/2))
xAxisLine.setOutline('lightgray')
xAxisLine.draw(win)


#print (pc)
#print (increment)
nMax = 1650

#red point to origin for verifying scaling
point = Point(0,0)
point.setOutline("red")
point.draw(win)

def drawPoint(point, red, green, blue):    
    point.setOutline(color_rgb(red, green, blue))
    point.draw(win)
    
def iterate(xStart, yStart, xLimit, yLimit, pc, increment, ZCX, ZCY):

    tx = xStart

    while (tx < xLimit):
        #print (tx)
        ty = yStart
        while (ty < yLimit):
            # run the z1 = z^2 + c for each point n times

            z = 0+0j
            z2 = 40.0+0j            
            n = 0
            same1 = False
            same2 = False
            while (abs(z) < 2.0 and n < nMax):
                c = tx + ty*1j
                
                z1 = z ** 2 + c
                
                
                if (same1 == False and abs(z - z1) < 0.001):
                    same1 = True
                if (same2 == False and abs(z1 - z2) < 0.001):
                    same2 = True
                    
                z2 = z

                z = z1
                
                n = n + 1

            if (n >= nMax): #black
                red = 180
                green = 180
                blue = 180
                if (same1):
                    red = 0
                    green = 0
                    blue = 0
                elif (same2):
                    red = 120
                    green = 60
                    blue = 40
            elif (n <= 12): #blue max -> green+
                red = 0
                green = n * 20
                blue = 255
            elif (n <= 24): #blue-
                red = 0
                green = 255
                blue = 255 - (n-12) * 20
            elif (n <= 36): #red+
                red = (n-24) * 20
                green = 255
                blue = 0
            elif (n <= 48): #green-
                red = 255
                green = (n-36) * 20
                blue = 0
            elif (n <= 60): #blue+
                red = 255
                green = 0
                blue = (n-48) * 20
            else: #red-
                red = 255 - (n-60)
                green = (n-60)
                blue = 255
                if (red < 0):
                    red = 0
                if (green > 255):
                    green = 255
                    
            if (n > 1):
                drawPoint(Point((tx-ZCX)*pc,(ty-ZCY)*pc),red, green, blue)                
                #drawPoint(Point(tx*pc,-ty*pc),red, green, blue)
                
            #if (n >= 600):
                #print(n)
            ty = ty + increment
            #print(str(tx) + "|" + str(ty))
        tx = tx + increment
        
def main():
    pc = width / 4 # plotting multiplier
    increment = 2 / pc
    yLimit = 1.5
    xLimit = 2
    xStart = -2.0
    yStart = -1.5
    iterate(xStart, yStart, xLimit, yLimit, pc, increment, 0, 0) #zoomed out
    ZCX = -1.4035 #Zoom center x
    ZCY = 0.0294 #Zoom center y
    ZW = 0.001 #Zoom wdth
    ZH = 0.001 #Zoom height
    pc = width / ZW
    increment = 2 / pc
    #print(str(ZCX - ZW/2) + " - " + str(pc))
    #iterate(ZCX - ZW/2, ZCY - ZH/2, ZCX - ZW/2 + ZW, ZCY - ZH/2 + ZH, pc, increment, ZCX, ZCY) #zoomed in
    
main()
    
# x2 = r * x1 * (1 - x1)
