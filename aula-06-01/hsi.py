#COLOR MODELS#
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("vsc\pdi\imagem\img.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

H = np.arctan2((G - B), (R - G / 2 + B / 2))
S = np.sqrt((R - G) ** 2 + (R - B) * (G - B))
I = (R + G + B) / 3

plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1); plt.title("Red"); plt.imshow(R); plt.axis('off')
plt.subplot(1, 4, 2); plt.title("Green"); plt.imshow(G); plt.axis('off')
plt.subplot(1, 4, 3); plt.title("Blue"); plt.imshow(B); plt.axis('off')
plt.subplot(1, 4, 4); plt.title("rgb"); plt.imshow(img); plt.axis('off')

#plt.imshow(img)
plt.show()