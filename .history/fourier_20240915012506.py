import numpy as np
import matplotlib.pyplot as plt

# Definindo os parâmetros
a = 1
b = np.pi / 2
x_values = np.linspace(-np.pi, np.pi, 400)

# Função para calcular a série de Fourier
def fourier_series(x, N):
    a0 = a * b / np.pi
    f_approx = a0 / 2
    for n in range(1, N+1):
        an = (2 * a * b / np.pi) / (n * n) * (1 - np.cos(n * b))
        f_approx += an * np.cos(n * x)
    return f_approx

# Plotando a série de Fourier para diferentes valores de N
for N in [10, 100]:
    y_values = fourier_series(x_values, N)
    plt.plot(x_values / np.pi, y_values, label=f'N={N}')

plt.title('Série de Fourier Aproximada')
plt.xlabel('x / π')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
