from math import *
from graphics import *
from operator import *
#from PIL import Image

import numpy as np
import matplotlib.pyplot as plt

#graph window initialisation
width, height = 200, 200

#nMax = 150
#nMax = 130

pointMap = np.zeros((height, width, 3), dtype=np.uint8)

def getColor(n, nMax):
    m = n % 150
    red = 0
    green = 0
    blue = 0

    if (n >= nMax): #black
        red = 0
        green = 0
        blue = 0                
    elif (m < 25): #blue -> green+
        red = 0
        green = m % 25 * 10
        blue = 255
    elif (m < 50): #cyan -> blue-
        red = 0
        green = 255
        blue = 255 - (m % 25) * 10
    elif (m < 75): #green -> red+
        red = (m % 25) * 10
        green = 255
        blue = 0
    elif (m < 100): #yellow -> green-
        red = 255
        green = 255 - (m % 25) * 10
        blue = 0
    elif (m < 125): #red -> blue+
        red = 255
        green = 0
        blue = (m % 25) * 10
    elif (m < 150): #magenta -> red-
        red = 255 - (m % 25) * 10
        green = 0
        blue = 255
    return red, green, blue

def iterate(start, increment, nMax):
    tx = start[0]

    for x in range(len(pointMap[0])):        
        ty = start[1]

        for y in range(len(pointMap)):                                
            # run the z1 = z^2 + c for each point n times

            z = 0+0j
            n = 0
            while (abs(z) < 2.0 and n < nMax):
                c = tx + ty*1j
                z = z ** 2 + c                
                n = n + 1

            if (n > 0):
                
                pointMap[y][x] = getColor(n, nMax)
                
            ty = ty + increment
        tx = tx + increment
            
def main():
    ## whole:
    center = (0.0, 0.0)
    size = 4
    i = 1    
    while (True):
        start = (center[0] - size/2, center[1] - size/2)
        print("start:" + str(start))
        increment = size / width
        print("Increment:" + str(increment))
        
        nMax = i * 200         
        print("nMax:" + str(nMax))
        
        iterate(start, increment, nMax)
        
        plt.imshow(pointMap, origin="lower", interpolation="nearest")
        points = plt.ginput(n=1, timeout=-1)
        print("Picked point:" + str(points))
        print("Picked point:" + str(points[0][0]) + ", " + str(points[0][1]))
        center = (start[0] + points[0][0]/width * size, start[1] + points[0][1]/height * size)
        print("Center:" + str(center))
        size = size / 5
        print("Size:" + str(size))
        i = i + 7 
            
main()
    
