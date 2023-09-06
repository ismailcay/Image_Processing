# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 03:12:31 2023

@author: dniso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

resim1=cv2.imread("./eiffel.jpg")
grayscaleImage = cv2.cvtColor(resim1, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale Görüntü", grayscaleImage)

hsvImage = cv2.cvtColor(resim1, cv2.COLOR_BGR2HSV)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

ax1.imshow(cv2.cvtColor(resim1, cv2.COLOR_BGR2RGB))
ax1.set_title("Orijinal Görüntü")

ax2.imshow(hsvImage)
ax2.set_title("HSV Görüntü")

plt.show()
kaydetme_yolu_hsv = "./kaydedilen_hsv_goruntu.jpg"
cv2.imwrite(kaydetme_yolu_hsv, hsvImage)


print(resim1.size)   
print(resim1.dtype)
print(resim1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()