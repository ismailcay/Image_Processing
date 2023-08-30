# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 04:54:17 2023

@author: dniso
"""

import cv2
import numpy as np

def gaussian_noise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    return noisy

img = cv2.imread("./camera.jpg")
img = img / 255
noise_img = gaussian_noise(img)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Noise", noise_img)

cv2.imwrite("noisy_image.jpg", noise_img * 255)

cv2.waitKey(0)
cv2.destroyAllWindows()
