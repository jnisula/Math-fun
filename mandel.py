from math import *
from graphics import *
from operator import *

#graph window initialisation
width, height = 1800, 1000
    
win = GraphWin('Graphics', width, height)
win.setCoords(-width/2, -height/2, width/2, height/2)    
win.setBackground('Black')

#draw axii
xAxisLine = Line(Point(-width/2,0),Point(width/2,0))
xAxisLine.setOutline('lightgray')
xAxisLine.draw(win)
xAxisLine = Line(Point(0,-height/2),Point(0,height/2))
xAxisLine.setOutline('lightgray')
xAxisLine.draw(win)

pc = 200 # plotting multiplier
nMax = 650

def drawPoint(point, color1, color2):    
    point.setOutline(color_rgb(0,color1,color2))
    point.draw(win)
    
def main():

    tx = -2.0

    while (tx < 2.0):
        ty = -2.0
        while (ty < 2.0):
            # run the z1 = z^2 + c for each point n times
            zx = 0
            zy = 0
            
            n = 0
            while (sqrt(zx ** 2 + zy ** 2) < 2.0 and n < nMax):
                zx1 = zx ** 2 - zy ** 2 + tx
                zy1 = 2 * zx * zy + ty
                zx = zx1
                zy = zy1
                
                n = n + 1

            if (n >= nMax):
                color1 = 0
                color2 = 0 
            else:
                color1 = 0
                color2 = 255-n
                if (color2 < 0):
                    color2 = 0
                    
            
            drawPoint(Point(tx*pc,ty*pc),color1, color2)
            #if (n >= 600):
                #print(n)
            ty = ty + 0.01
        tx = tx + 0.01
        
    
    
main()
    
# x2 = r * x1 * (1 - x1)
