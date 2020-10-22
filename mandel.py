from math import *
from graphics import *
from operator import *
#from PIL import Image

import numpy as np
import matplotlib.pyplot as plt

#graph window initialisation
width, height = 800, 800

nMax = 3000

pointMap = np.zeros((height, width, 3), dtype=np.uint8)
    
def iterate(start, increment, ZCX, ZCY):
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

            m = n % 150
            if (n >= nMax): #black
                red = 0
                green = 0
                blue = 0                
            elif (m <= 25): #blue -> green+
                red = 0
                green = m % 25 * 10
                blue = 255
            elif (m <= 50): #cyan -> blue-
                red = 0
                green = 255
                blue = 255 - (m % 25) * 10
            elif (m <= 75): #green -> red+
                red = (m % 25) * 10
                green = 255
                blue = 0
            elif (m <= 100): #yellow -> green-
                red = 255
                green = 255 - (m % 25) * 10
                blue = 0
            elif (m <= 125): #red -> blue+
                red = 255
                green = 0
                blue = (m % 25) * 10
            elif (m <= 150): #magenta -> red-
                red = 255 - (m % 25) * 10
                green = 0
                blue = 255            
                    
            if (n > 0):                
                pointMap[y][x] = (red, green, blue)
                                
            ty = ty + increment
        tx = tx + increment
    
    plt.imshow(pointMap, interpolation="nearest")
    plt.show()
    
    #img = Image.fromarray(pointMap)
    #img.save("mandelTest.png")
        
def main():
    size = 0.000000000001
    const = 0.000000000003 *0.96
    const2 = 0.000000000003 *0.95
    start = (-1.26929999993 + const2,-0.18036999993 + const)

    ## whole:
    #size = 4
    #start = (-2.0,-2.0)

    increment = size / width
        
    
    iterate(start, increment, 0, 0) #zoomed out
    
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
