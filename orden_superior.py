import math
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada
x = [0.1 ,0.4, 0.5, 0.7, 0.7, 0.9]
y = [0.61, 0.92, 0.99, 1.52, 1.47, 2.03]

m = 2
ni = 6

# Inicializar matrices
z1 = [[0.0 for n in range(m + 1)] for n in range(m + 1)]
z2 = [0.0 for n in range(m + 1)]

# Función para calcular la suma de xi^k
def fun(xi, k):
    f = 0.0
    for x_i in xi:
        f += pow(x_i, k)
    return f

# Función para calcular la suma de (xi^k * yi)
def mul(xi, yi, k):
    f = 0.0
    for x_i, y_i in zip(x, y):
        f += pow(x_i, k) * y_i
    return f

# Calcular las matrices z1 y z2
for i in range(m + 1):
    for j in range(m + 1):
        z1[i][j] = fun(x, i + j)
        z1[j][i] = fun(x, i + j)
    z2[i] = mul(x, y, i)

# Imprimir la matriz z1
for z1i in z1:
  print(z1i, end='\n')

# Imprimir la matriz z1
for z2i in z2:
  print(z2i, end='\n')

# Convertir las matrices en arrays de numpy
A = np.array(z1)
B = np.array(z2)

# Calcular la inversa de A
A_inv = np.linalg.inv(A)

# Calcular el vector de coeficientes g
g = np.dot(A_inv, B)

# Función para evaluar el polinomio en un punto xi
def pol(xi):
    f = 0.0
    for i in range(len(g)):
        f += g[i] * pow(xi, i)
    return f

# Calcular los valores del polinomio para los puntos x
polinomio = [pol(xi) for xi in x]

# Imprimir polinomio
#for po in polinomio:
#  print(po, end='\n')

# Invertir los coeficientes para que coincidan con la convención numpy
coeficiente = g[::-1]

# Crear un rango de puntos x para trazar la curva
x_rango = np.linspace(min(x), max(x), 6)
print(x_rango)

# Evaluar el polinomio en el rango de puntos x
yy = np.polyval(coeficiente, x_rango)

# Crear el gráfico
plt.scatter(x, y, color='red', label='un punto dato')  # Graficar los puntos
plt.plot(x_rango, yy, label='Polinomio')  # Graficar la curva

# Configurar el gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de puntos y una curva')
plt.legend()

plt.show()
