import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from matplotlib.colors import LogNorm

# Função para exibir a imagem em escala de cinza
def show_gray(img, title):
    plt.figure(figsize=(12,10))
    plt.title(title)
    plt.imshow(img, cmap='gray')  # Exibe a imagem em escala de cinza
    plt.colorbar()
    plt.show()                   # Mostra a figura

# Função para exibir o espectro com normalização logarítmica
def show_spect(IMG, title):
    plt.figure(figsize=(12,10))
    plt.title(title)
    
    # Calcula o espectro absoluto e substitui valores muito baixos por 1e-6
    spectrum = np.abs(IMG)
    spectrum = np.maximum(spectrum, 1e-6)  # Substitui valores muito baixos para evitar log(0)

    plt.imshow(spectrum, norm=LogNorm(vmin=1e-6))  # Use LogNorm com vmin=1e-6
    plt.colorbar()
    plt.show()                   # Mostra a figura

# Caminho para o arquivo da imagem
path = '/home/meteoro/Descargas/'
# Lê a imagem e converte para float
img = plt.imread(path + 'Dark.png').astype(float)

# Diagnóstico: Verifica se a imagem foi carregada corretamente
print(f"Imagem carregada com forma: {img.shape}")

# Exibe a imagem original
show_gray(img, "Original")

# Aplica a FFT à imagem
IMG = fftpack.fft2(img)
# Desloca a componente de baixa frequência para o centro
IMG_shift = fftpack.fftshift(IMG)

# Diagnóstico: Verifica a forma das transformações
print(f"Forma da Transformada de Fourier: {IMG.shape}")
print(f"Forma da Transformada de Fourier com Shift: {IMG_shift.shape}")

# Exibe o espectro de frequências antes do deslocamento
show_spect(IMG, "Transformada de Fourier")

# Exibe o espectro de frequências após o deslocamento
show_spect(IMG_shift, "Transformada de Fourier com Shift")

# Cria uma máscara de filtro de frequência
h, w = IMG_shift.shape[:2]          # Obtém as dimensões da imagem
Y, X = np.ogrid[0:h, 0:w]          # Cria uma grade de coordenadas para a imagem
mask = np.sqrt(((X - w / 2)**2 + (Y - h / 2)**2))  # Calcula a distância das frequências ao centro

# Exibe a máscara usada para filtrar
show_spect(mask, "Máscara")

# Aplica o filtro à imagem no domínio da frequência
IMG_shift[mask > 0.1 * w] = 0
# Exibe o espectro de frequências após a aplicação do filtro
show_spect(IMG_shift, "Frequência Filtrada")

# Aplica a Transformada Inversa de Fourier para obter a imagem filtrada
img_filtered = fftpack.ifft2(fftpack.ifftshift(IMG_shift)).real

# Exibe a imagem filtrada
show_gray(img_filtered, "Imagem Filtrada")
