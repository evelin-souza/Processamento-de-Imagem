import cv2
import matplotlib.pyplot as plt
# Carregar imagem em tons de cinza
imagem = cv2.imread(r"vsc\pdi\imagem\img.png", cv2.IMREAD_GRAYSCALE)
# Suavização
suave = cv2.GaussianBlur(imagem, (5,5), 0)
# Laplaciano
laplaciano = cv2.Laplacian(suave, cv2.CV_64F)
laplaciano = cv2.convertScaleAbs(laplaciano)
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.imshow(imagem, cmap='gray')
plt.title("Imagem Original")
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(laplaciano, cmap='gray')
plt.title("Filtro Laplaciano")
plt.axis('off')
plt.show()