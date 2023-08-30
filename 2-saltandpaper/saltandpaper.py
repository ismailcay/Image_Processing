# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 00:23:47 2023

@author: dniso
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def tuz_biber_gurultusu_ekle(goruntu, gurultu_orani):
    gurultulu_goruntu = np.copy(goruntu)
    yukseklik, genislik, kanallar = gurultulu_goruntu.shape
    toplam_piksel = yukseklik * genislik
    gurultulu_piksel_sayisi = int(toplam_piksel * gurultu_orani)
    
    # Gurultu eklemek icin rastgele pikselleri secin
    tuz_pikseller = np.random.choice(toplam_piksel, gurultulu_piksel_sayisi, replace=False)
    biber_pikseller = np.random.choice(toplam_piksel, gurultulu_piksel_sayisi, replace=False)
    
    # Tuz gurultusu ekle (beyaz pikseller)
    gurultulu_goruntu.reshape(-1, kanallar)[tuz_pikseller] = 255
    
    # Biber gurultusu ekle (siyah pikseller)
    gurultulu_goruntu.reshape(-1, kanallar)[biber_pikseller] = 0
    
    return gurultulu_goruntu

fotograf = cv2.imread("./lena.png")

print(type(fotograf))
print(fotograf.shape)

gurultulu_fotograf = tuz_biber_gurultusu_ekle(fotograf, gurultu_orani=0.05)

plt.figure(figsize=(10, 10))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(fotograf, cv2.COLOR_BGR2RGB))
plt.title("Orijinal Görüntü")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(gurultulu_fotograf, cv2.COLOR_BGR2RGB))
plt.title("Gürültülü Görüntü")

plt.show()
