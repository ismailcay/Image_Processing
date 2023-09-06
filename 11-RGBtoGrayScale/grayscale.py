# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 04:06:25 2023

@author: dniso
"""

import cv2


resim1=cv2.imread("./cars.jpg")
grayscaleImage = cv2.cvtColor(resim1, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale Görüntü", grayscaleImage)
cv2.imwrite("GrayOutput.jpg", grayscaleImage)

print(resim1.size)   
print(resim1.dtype)
print(resim1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()