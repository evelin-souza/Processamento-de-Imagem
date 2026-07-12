import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread(r"vsc\pdi\imagem\img.png")

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

bordas = cv2.Canny(cinza,50,150)

linhas = cv2.HoughLinesP(
    bordas,
    rho=1,
    theta=np.pi/180,
    threshold=80,
    minLineLength=50,
    maxLineGap=10
)

resultado = imagem.copy()

if linhas is not None:
    for linha in linhas:
        x1,y1,x2,y2 = linha[0]
        cv2.line(resultado,(x1,y1),(x2,y2),(0,0,255),2)

plt.figure(figsize=(15,5))

plt.subplot(131)
plt.imshow(cv2.cvtColor(imagem,cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis('off')

plt.subplot(132)
plt.imshow(bordas,cmap='gray')
plt.title("Bordas")
plt.axis('off')

plt.subplot(133)
plt.imshow(cv2.cvtColor(resultado,cv2.COLOR_BGR2RGB))
plt.title("Linhas Detectadas")
plt.axis('off')

plt.show()