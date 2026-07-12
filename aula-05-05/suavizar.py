import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carregar imagem
img = cv2.imread(r'pdi\imagem\img.png', cv2.IMREAD_GRAYSCALE)

kernel_3x3 = np.ones((3, 3), np.float32) / 9
kernel_5x5 = np.ones((5, 5), np.float32) / 25
kernel_7x7 = np.ones((7, 7), np.float32) / 49

# Aplicar suavização
img_3x3 = cv2.filter2D(img, -1, kernel_3x3)
img_5x5 = cv2.filter2D(img, -1, kernel_5x5)
img_7x7 = cv2.filter2D(img, -1, kernel_7x7)

#ou img_3x3 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

plt.figure(figsize=(12, 5))

# Mostrar imagem original
plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(img, cmap='gray') # Adicionado cmap='gray'
plt.axis('off')

# Mostrar imagem suavizada com kernel 3x3
plt.subplot(1, 4, 2)
plt.title("Suavizada 3x3")
plt.imshow(img_3x3, cmap='gray') # Adicionado cmap='gray'
plt.axis('off')

# Mostrar imagem suavizada com kernel 5x5
plt.subplot(1, 4, 3)
plt.title("Suavizada 5x5")
plt.imshow(img_5x5, cmap='gray') # Adicionado cmap='gray'
plt.axis('off')

# Mostrar imagem suavizada com kernel 7x7
plt.subplot(1, 4, 4)
plt.title("Suavizada 7x7")
plt.imshow(img_7x7, cmap='gray') # Adicionado cmap='gray'
plt.axis('off')

plt.show()