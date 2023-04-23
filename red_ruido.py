import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread('imagem_ruidosa.png')

# Aplica o filtro de mediana com tamanho da janela 5x5
filtered = cv2.medianBlur(img, 5)

# Salva a imagem filtrada
cv2.imwrite('imagem_filtrada.jpg', filtered)
