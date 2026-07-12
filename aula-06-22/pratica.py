import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'pdi\imagem\img.png', cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY).astype(np.uint8)

plt.figure(figsize=(6,6))
plt.imshow(img, cmap='gray');plt.title("Original"); plt.axis('off');plt.show()

diferenca = np.zeros_like(img, dtype=int)
for y in range (img.shape[0]):
    for x in range (img.shape[1]):
        diferenca[y,x] = (int(img[y,x - 1]))

diferenca_visual = diferenca + 128

plt.figure(figsize=(6,6))
plt.imshow(diferenca_visual, cmap='gray');plt.title("Diferenca"); plt.axis('off');plt.show()

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.hist(img.ravel(), bins=256),plt.title("Histograma img Original")

plt.subplot(1,2,2)
plt.hist(diferenca_visual.ravel(), bins=256),plt.title("Histograma diferenca")

plt.show()

unique_original = len(np.unique(img))
unique_diferenca = len(np.unique(diferenca_visual))

print("Quantidade de níveis:")
print("Quantidade de intensidades original: ", unique_original)
print("Quantidade de intensidades diferenca: ", unique_diferenca)