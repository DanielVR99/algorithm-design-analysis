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

def divide(A, n):
    if n == 0:
        return [[1, 0], 
                [0, 1]]

    if n == 1:
        return A

    mitad = divide(A,n//2)

    resultado = multiplicar_matrices(mitad,mitad)

    if n%2 == 1:
        resultado = multiplicar_matrices(resultado,A)

    return resultado

def fibonacci(n):
    A = [[0, 1], 
         [1, 1]]
    matriz_resultado = divide(A, n)
    return matriz_resultado[0][1]


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))