from math import *
from graphics import *
from operator import *

#graph window initialisation
width, height = 1800, 1200
    
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
nMax = 650

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
            
            zx = 0.0
            zy = 0.0
            n = 0
            while (sqrt(zx ** 2 + zy ** 2) < 2.0 and n < nMax):
                zx1 = zx ** 2 - zy ** 2 + tx
                zy1 = 2 * zx * zy + ty
                zx = zx1
                zy = zy1
                
                n = n + 1

            if (n >= nMax): #black
                red = 0
                green = 0
                blue = 0
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
                red = (n-36) * 20
                green = 0
                blue = 0
            elif (n <= 60): #blue+
                red = 255
                green = 0
                blue = (n-48) * 20
            else: #red-
                red = 255 - (n-60)
                green = 0
                blue = 255
                if (red < 0):
                    red = 0
                    
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
    xLimit = 0.6
    xStart = -2.0
    yStart = -1.5
    #iterate(xStart, yStart, xLimit, yLimit, pc, increment, 0, 0) #zoomed out
    ZCX = -1.4 #Zoom center x
    ZCY = 0.029 #Zoom center y
    ZW = 0.01 #Zoom wdth
    ZH = 0.01 #Zoom height
    pc = width / ZW
    increment = 2 / pc
    #print(str(ZCX - ZW/2) + " - " + str(pc))
    iterate(ZCX - ZW/2, ZCY - ZH/2, ZCX - ZW/2 + ZW, ZCY - ZH/2 + ZH, pc, increment, ZCX, ZCY) #zoomed in
    
main()
    
# x2 = r * x1 * (1 - x1)
