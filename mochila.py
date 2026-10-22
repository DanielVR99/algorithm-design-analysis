valores = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
pesos = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
capacidad = 101

objetos = []

# Empaquetamos cada objeto con su id original y calculamos su densidad (valor/peso)
for i in range(len(valores)):
	relacion = valores[i]/pesos[i]
	objetos.append((i+1, valores[i], pesos[i], relacion))

# Ordenamos por densidad descendente: clave para maximizar la cota y podar rápido
objetos.sort(key=lambda objeto: objeto[3], reverse=True)

# Calcula la cota superior relajando el problema a mochila fraccionaria (óptimo teórico)
def calcular_cota(i, peso, valor):
	cota = valor
	capacidad_restante = capacidad-peso

	for j in range(i, len(objetos)):
		numero, valor_objeto, peso_objeto, relacion = objetos[j]

		# Si el objeto no cabe entero, toma la fracción proporcional y cierra la cota
		if peso_objeto > capacidad_restante:
			cota += capacidad_restante * relacion
			break	
		else:
			cota += valor_objeto
			capacidad_restante -= peso_objeto

	return cota

mejor_valor = 0
mejor_seleccion = []

def ramificar(i, peso, valor, seleccion):
    global mejor_valor, mejor_seleccion

    # Poda por no factibilidad: se excede la capacidad límite
    if peso > capacidad:
    	return

    # Actualiza el mejor óptimo global encontrado hasta el momento
    if valor > mejor_valor:
        mejor_valor = valor
        mejor_seleccion = seleccion.copy()

    # Condición de paro: se evaluaron todos los objetos disponibles
    if i == len(objetos):
    	return

    # Poda por cota: si el potencial máximo no supera al mejor valor actual, descarta la rama
    if calcular_cota(i, peso, valor) <= mejor_valor:
        return

    numero, valor_objeto, peso_objeto, relacion = objetos[i]

    # Rama izquierda: decisión de incluir el objeto actual
    ramificar(
        i + 1,
        peso + peso_objeto,
        valor + valor_objeto,
        seleccion + [numero]
    )

    # Rama derecha: decisión de excluir el objeto actual
    ramificar(i + 1, peso, valor, seleccion)

# Inicia la exploración desde la raíz del árbol de decisiones
ramificar(0, 0, 0, [])

print("Mejor valor:", mejor_valor)
print("Objetos seleccionados:", mejor_seleccion)