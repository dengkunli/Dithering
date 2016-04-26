# -*- coding: utf-8 -*-
'''
Created on Tue Apr 26 21:20:52 2016

@author: shenlin
              |    *  7 |
        1/16  |         |
              | 3  5  1 |
'''
from skimage import io, color, filters
import matplotlib.pyplot as plt
import threshold


img = io.imread("lenna.png")

img_gray = color.rgb2gray(img)


for y in range(0, img.shape[1]-1):
    for x in range(1, img.shape[0]-1):
      oldpixel = img_gray[x, y]
      img_gray[x, y] = 1 if oldpixel > 0.25 else 0
      quant_error = oldpixel - img_gray[x, y]
      img_gray[x+1, y  ] = img_gray[x+1, y  ] + 7/16.0 * quant_error
      img_gray[x-1, y+1] = img_gray[x-1, y+1] + 3/16.0 * quant_error
      img_gray[x,   y+1] = img_gray[x,   y+1] + 5/16.0 * quant_error
      img_gray[x+1, y+1] = img_gray[x+1, y+1] + 1/16.0 * quant_error
      
plt.figure(1)
plt.imshow(img_gray, cmap='Greys_r')
