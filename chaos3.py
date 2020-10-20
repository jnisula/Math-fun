from math import *
from graphics import *
from operator import *

def drawPoint(point, win, n):    
    if (n==0):
        colno = "black"
    elif (n==1):
        colno = "gray"
    elif (n==2):
        colno = "blue"
    elif (n==3):
        colno = "green"
    elif (n==4):
        colno = "lightblue"
    elif (n==5):
        colno = "lightgreen"
    else:
        colno = "red"
    point.setOutline(colno)
    point.draw(win)
    
def main():
#graph window initialisation
    width, height = 1800, 1000
    offset = 0
    win = GraphWin('Graphics', width, height)
    #win.setCoords(-offset, -height/2, width-offset, height/2)
    win.setCoords(-offset, 0, width-offset, height)
    win.setBackground('White')
    xAxisLine = Line(Point(0,0),Point(1800,0))
    xAxisLine.setOutline('gray')
    xAxisLine.draw(win)

    yc = 900

    xAxisLine = Line(Point(0,yc),Point(1800,yc))
    xAxisLine.setOutline('gray')
    xAxisLine.draw(win)

    

    x = 0.1
    r = 0.9
    n = 0
    while (r < 4):
        i = 0
        x = 0.1
        while (i < 100):    
            x = r * x * (1 - x )
            #print (str(n) + ", " + str(x))
            i = i + 1

        cont = True
        x1 = x
        count = 0
        while (cont):
            drawPoint(Point(n*2, x*yc), win, count)
            
            x = r * x * (1 - x )
            count = count + 1
            if (abs(x - x1) < 0.001):
                cont = False
                                            
        n = n + 1
        r = r + 0.005
        #print (str(r) + " -- " + str(n) + " -- " + str(x4))

main()
    
# x2 = r * x1 * (1 - x1)
