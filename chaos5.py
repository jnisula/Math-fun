from math import *
from graphics import *
from operator import *

def drawPoint2(point, win, n):    
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
def drawPoint(point, win, n):
    color = int(n / 5)
    point.setOutline(color_rgb(0,0,color))
    point.draw(win)
    
def main():
#graph window initialisation
    width, height = 1800, 1000
    offset = 0
    win = GraphWin('Graphics', width, height)
    #win.setCoords(-offset, -height/2, width-offset, height/2)
    win.setCoords(-offset, -40, width-offset, height-40)
    win.setBackground('White')
    xAxisLine = Line(Point(0,0),Point(1800,0))
    xAxisLine.setOutline('gray')
    xAxisLine.draw(win)

    yc = 900

    xAxisLine = Line(Point(0,yc),Point(1800,yc))
    xAxisLine.setOutline('gray')
    xAxisLine.draw(win)

    xAxisLine = Line(Point(0,0.5*yc),Point(1800,0.5*yc))
    xAxisLine.setOutline('gray')
    xAxisLine.draw(win)

    first = True
    
    x = 0.1
    r = 2.4
    n = 0
    while (r < 4.0):
        i = 0
        x = 0.1
        while (i < 200):
            #y = -6 * x ** 3 + 6 * x **2   #weird
            #y = x ** 3 - 3 * x ** 2 + 2 * x  #r can be > 4
            
            y = x   # simple
            
            if(y < 0.0 or y > 1.0):
                print ("Y: " + str(y))
            x = r * y * (1 - y)
            # - 6 x^3 + 6 x^2

            # x^3 - 3x^2 + 2x
            #if (x > 1):
                #print (str(r) + ", " + str(x))
            i = i + 1
            #if (abs(r - 1.95) < 0.0001):
            #    print (y)
            #    drawPoint(Point(n+i, x*yc), win, 1)

        #print ("---" + str(n) + "---")    
        cont = True
        x1 = x
        count = 0
        while (cont):
            drawPoint(Point(n*2, x*yc), win, count)
            
            #y = -6 * x ** 3 + 6 * x ** 2   #weird
            #y = x ** 3 - 3 * x ** 2 + 2 * x  #r can be > 4
            
            y = x   #simple
            
            x = r * y * (1 - y)
            count = count + 1
            if (abs(x - x1) < 0.001 or count > 500):
                cont = False
                if (x>0.0 and first):
                    xAxisLine = Line(Point(n*2,0),Point(n*2,yc))
                    xAxisLine.setOutline('gray')
                    xAxisLine.draw(win)
                    first = False
                    #print(x)
                #if (x == 0.0):
                #    print ("---" + str(r))
                #else:
                #    print (str(x) + " << >> " + str(x1))
        n = n + 1
        r = r + 0.002
        #print (str(r) + " -- " + str(n) + " -- " + str(x4))

main()
    
# x2 = r * x1 * (1 - x1)
