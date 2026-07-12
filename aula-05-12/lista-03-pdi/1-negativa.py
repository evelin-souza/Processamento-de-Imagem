#1. Transformação Negativa da Imagem
#Imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('vsc\pdi\imagem\img.png', 0) # escala de cinza
L = 256
negativa = (L - 1) - img
plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title("Original")
plt.subplot(1,2,2), plt.imshow(negativa, cmap='gray'), plt.title("Negativa")
plt.show()
