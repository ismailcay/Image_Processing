# -*- coding: utf-8 -*-
"""
Created on Aug  25 04:39:36 2023

@author: dniso
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

img = cv2.imread(r"./manzara.jpg",0).astype('float64')
img/=255.0

roberts_cross_v = np.array( [[1, 0 ],
                             [0,-1 ]] )
roberts_cross_h = np.array( [[ 0, 1 ],
                             [ -1, 0 ]] )

vertical = ndimage.convolve( img, roberts_cross_v )
horizontal = ndimage.convolve( img, roberts_cross_h )
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
edged_img*=255

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1), plt.imshow(img)
plt.title('Original')
plt.axis("off")
plt.subplot(1, 2, 2) ,plt.imshow(edged_img)
plt.title('Robert Cross')
plt.axis("off")
plt.show()
cv2.imwrite("RobertCross.jpg", edged_img)
cv2.imshow('Robert Cross', edged_img)

cv2.waitKey()
cv2.destroyAllWindows()