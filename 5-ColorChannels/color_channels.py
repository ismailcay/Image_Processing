# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 02:16:22 2023

@author: dniso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./batman.jpg")

blue_channel = image[:, :, 0]
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

cv2.imwrite("blue_channel.jpg", blue_channel)
cv2.imwrite("green_channel.jpg", green_channel)
cv2.imwrite("red_channel.jpg", red_channel)

plt.imshow(blue_channel, cmap='gray')
plt.title("Blue Channel")
plt.show()

plt.imshow(green_channel, cmap='gray')
plt.title("Green Channel")
plt.show()

plt.imshow(red_channel, cmap='gray')
plt.title("Red Channel")
plt.show()
