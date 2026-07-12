import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"vsc\pdi\imagem\img.png", cv2.IMREAD_GRAYSCALE)

#Aplica pseudocores usando mapa de cores
pseudo = cv2.applyColorMap(img, cv2.COLORMAP_JET)
#Converte BGR para RGB
pseudo = cv2.cvtColor(pseudo, cv2.COLOR_BGR2RGB)

#Exibição
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Pseudocores")
plt.imshow(pseudo)
plt.axis('off')

plt.show()