from math import *
from graphics import *
from operator import *

#graph window initialisation
width, height = 1800, 1000
    
win = GraphWin('Graphics', width, height)
win.setCoords(-width/2, -height/2, width/2, height/2)    
win.setBackground('White')

#draw axii
xAxisLine = Line(Point(-width/2,0),Point(width/2,0))
xAxisLine.setOutline('gray')
xAxisLine.draw(win)
xAxisLine = Line(Point(0,-height/2),Point(0,height/2))
xAxisLine.setOutline('gray')
xAxisLine.draw(win)

def drawPoint(point, color):
    point.setOutline(color_rgb(0,0,color))
    point.draw(win)
    
def main():

    drawPoint(Point(0,0),199)
    
main()
    
# x2 = r * x1 * (1 - x1)
