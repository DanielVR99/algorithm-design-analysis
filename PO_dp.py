import numpy as np

p = [5, 10, 3, 12, 5, 50, 6]
n = len(p) - 1  # 6 matrices

dp = np.zeros((n, n), dtype=int)
division = np.zeros((n, n), dtype=int)

for lon in range(2,n + 1):
	for i in range(n - lon + 1):
		j = i + lon - 1
		for k in range(i, j):
			costo = (dp[i][k]
					 + dp[k + 1][j]
    				 + p[i] * p[k + 1] * p[j + 1]
					)

			if k == i or costo < dp[i][j]:
				dp[i][j] = costo
				division[i][j] = k

print("Costo mínimo:", dp[0][n - 1])
print(division)

def parentizar(i, j):
	if i == j:
		return f"A{i + 1}"
	else:
		k = division[i][j]
		return f"({parentizar(i, k)} x {parentizar(k + 1, j)})"

print("Parentización óptima:", parentizar(0, n - 1))