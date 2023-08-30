# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 01:06:58 2023

@author: dniso
"""

import cv2
import numpy as np

height = 512
width =512
img = np.random.randint(255,size=(height,width, 1),dtype=np.uint8)

cv2.imshow("Binary", img)

cv2.waitKey(0)
cv2.destroyAllWindows()