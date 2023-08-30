# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 02:16:22 2023

@author: dniso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

resim1 = cv2.imread("./batman.jpg")

hsvImage = cv2.cvtColor(resim1, cv2.COLOR_BGR2HSV)

plt.imshow(cv2.cvtColor(resim1, cv2.COLOR_BGR2RGB))
plt.title("Orijinal Görüntü")
plt.show()

plt.imshow(hsvImage)
plt.title("HSV Görüntü")
plt.show()
cv2.imwrite("BatmanHSV.jpg", hsvImage)
cv2.imshow("BatmanHSV", hsvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()