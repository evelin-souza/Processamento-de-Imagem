import cv2
import numpy as np
import matplotlib.pyplot as plt


#Carregar imagem
image = cv2.imread(r'pdi\aula04-14\img.png', cv2.IMREAD_GRAYSCALE)
#Normalizar a imagem para as intesidades ficarem entre [0, 1]
image = image / 255.0

#Criar uma máscara
mask = np.zeros_like(image)
#Definir uma região retangular dentro da imagem (ROI)
h, w = image.shape
mask[int(h*0.3):int(h*0.7), int(w*0.3):int(w*0.7)] = 1.0

#versao para imagem colorida:
#mask_color = np.dstack([mask, mask, mask])


#Aplicar a máscara na imagem
masked_image = image * mask

#Plotar as imagens
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1), plt.title("Original"), plt.imshow(image, cmap='gray'), plt.axis('off')
plt.subplot(1, 3, 2), plt.title("Máscara"), plt.imshow(mask, cmap='gray'), plt.axis('off')
plt.subplot(1, 3, 3), plt.title("Imagem com Máscara"), plt.imshow(masked_image, cmap='gray'), plt.axis('off')


plt.tight_layout()
plt.show()