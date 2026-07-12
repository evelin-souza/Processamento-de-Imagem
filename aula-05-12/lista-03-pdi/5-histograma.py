#5. Histograma
#Imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('vsc\pdi\imagem\img.png', 0)

plt.hist(img.ravel(), bins=256, range=[0,256])
plt.title("Histograma")
plt.show()