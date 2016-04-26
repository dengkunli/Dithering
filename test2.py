# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 00:07:18 2016

@author: shenlin
"""

from skimage import io, color, filters
import matplotlib.pyplot as plt
import threshold
import errorDiffusion

img = io.imread("lenna.png")
tmp=img.copy()
plt.imshow(tmp)

