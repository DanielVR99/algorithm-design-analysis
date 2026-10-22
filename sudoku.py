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

def buscar_vacio(matrix):
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == 0:
				return (row,col)

	return None

def es_valido(matrix,row,col,num):
    if num in matrix[row]:
        return False

    for i in range(len(matrix)):
        if matrix[i][col] == num:
            return False

    inicio_row = (row // 3) * 3
    inicio_col = (col // 3) * 3

    for i in range(inicio_row, inicio_row + 3):
        for j in range(inicio_col, inicio_col+3):
            if matrix[i][j] == num:
                return False

    return True


def solve(matrix):

    vacio = buscar_vacio(matrix)

    if vacio is None:
        return True

    row, col = vacio

    nums = [1,2,3,4,5,6,7,8,9]

    for num in nums:
        if es_valido(matrix,row,col,num):
            matrix[row][col] = num
            if solve(matrix):
                return True

            matrix[row][col] = 0

    return False


resuelto = solve(matrix1)
print(resuelto)

for fila in matrix1:
    print(fila)



















