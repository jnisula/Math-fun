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

pc = 450 # plotting multiplier
increment = 2 / pc
yLimit = 1.3
xUpperLimit = 0.6
print (pc)
print (increment)
nMax = 650

#red point to origin for verifying scaling
point = Point(0,0)
point.setOutline("red")
point.draw(win)

def drawPoint(point, red, green, blue):    
    point.setOutline(color_rgb(red, green, blue))
    point.draw(win)
    
def main():

    tx = -2.0

    while (tx < xUpperLimit):
        ty = 0#-yLimit
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

            if (n >= nMax):
                red = 0
                green = 0
                blue = 0
            elif (n <= 12):
                red = 0
                green = n * 20
                blue = 255
            elif (n <= 24):
                red = (n-12) * 20
                green = 255
                blue = 255
            elif (n <= 36):
                red = (n-24) * 20
                green = 0
                blue = 255
            elif (n <= 48):
                red = (n-36) * 20
                green = 0
                blue = 0
            else:
                red = 255
                green = 255
                blue = 255-n
                if (blue < 0):
                    blue = 0
                    
            if (n > 3):
                drawPoint(Point(tx*pc,ty*pc),red, green, blue)
                drawPoint(Point(tx*pc,-ty*pc),red, green, blue)
                
            #if (n >= 600):
                #print(n)
            ty = ty + increment
        tx = tx + increment
        
    
    
main()
    
# x2 = r * x1 * (1 - x1)
