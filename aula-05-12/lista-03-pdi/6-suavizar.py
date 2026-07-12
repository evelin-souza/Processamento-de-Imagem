#6. Filtragem Espacial
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('vsc\pdi\imagem\img.png', 0)
kernel = np.ones((3,3), np.float32) / 9
suave = cv2.filter2D(img, -1, kernel)
plt.imshow(suave, cmap='gray')
plt.title("Filtro de Média")
plt.show()
