#Importar bibliotecas
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Carregar imagem
img = cv2.imread(r'pdi\aula02\img.jpeg', 0)

#Adicionar ruido artificial a imagem
noise = np.random.normal(0, 25, img.shape).astype('uint8')
noisy = cv2.add(img, noise)

#Imprimir imagens
print('Imagem original: ', img.shape)
print('Imagem com ruido:',noise.shape)
print('Imagem com ruido 2.0: ', noisy.shape)


#Aplicar diferentes filtros
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)


#Mostrar imagens criando uma aba para cada imagem
#cv2.imshow('Original', img)
#cv2.imshow('Com ruido', noise)
#cv2.imshow('Com ruido 2.0', noisy)
#cv2.imshow('Gaussiana', gaussian)
#cv2.imshow('Mediana', median)
#cv2.imshow('Bilateral', bilateral)
#cv2.waitKey(0)

#Mostrar imagens em uma mesma aba
plt.subplot(2, 3, 1), plt.title("Original"), plt.imshow(img, cmap='gray')
plt.subplot(2, 3, 2), plt.title("Com ruido"), plt.imshow(noise, cmap='gray')
plt.subplot(2, 3, 3), plt.title("Com ruido 2.0"), plt.imshow(noisy, cmap='gray')
plt.subplot(2, 3, 4), plt.title("Gaussiana"), plt.imshow(gaussian, cmap='gray')
plt.subplot(2, 3, 5), plt.title("Mediana"), plt.imshow(median, cmap='gray')
plt.subplot(2, 3, 6), plt.title("Bilateral"), plt.imshow(bilateral, cmap='gray')

plt.tight_layout() #Ajusta o layout das imagens para evitar sobreposição
plt.show()