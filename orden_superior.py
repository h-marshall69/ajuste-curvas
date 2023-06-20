import math
import numpy as np
import matplotlib.pyplot as plt

x = [0.1 ,0.4, 0.5, 0.7, 0.7, 0.9]
y = [0.61, 0.92, 0.99, 1.52, 1.47, 2.03]

m = 2 
ni= 6

z1 = [[0.0 for n in range(m + 1)] for n in range(m + 1)]
z2 = [0.0 for n in range(m + 1)]

def fun(xi, k):
    f = 0.0
    for x_i in xi:
        f += pow(x_i, k)
    return f

def mul(xi, yi, k):
    f = 0.0


    for x_i, y_i in zip(x, y):
        f += pow(x_i, k) * y_i
    return f

for i in range(m + 1):
    for j in range(m + 1):
        z1[i][j] = fun(x, i + j)
        z1[j][i] = fun(x, i + j)
    z2[i] = mul(x, y, i)

A = np.array(z1)
B = np.array(z2)

A_inv = np.linalg.inv(A)

g = np.dot(A_inv, B)

def pol(xi):
    f = 0.0
    for i in range(len(g)):
        f += g[i] * pow(xi, i)

    return f

polinomio = [pol(xi) for xi in x]

print(g)

coeficiente = g[::-1]
print(coeficiente)
x_rango = np.linspace(min(x), max(x), 100)

yy = np.polyval(coeficiente, x_rango)

plt.plot(x_rango, yy, label='Polinomio')
plt.scatter(x, np.polyval(coeficiente, x), color='red')

plt.show()
