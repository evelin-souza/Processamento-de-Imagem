#2. Transformação Logarítmica
#Imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('vsc\pdi\imagem\img.png', 0).astype(np.float32)
c = 255 / np.log(1 + np.max(img))
log_img = c * np.log(1 + img)
log_img = np.uint8(log_img)
plt.imshow(log_img, cmap='gray')
plt.title("Transformação Logarítmica")
plt.show()
