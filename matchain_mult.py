def matChain_mult(dims):
    n = len(dims) - 1  # Number of matrices
    if n <= 1:
        return 0, None  # No or only one matrix, no multiplications needed

    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]


    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

def opt_parenthesization(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        opt_parenthesization(s, i, s[i][j])
        opt_parenthesization(s, s[i][j] + 1, j)
        print(")", end="")

if __name__ == "__main__":
    dimensions = [30, 35, 15, 5, 10, 20, 25]
    m_table, s_table = matChain_mult(dimensions)
    n_matrices = len(dimensions) - 1

    print("Minimum number of multiplications:", m_table[1][n_matrices])
    print("Optimal parenthesization:")
    opt_parenthesization(s_table, 1, n_matrices)
    print()