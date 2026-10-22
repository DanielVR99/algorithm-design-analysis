import numpy as np

p = [5, 10, 3, 12, 5, 50, 6] # dimensiones de las matrices: A1 es 5x10, A2 es 10x3, etc.
n = len(p) - 1  # 6 matrices

dp = np.zeros((n, n), dtype=int) # tabla para guardar el costo mínimo de multiplicar de la matriz i a la j
division = np.zeros((n, n), dtype=int) # guarda en qué punto k conviene partir para reconstruir los paréntesis

for lon in range(2,n + 1): # tamaño de la cadena de matrices que vamos evaluando
    for i in range(n - lon + 1):
        j = i + lon - 1
        for k in range(i, j): # probamos partir entre la matriz k y k+1
            costo = (dp[i][k]
                     + dp[k + 1][j]
                     + p[i] * p[k + 1] * p[j + 1] # costo de multiplicar los dos bloques resultantes
                    )

            if k == i or costo < dp[i][j]: # si es la primera opción o encontramos un costo más bajo, actualizamos
                dp[i][j] = costo
                division[i][j] = k

print("Costo mínimo:", dp[0][n - 1])
print(division)

def parentizar(i, j): # reconstruye recursivamente los paréntesis usando la matriz division
    if i == j:
        return f"A{i + 1}"
    else:
        k = division[i][j]
        return f"({parentizar(i, k)} x {parentizar(k + 1, j)})"

print("Parentización óptima:", parentizar(0, n - 1))