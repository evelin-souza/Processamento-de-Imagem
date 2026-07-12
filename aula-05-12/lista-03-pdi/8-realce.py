#8.Filtro de Realce(Laplaciano)
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('vsc\pdi\imagem\img.png', 0)
kernel = np.array([[0, -1, 0],
 [-1, 4, -1],
 [0, -1, 0]])
realce = cv2.filter2D(img, -1, kernel)
plt.imshow(realce, cmap='gray')
plt.title("Realce (Laplaciano)")
plt.show()
