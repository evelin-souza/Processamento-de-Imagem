import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'vsc\pdi\imagem\img.png', cv2.IMREAD_GRAYSCALE)

#carrega imagem rgb de saida
pseudo = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)


#Fatiamento de intensidade
pseudo[(img >= 0) & (img <= 63)] = [0, 0, 255]       # Azul
pseudo[(img >= 64) & (img <= 127)] = [0, 255, 0]     # Verde
pseudo[(img >= 128) & (img <= 191)] = [255, 255, 0]  # Amarelo
pseudo[(img >= 192) & (img <= 255)] = [255, 0, 0]    # Vermelho

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Fatiamento de Intensidade")
plt.imshow(pseudo)
plt.axis('off')

plt.show()
