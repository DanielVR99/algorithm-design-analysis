precios = [1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51]
longitud = 11

dp = [0] * (longitud + 1)
primera_pieza = [0] * (longitud + 1)

for lon in range(1, longitud + 1):
	for i in range(1,lon + 1):
		ingreso = precios[i - 1] + dp[lon - i]


		if ingreso > dp[lon]:
			dp[lon] = ingreso
			primera_pieza[lon] = i

restante = longitud
piezas = []

while restante > 0:
	size = primera_pieza[restante]
	piezas.append(size)
	restante -= size

print("Ingreso máximo:", dp[longitud])
print("Piezas:", piezas)