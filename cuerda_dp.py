precios = [1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51] 
longitud = 11 

dp = [0] * (longitud + 1) # Almacena la ganancia max
primera_pieza = [0] * (longitud + 1) # Registro del primer corte se inicia en 0s

for lon in range(1, longitud + 1): # ver todas las ganancias óptimas para cada longitud de cuerda
	for i in range(1,lon + 1): # Ver todos los primeros cortes posibles de tamaño i para la longitud actual
		ingreso = precios[i - 1] + dp[lon - i] # Suma el precio del corte actual más la mejor solucion ya calculada


		if ingreso > dp[lon]: # Es es mejor:
			dp[lon] = ingreso # Actualiza el valor maximo
			primera_pieza[lon] = i # Guarda el tamaño de corte de este valor máximo

restante = longitud # Inicializa la reconstrucción
piezas = [] # combinación exacta de cortes

while restante > 0: 
	size = primera_pieza[restante] # Recupera el tamaño del corte 
	piezas.append(size) 
	restante -= size 

print("Ingreso máximo:", dp[longitud]) 
print("Piezas:", piezas)