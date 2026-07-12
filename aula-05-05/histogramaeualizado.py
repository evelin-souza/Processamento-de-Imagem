import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carregar imagem
img = cv2.imread(r'pdi\imagem\img.png', cv2.IMREAD_GRAYSCALE)

# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro: A imagem não foi encontrada no caminho especificado.")
else:
    # Aplicar histograma equalizado
    image_equalized = cv2.equalizeHist(img)

    plt.figure(figsize=(12, 5))

    # Mostrar imagem original
    plt.subplot(1, 4, 1)
    plt.title("Original")
    plt.imshow(img, cmap='gray') 
    plt.axis('off')

    # Mostrar imagem equalizada
    plt.subplot(1, 4, 2)
    plt.title("Equalized")
    plt.imshow(image_equalized, cmap='gray')
    plt.axis('off')

    # Histograma da original
    plt.subplot(1, 4, 3)
    plt.title("Hist Original")
    plt.hist(img.ravel(), bins=256, range=[0, 256], color='black')

    # Histograma da equalizada
    plt.subplot(1, 4, 4)
    plt.title("Hist Equalized")
    plt.hist(image_equalized.ravel(), bins=256, range=[0, 256], color='black')

    plt.tight_layout()
    plt.show()