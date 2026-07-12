import cv2
import numpy as np
import matplotlib.pyplot as plt

#Carregar imagens
img2 = cv2.imread(r'vsc\pdi\imagem\img.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread(r'vsc\pdi\imagem\img.jpeg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(r'vsc\pdi\imagem\eve.jpg', cv2.IMREAD_GRAYSCALE)


#Criar kernel de desfoque de moviemntos
size = 15
kernel = np.zeros((size, size))
kernel[int((size-1)/2), :] = np.ones(size)
kernel = kernel / size

#Aplicar desfoque
blurred = cv2.filter2D(img, -1, kernel)
blurred2 = cv2.filter2D(img2, -1, kernel)
blurred3 = cv2.filter2D(img3, -1, kernel)


#transformada de fourier
F_blurred = np.fft.fft2(blurred)
H = np.fft.fft2(kernel, s=img.shape)

#Evitar divisão por zero
epsilon = 1e-3
H = H + epsilon

#Filtragem inversa
F_restored = F_blurred / H #dominio da frequencia
restored = np.abs(np.fft.ifft2(F_restored)) #Volta ao dominio do espaço

#Normalizar
restored = np.clip(restored, 0, 255).astype(np.uint8)


titles = ['Original', 'desfoque movimento', 'restaurada']
images = [img, blurred, restored]


plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
