def gauss_elimination(A, B):
    n = len(B)

    for i in range(n):
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] = A[j][k] - ratio * A[i][k]
            B[j] = B[j] - ratio * B[i]


    X = [0] * n
    X[n-1] = B[n-1] / A[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i][j] * X[j]
        X[i] = (B[i] - sum_ax) / A[i][i]

    return X



A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]

B = [8, -11, -3]

solution = gauss_elimination(A, B)
print("Solution:", solution)