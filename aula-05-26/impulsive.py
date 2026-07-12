import cv2
import numpy as np
import matplotlib.pyplot as plt

#Carregar imagens
img = cv2.imread(r'vsc\pdi\imagem\img.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'vsc\pdi\imagem\img.jpeg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(r'vsc\pdi\imagem\eve.jpg', cv2.IMREAD_GRAYSCALE)
#Ruido sal e pimenta
noise_prob = 0.05
noisy_img = np.copy(img)

#Ruido sal
salt = np.random.rand(*img.shape) < noise_prob
noisy_img[salt] = 255

#Ruido pimenta
pepper = np.random.rand(*img.shape) < noise_prob
noisy_img[pepper] = 1

#Restauração com filtro da mediana
restored_img = cv2.medianBlur(noisy_img, 15)

titles = ['Original', 'Ruido', 'Ruido 2.0']
images = [img, noisy_img, restored_img]


plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
