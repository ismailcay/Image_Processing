# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 02:47:09 2023

@author: dniso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("ColorfulBird.jpg")

kernel1 = np.ones((5, 5), np.float32) / 30

img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

# Orijinal resmi küçültülmüş boyutta görüntüleme
cv2.namedWindow('Orijinal', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Orijinal', 600, 600)
cv2.imshow('Orijinal', image)

# Kernel Blur uygulanmış resmi küçültülmüş boyutta görüntüleme
cv2.namedWindow('Kernel Blur', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Kernel Blur', 600, 600)
cv2.imshow('Kernel Blur', img)

cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('kernel_blurred_image.jpg', img)
plt.figure(figsize=(10, 10))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Orijinal Görüntü")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Gürültülü Görüntü")

plt.show()