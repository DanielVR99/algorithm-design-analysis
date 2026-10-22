valores = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
pesos = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
capacidad = 140

import numpy as np

dp = np.zeros((len(valores) + 1, capacidad + 1), dtype=int)

for i in range(1,len(pesos)+1):
	for c in range(1,capacidad+1):
		if pesos[i-1] > c:
			dp[i][c] = dp[i - 1][c]
		else:
			dp[i][c] = max(dp[i - 1][c],dp[i - 1][c - pesos[i - 1]] + valores[i-1])


print("Valor óptimo:", dp[len(valores)][capacidad])

i = len(valores)
c = capacidad
seleccion = []

while i > 0:
	if dp[i][c] != dp[i-1][c]:
		seleccion.append(i)
		c -= pesos[i - 1]

	i -= 1

print("Objetos seleccionados:", seleccion)