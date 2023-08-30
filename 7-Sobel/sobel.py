# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:16:09 2023

@author: dniso
"""

import cv2
import numpy as np

image = cv2.imread("./ColorfulBird.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Sobel filter
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
sobel = np.uint8(sobel)

# Save the output image
cv2.imwrite("sobel.jpg", sobel)