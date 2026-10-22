matrix1 = [
    [5, 0, 0, 9, 1, 3, 7, 2, 0],
    [3, 0, 0, 0, 8, 0, 5, 0, 9],
    [0, 9, 0, 2, 5, 0, 0, 8, 0],
    [6, 8, 0, 4, 7, 0, 2, 3, 0],
    [0, 0, 9, 5, 0, 0, 4, 6, 0],
    [7, 0, 4, 0, 0, 0, 0, 0, 5],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 8, 9, 1, 6, 0, 0],
    [8, 5, 0, 7, 2, 0, 0, 0, 3],
]

matrix2 = [
    [6, 9, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 9, 6, 0, 0, 0],
    [0, 8, 0, 7, 5, 3, 0, 9, 0],
    [0, 2, 0, 3, 7, 4, 5, 6, 1],
    [3, 6, 0, 0, 0, 5, 0, 2, 0],
    [0, 0, 0, 9, 6, 0, 3, 7, 8],
    [0, 0, 6, 0, 3, 1, 0, 8, 4],
    [0, 4, 5, 8, 0, 7, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 7],
]

def buscar_vacio(matrix): # Busca la primera casilla vacía y devuelve sus coordenadas.
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == 0:
				return (row,col)
	return None # No quedan casillas vacías.

def es_valido(matrix,row,col,num): # Comprueba si num puede colocarse en la casilla vacía (row, col).
    if num in matrix[row]: #revisamos la fila
        return False

    for i in range(len(matrix)): # revisamos la columna
        if matrix[i][col] == num:
            return False

    inicio_row = (row // 3) * 3 ## Calcula la esquina superior izquierda del bloque de 3 × 3.
    inicio_col = (col // 3) * 3 

    for i in range(inicio_row, inicio_row + 3): #hacemos el recorrido de la submatriz
        for j in range(inicio_col, inicio_col+3): #para buscar numeros
            if matrix[i][j] == num:
                return False

    return True


def solve(matrix): #recursiva

    vacio = buscar_vacio(matrix) #buscamos si aun hay espacios por rellenar

    if vacio is None: #si no hay espacios  regresamos
        return True

    row, col = vacio

    nums = [1,2,3,4,5,6,7,8,9] #posibles numeros

    for num in nums:#probamos todos los numeros
        if es_valido(matrix,row,col,num):
            matrix[row][col] = num #si es valido hacemos el cambio
            if solve(matrix): #recursivo, buscamos otro 0 y buscamos posibles soluciones ya con los cambios anteriores
                return True #regresamos true hasta que todo este correcto

            matrix[row][col] = 0 #si no hubo exito le ponemos 0 de nuevo e intentamos con otro numero

    return False #regresamos false para que se intente de nuevo con otro numero, la llamada anterior debe retroceder


resuelto = solve(matrix2)
print(resuelto)

for fila in matrix2:
    print(fila)



















