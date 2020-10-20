from math import *
from graphics import *
from operator import *

def drawPoint(point, win):
    point.setOutline('lightblue')
    point.draw(win)
    
def main():
#graph window initialisation
    width, height = 800, 400
    offset = 0
    win = GraphWin('Graphics', width, height)
    win.setCoords(-offset, -height/2, width-offset, height/2)
    win.setBackground('White')
    yc = 150

    x = 0.1
    r = 0.9
    n = 0
    while (r < 4):
        i = 0
        x = 0.1
        while (i < 100):    
            x = r * (x - x * x)
            #print (str(n) + ", " + str(x))
            i = i + 1
            
        x = r * (x - x * x)
        x1 = x
        x = r * (x - x * x)
        x2 = x
        x = r * (x - x * x)
        x3 = x
        x = r * (x - x * x)
        x4 = x

        if (abs(x4 - x3) < 0.001):
            drawPoint(Point(n, x4*yc), win)
            
        elif (abs(x4 - x2) < 0.001):                
            drawPoint(Point(n, x3*yc), win)
            drawPoint(Point(n, x4*yc), win)
            
        elif (abs(x4 - x1) < 0.001):                
            drawPoint(Point(n, x2*yc), win)
            drawPoint(Point(n, x3*yc), win)
            drawPoint(Point(n, x4*yc), win)
            
        else:
            drawPoint(Point(n, x1*yc), win)
            drawPoint(Point(n, x2*yc), win)
            drawPoint(Point(n, x3*yc), win)
            drawPoint(Point(n, x4*yc), win)
                    
        n = n + 1
        r = r + 0.005
        print (str(r) + " -- " + str(n) + " -- " + str(x4))

main()
    
# x2 = r * x1 * (1 - x1)
