import cv2
import matplotlib.pyplot as plt
imagem = cv2.imread(r"vsc\pdi\imagem\img.png", cv2.IMREAD_GRAYSCALE)

#tresholds = [[100, 200], [30, 100], [100, 200], [150,250]]
#for i in tresholds:
#    bordas = cv2.Canny(imagem,
#     threshold1=i[0],
#     threshold2=i[1])
#    plt.figure(figsize=(12,5))
#    plt.subplot(1,2,1)
#    plt.imshow(imagem, cmap='gray')
#    plt.title("Original")
#    plt.axis('off')
#    plt.subplot(1,2,2)
#    plt.imshow(bordas, cmap='gray')
#    plt.title(f"Canny {i[0]}-{i[1]}")
#    plt.axis('off')
#    plt.show()

bordas = cv2.Canny(imagem,
    threshold1=100,
    threshold2=200)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.imshow(imagem, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(bordas, cmap='gray')
plt.title("Canny")
plt.axis('off')
plt.show()