
import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("./c120.png")

# Gri tonlamalı bir görüntüye dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('1gray.png', gray)

# Median filtresi
blur_median = cv2.medianBlur(gray, 5)
cv2.imwrite('2blur_median.png', blur_median)

# Gaussian filtresi
blur_gaussian = cv2.GaussianBlur(gray, (9, 9), 0)
cv2.imwrite('3blur_gaussian.png', blur_gaussian)

# Histogram eşitleme
histogram_eql = cv2.equalizeHist(gray)
cv2.imwrite('4histogram_eql.png', histogram_eql)

# CLAHE (Kontrast Sınırlı Uyarlamalı Histogram Eşitleme)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_eql = clahe.apply(gray)
cv2.imwrite('5clahe_eql.png', clahe_eql)

# Kontrast genişletme
def pixel_val(pix, r1, s1, r2, s2):
	if (0 <= pix and pix <= r1):
		return (s1 / r1) * pix
	elif (r1 < pix and pix <= r2):
		return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
	else:
		return ((255 - s2) / (255 - r2)) * (pix - r2) + s2

r1 = 70
s1 = 0
r2 = 200
s2 = 255


pixel_val_func = np.vectorize(pixel_val)
contrast_stretched = pixel_val_func(gray, r1, s1, r2, s2)
contrast_stretched_blur_median = pixel_val_func(blur_median, r1, s1, r2, s2)

cv2.imwrite('6contrast_stretched.png', contrast_stretched)
cv2.imwrite('7contrast_stretched_blur_median.png', contrast_stretched_blur_median)

# Canny kenar dedektörü ile kenar tespiti
edge = cv2.Canny(gray, 100, 200)
cv2.imwrite('8edge.png', edge)

edge_gaussian = cv2.Canny(blur_gaussian, 100, 200)
cv2.imwrite('9edge_gaussian.png', edge_gaussian)

edge_median = cv2.Canny(blur_median, 100, 200)
cv2.imwrite('10edge_median.png', edge_median)

cv2.waitKey()
cv2.destroyAllWindows()
