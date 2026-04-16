import cv2
import numpy as np

img = cv2.imread(r'pdi\aula31-03\img.png', cv2.IMREAD_COLOR)
N = 8 #niveis de cinza por canal
levels = np.linspace(0, 255, N, endpoint=True).astype(np.uint8)

#Metodo de quantizacao
def quantizar(img, N):
    bins = 250 // N
    q = (img // bins) * bins + bins//2
    return q.astype(np.uint8)


quant = quantizar(img, N)

cv2.imwrite("img_quantizar.png", quant)

Z = img.reshape((-1, 3)).astype(np.float32)
K = 16 #Numero de cores na paleta
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
_, label, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)
quant = centers[label.flatten()].reshape(img.shape)

cv2.imwrite("img_kmeans.png", quant)

#Amostragem

height, width = img.shape[:2]
#Downsample
down = cv2.resize(img, (width//4, height//4), interpolation=cv2.INTER_AREA)
cv2.imwrite("img_downsample_2x.png", down)
#Upsample
up = cv2.resize(img, (width*4, height*4), interpolation=cv2.INTER_NEAREST)
cv2.imwrite("img_upsample_2x.png", up)
