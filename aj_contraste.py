import cv2

# Carrega a imagem
img = cv2.imread('imagem_baixo_contraste.jpg')

# Converte a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calcula o histograma da imagem em escala de cinza
hist = cv2.calcHist([gray],[0],None,[256],[0,256])

# Calcula os valores mínimo e máximo do histograma
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(hist)

# Normaliza os valores de pixel da imagem para o intervalo [0, 255]
adjusted = cv2.normalize(gray, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Salva a imagem ajustada
cv2.imwrite('imagem_contraste_ajustado.jpg', adjusted)
