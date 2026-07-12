#9.Detecção de Bordas (Sobel)
#Imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('vsc\pdi\imagem\img.png', 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
bordas = np.sqrt(sobelx**2 + sobely**2)
plt.imshow(bordas, cmap='gray')
plt.title("Detecção de Bordas (Sobel)")
plt.show()