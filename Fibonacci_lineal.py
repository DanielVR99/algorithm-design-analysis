def multiplicar_matrices(A, B):
    resultado = [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1]
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1]
        ]
    ]

    return resultado

def potencia_matriz(A, n):
    resultado = A

    for i in range(n - 1):
        resultado = multiplicar_matrices(resultado, A)

    return resultado

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        A = [[0, 1], 
             [1, 1]]
        matriz_resultado = potencia_matriz(A, n)
        return matriz_resultado[0][1]

print(fibonacci(7))