#10. Função Genérica de Filtragem
#Imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('vsc\pdi\imagem\img.png', 0)
def aplicar_filtro(imagem, kernel):
 return cv2.filter2D(imagem, -1, kernel)
kernel = np.ones((3,3)) / 9
resultado = aplicar_filtro(img, kernel)
plt.imshow(resultado, cmap='gray')
plt.show()