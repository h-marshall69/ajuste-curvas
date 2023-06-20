import math
import numpy as np
import matplotlib.pyplot as plt

x = [0.1 ,0.4, 0.5, 0.7, 0.7, 0.9]
y = [0.61, 0.92, 0.99, 1.52, 1.47, 2.03]
z = [0.0 for n in range(4)]

ni = len(x)

for i in range(6):
    z[0] = z[0] + x[i]
    z[1] = z[1] + y[i]
    z[2] = z[2] + pow(x[i], 2)
    z[3] = z[3] + x[i]*y[i]

print(z)

# Definir la matriz y el vector
A = np.array([[ni, z[0]], [z[0], z[2]]])
B = np.array([z[1], z[3]])

# Calcular la inversa de A
A_inv = np.linalg.inv(A)

# Calcular el vector solución X
g = np.dot(A_inv, B)

# Imprimir el vector solución
print("Solución:")
print(g[0] + g[1]*0.1)

# Creacion de la recta
y_recta = [g[0] + g[1]*x1 for x1 in x]

# Crear el gráfico
plt.scatter(x, y, color='red', label='un punto dato')  # Graficar los puntos
plt.plot(x, y_recta, color='blue', label='Recta')  # Graficar la recta

# Configurar el gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de puntos y una recta')
plt.legend()

# Mostrar el gráfico
plt.show()