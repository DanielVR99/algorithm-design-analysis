# Función para multiplicar dos matrices cuadradas de 2x2
def multiplicar_matrices(A, B):
    # Se realiza el producto punto tradicional: filas de A por columnas de B
    resultado = [
        [
            # Fila 0 de A con columnas 0 y 1 de B
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1]
        ],
        [
            # Fila 1 de A con columnas 0 y 1 de B
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1]
        ]
    ]

    return resultado

# Función para calcular A^n usando la técnica Divide y Vencerás (Exponenciación Rápida) en O(log n)
def divide(A, n):
    # Caso base 1: Cualquier matriz elevada a la 0 es la matriz identidad (I)
    if n == 0:
        return [[1, 0], 
                [0, 1]]

    # Caso base 2: Cualquier matriz elevada a la 1 es la misma matriz
    if n == 1:
        return A

    # Paso Divide: Calcula recursivamente A^(n // 2) dividiendo el exponente a la mitad
    mitad = divide(A,n//2)

    # Paso Vence: Eleva al cuadrado la mitad obtenida -> (A^(n//2))^2 = A^(2 * (n//2))
    resultado = multiplicar_matrices(mitad,mitad)

    # Si n es impar, falta multiplicar por una matriz A adicional para completar la potencia: A^n = (A^(n//2))^2 * A
    if n%2 == 1:
        resultado = multiplicar_matrices(resultado,A)

    return resultado

# Función principal para obtener el n-ésimo número de Fibonacci mediante la matriz compañera
def fibonacci(n):
    # Matriz base de transformación lineal de Fibonacci:
    # [[0, 1], [1, 1]]^n genera [[F(n-1), F(n)], [F(n), F(n+1)]]
    A = [[0, 1], 
         [1, 1]]
    
    # Se calcula A^n en tiempo logarítmico O(log n)
    matriz_resultado = divide(A, n)
    
    # El valor de F(n) se encuentra en la posición [0][1] (o [1][0])
    return matriz_resultado[0][1]


# Pruebas de ejecución para verificar los primeros términos de la serie (F(0) hasta F(6))
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(2))  # 1
print(fibonacci(3))  # 2
print(fibonacci(4))  # 3
print(fibonacci(5))  # 5
print(fibonacci(6))  # 8
