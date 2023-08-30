# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 02:29:34 2023

@author: dniso
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('manzara.jpg',0)


hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


equ = cv.equalizeHist(img)
res = np.hstack((img,equ))
cv.imwrite('res2.png',res)
