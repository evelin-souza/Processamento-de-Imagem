import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("vsc\pdi\imagem\img.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Imagem separada nos tres canais

R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

#Exibir RGB

plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1); plt.title("Red"); plt.imshow(R); plt.axis('off')
plt.subplot(1, 4, 2); plt.title("Green"); plt.imshow(G); plt.axis('off')
plt.subplot(1, 4, 3); plt.title("Blue"); plt.imshow(B); plt.axis('off')
plt.subplot(1, 4, 4); plt.title("rgb"); plt.imshow(img); plt.axis('off')

plt.show()

def rgb_to_hsi(img):
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]
    numerator = 0.5((R - G) + (R - B))
    denominator = np.sqrt((R - G) ** 2 + (R - B) * (G - B))
    theta = np.arccos(np.clip(numerator / denominator + 1e-8), -1, 1)

    H = np.where(B <= G, theta, 2 * np.pi - theta)
    H = H / (2 * np.pi)

    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (3/ (R + G + B+ 1e-8)) * min_rgb

    I = (R + G + B) / 3
    return H, S, I