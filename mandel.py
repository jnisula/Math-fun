from math import *
from graphics import *
from operator import *
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt

#graph window initialisation
width, height = 800, 800

nMax = 100

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
                red = 255
                green = (n-36) * 20
                blue = 0
            elif (n <= 60): #blue+
                red = 255
                green = 0
                blue = (n-48) * 20
            else: #red-
                red = 255 - (n-60)
                green = (n-60)
                blue = 255
                if (red < 0):
                    red = 0
                if (green > 255):
                    green = 255
                    
            if (n > 0):                
                pointMap[y][x] = (red, green, blue)
                                
            ty = ty + increment
        tx = tx + increment
    
    plt.imshow(pointMap, interpolation="nearest")
    plt.show()
    
    #img = Image.fromarray(pointMap)
    #img.save("mandelTest.png")
        
def main():
    size = 4
    increment = size / width
        
    start = (-2.0,-2.0)
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
