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

# Función para elevar una matriz A a la potencia n de forma iterativa
def potencia_matriz(A, n):
    # Se inicializa el resultado con la matriz base (equivale a potencia 1)
    resultado = A

    # Se multiplica la matriz por sí misma n - 1 veces para alcanzar A^n
    for i in range(n - 1):
        resultado = multiplicar_matrices(resultado, A)

    return resultado


def fibonacci_lineal(n):
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

def fibonacci_log(n):
    # Matriz base de transformación lineal de Fibonacci:
    # [[0, 1], [1, 1]]^n genera [[F(n-1), F(n)], [F(n), F(n+1)]]
    A = [[0, 1], 
         [1, 1]]
    
    # Se calcula A^n en tiempo logarítmico O(log n)
    matriz_resultado = divide(A, n)
    
    # El valor de F(n) se encuentra en la posición [0][1] (o [1][0])
    return matriz_resultado[0][1]

import timeit

n = 10000
repeticiones = 1000

tiempo_lineal = timeit.timeit(
    lambda: fibonacci_lineal(n),
    number=repeticiones
) / repeticiones

tiempo_rapido = timeit.timeit(
    lambda: fibonacci_log(n),
    number=repeticiones
) / repeticiones

print("Lineal:", tiempo_lineal, "segundos")
print("Divide y vencerás:", tiempo_rapido, "segundos")