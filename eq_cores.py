import cv2

# Carrega a imagem
img = cv2.imread('imagem_1.jpg')

# Converte a imagem de BGR para HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Separa o canal Hue (que representa a cor)
h, s, v = cv2.split(hsv)

# Calcula o histograma do canal Hue
hist = cv2.calcHist([h],[0],None,[256],[0,256])

# Equaliza o histograma para distribuir uniformemente as cores
eq_h = cv2.equalizeHist(h)

# Combina os canais novamente em uma imagem
eq_hsv = cv2.merge([eq_h, s, v])

# Converte a imagem de volta para BGR
result = cv2.cvtColor(eq_hsv, cv2.COLOR_HSV2BGR)

# Salva a imagem ajustada
cv2.imwrite('imagem_ajustada.jpg', result)
