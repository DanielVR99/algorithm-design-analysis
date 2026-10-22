valores = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
pesos = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
capacidad = 140

import numpy as np

dp = np.zeros((len(valores) + 1, capacidad + 1), dtype=int) # creamos una matriz para guardar nuestros resultados con puros 0s

for i in range(1,len(pesos)+1): 
	for c in range(1,capacidad+1): #ciclos para recorrer la matriz revisando cada objeto y la capacidad de la mochila
		if pesos[i-1] > c: # Si el peso es mayor a nuestra capacidad actual
			dp[i][c] = dp[i - 1][c] # dejamos el valor anterior
		else: # si el peso cabe en la mochila
			dp[i][c] = max(dp[i - 1][c],dp[i - 1][c - pesos[i - 1]] + valores[i-1])	# comparamos al valor de la row anterior con el valor que tenemos 
																					# si sumamos el valor del objeto actual + que teniamos guardado en la 
																					# tabla que sería el valor maximo acumulado


print("Valor óptimo:", dp[len(valores)][capacidad])

i = len(valores)
c = capacidad
seleccion = []

while i > 0: # para revisar que objetos se seleccionaron
	# recorremos cada objeto de la matriz
	if dp[i][c] != dp[i-1][c]:  # Si el valor del objeto anterior es diferente al que estamos actualmente
		seleccion.append(i)		# Significa que ese objeto fue seleccionado
		c -= pesos[i - 1]		# Nos movemos en la capacidad para buscar el siguiente objeto

	i -= 1 # Buscamos el siguiente objeto

print("Objetos seleccionados:", seleccion)