#3. Correção Gama
#Imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('vsc\pdi\imagem\img.png', 0).astype(np.float32) / 255.0
gamma = 2.0
corrigida = np.power(img, gamma)
plt.imshow(corrigida, cmap='gray')
plt.title("Correção Gama (γ=2.0)")
plt.show()
