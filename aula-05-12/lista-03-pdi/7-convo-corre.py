#7. Convolução vs Corrlação
#Imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('vsc\pdi\imagem\img.png', 0)
kernel = np.ones((3,3), np.float32) / 9
# Correlação
corr = cv2.filter2D(img, -1, kernel)
# Convolução (kernel invertido)
kernel_conv = np.flipud(np.fliplr(kernel))
conv = cv2.filter2D(img, -1, kernel_conv)

plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(corr, cmap='gray')
plt.title("Correlação")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(conv, cmap='gray')
plt.title("Convolução")
plt.axis('off')

plt.show()