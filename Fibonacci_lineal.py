# Función para multiplicar dos matrices cuadradas de tamaño 2x2
def multiplicar_matrices(A, B):
    # Se calcula manualmente el producto fila por columna para cada posición:
    resultado = [
        [
            # Posición [0][0]: fila 0 de A * columna 0 de B
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            # Posición [0][1]: fila 0 de A * columna 1 de B
            A[0][0] * B[0][1] + A[0][1] * B[1][1]
        ],
        [
            # Posición [1][0]: fila 1 de A * columna 0 de B
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            # Posición [1][1]: fila 1 de A * columna 1 de B
            A[1][0] * B[0][1] + A[1][1] * B[1][1]
        ]
    ]

    return resultado

# Función para elevar una matriz A a la potencia n de forma iterativa
def potencia_matriz(A, n):
    # Se inicializa el resultado con la matriz base (equivale a potencia 1)
    resultado = A

    # Se multiplica la matriz por sí misma n - 1 veces para alcanzar A^n
    for i in range(n - 1):
        resultado = multiplicar_matrices(resultado, A)

    return resultado

# Función para calcular el n-ésimo número de Fibonacci usando potenciación de matrices
def fibonacci(n):
    # Casos base de la sucesión de Fibonacci
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        # Matriz de transformación estándar para Fibonacci:
        # [[0, 1], [1, 1]]^n produce [[F(n-1), F(n)], [F(n), F(n+1)]]
        A = [[0, 1], 
             [1, 1]]
        
        # Se calcula A elevado a la potencia n
        matriz_resultado = potencia_matriz(A, n)
        
        # El término F(n) queda ubicado en la posición [0][1] (o en [1][0])
        return matriz_resultado[0][1]

# Llamada de prueba para obtener el 7-ésimo término de Fibonacci (resultado esperado: 13)
print(fibonacci(7))