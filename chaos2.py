from math import *
from graphics import *
from operator import *

def drawPoint(point, win):
    point.setOutline('lightblue')
    point.draw(win)
    
def main():
#graph window initialisation
    width, height = 1800, 500
    offset = 0
    win = GraphWin('Graphics', width, height)
    #win.setCoords(-offset, -height/2, width-offset, height/2)
    win.setCoords(-offset, 0, width-offset, height)
    win.setBackground('White')
    yc = 450

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

        cont = True
        x1 = x
        while (cont):
            drawPoint(Point(n*2, x*yc), win)
            
            x = r * (x - x * x)
            if (abs(x - x1) < 0.001):
                cont = False
                                            
        n = n + 1
        r = r + 0.005
        #print (str(r) + " -- " + str(n) + " -- " + str(x4))

main()
    
# x2 = r * x1 * (1 - x1)
