import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carrega a imagem em escala de cinza
img = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)

# Calcula o histograma da imagem
hist, bins = np.histogram(img.ravel(), 256, [0, 256])

# Exibe o histograma da imagem
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
