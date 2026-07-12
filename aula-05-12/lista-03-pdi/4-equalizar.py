#4.Equalização de Imagem
#Imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('vsc\pdi\imagem\img.png', 0)
eq = cv2.equalizeHist(img)
plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title("Original")
plt.subplot(1,2,2), plt.imshow(eq, cmap='gray'), plt.title("Equalizada")
plt.show()