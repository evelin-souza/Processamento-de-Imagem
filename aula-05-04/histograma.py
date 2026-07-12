#imports
import matplotlib.pyplot as plt
import cv2

#Carregar imagem

img = cv2.imread(r'pdi\aula-05-04\img.jpeg', cv2.IMREAD_COLOR)


#Calcular histograma em escala de cinza
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Histograma colorido
#for i, c in enumerate(('r', 'g', 'b')):
 #   plt.plot(cv2.calcHist([img], [i], None, [256], [0, 256]), color=c)
#plt.title("Color Histogram"), plt.xlabel("Itensidade"), plt.ylabel("Frequencia")

#Equalização de imagem
imgEqualized = cv2.equalizeHist(imgGray)

plt.subplot(1, 4, 1), plt.title("Grayscale"), plt.imshow(imgGray, cmap='gray'), plt.axis('off'), 
plt.subplot(1, 4, 2), plt.title("Gray Histogram"), plt.hist(imgGray.ravel(), 256, [0, 256], color='k'), plt.axis('off'), plt.xlabel("Itensidade"), plt.ylabel("Frequencia")
# 3. Imagem Equalizada
plt.subplot(1, 4, 3)
plt.title("Equalized")
plt.imshow(imgEqualized)
plt.axis('off')

# 4. Histograma Equalizado
plt.subplot(1, 4, 4)
plt.title("Equalized Histogram")
plt.hist(imgEqualized.ravel(), 256, [0, 256], color='c')
plt.xlabel("Intensidade")
plt.ylabel("Frequência")

plt.tight_layout()
plt.show()
