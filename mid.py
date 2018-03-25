from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
from copy import deepcopy

def getGrayColor(rgb):
    gray = int((int(rgb[0])+int(rgb[1])+int(rgb[2]))/3)
    return gray

def setGrayColor(color):
    color = int(color)
    return [color, color, color] 

size = 3
limit = int((size-1)/2)

file = input('Enter image name: ')
print('Hello', file)


#image gaussianNoise  

imgPep = Image.open('image/'+file+'.bmp')

imgPep = np.asarray(imgPep)
Mid = deepcopy(imgPep)

for i in range(limit,len(imgPep)-limit):
    for j in range(limit,len(imgPep[i])-limit):
        min= 256
        max= 0
        
        for k in range(i-limit, i+limit+1):
            for l in range(j-limit, j+limit+1):
                exe = getGrayColor(imgPep[k][l])
                
                if exe < min:
                    min =exe
                if exe > max:
                    max =exe

        Mid[i][j] = setGrayColor(1/2.0*(max+min))

plt.subplot(2, 2, 1)
plt.imshow(imgPep)
plt.subplot(2, 2, 2)
plt.imshow(Mid)
plt.show()
