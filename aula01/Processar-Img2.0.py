#Importar bibliotecas (Import the libraries)
#Instala com 'pip install opencv-python matplotlib' (install with 'pip install opencv-python matplotlib')
import cv2 
import matplotlib.pyplot as plt 

#Carregar imagem (Load the image)
#Utilizado r'copy relative path'
img = cv2.imread(r'pdi\aula01\img.webp', 0)

#Caso a imagem não seja carregada, sair (Exit if the image is not loaded)
if img is None:
    print("Erro ao carregar a imagem")
    exit()


#Aplicar diferentes detectores de bordas (Apply different edge detectors)
sobel = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5) 
laplacian = cv2.Laplacian(img, cv2.CV_64F) 
canny = cv2.Canny(img, 100, 200)


#Imprimir resultado (Show the results)
plt.subplot(1, 4, 1), plt.title("Original P&B"), plt.imshow(img, cmap='gray') #Imagem original (Show the original image)
plt.subplot(1, 4, 2), plt.title("Sobel"), plt.imshow(sobel, cmap='gray')
plt.subplot(1, 4, 3), plt.title("Laplacian"), plt.imshow(laplacian, cmap='gray')
plt.subplot(1, 4, 4), plt.title("Canny"), plt.imshow(canny, cmap='gray')

plt.tight_layout() #Ajusta o layout das imagens para evitar sobreposição (Adjust the layout to avoid overlap)
plt.show()