def product(M, N):
    R = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            R[i][j] = M[i][0] * N[0][j] + M[i][1] * N[1][j]
    return R

def subtract(M, N):
    R = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            R[i][j] = M[i][j] - N[i][j]
    return R

def multiply(k, M):
    R = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            R[i][j] = k * M[i][j]
    return R

def compute_AB(n):
    A = [[1, 3], [2, -1]]
    B = [[2, 1], [1, 4]]

    An = [[1, 0], [0, 1]]
    Bn = [[0, 0], [0, 0]]

    for i in range(n):
        next_An = subtract(product(An, A), multiply(7, product(Bn, B)))
        next_Bn = subtract(product(Bn, A), product(An, B))

        An = next_An
        Bn = next_Bn

    return An, Bn

def print_matrix(M):
    for row in M:
        print(f"{row[0]} {row[1]}")

def main():
    print("=================== PROBLEM 2 BẮT ĐẦU ===================")
    
    A = [[1, 3], [2, -1]]
    B = [[2, 1], [1, 4]]
    
    print("--- Câu 2.1: Nhân ma trận A và B ---")
    print("A * B =")
    print_matrix(product(A, B))
    
    print("\n--- Câu 2.2: Tính An và Bn ---")
    
    A1, B1 = compute_AB(1)
    print("Test case n=1:")
    print("A1 =")
    print_matrix(A1)
    print('')
    print("B1 =")
    print_matrix(B1)
    print('')
    print("-------------------------------------------------")
    
    # Test case n = 2
    A2, B2 = compute_AB(2)
    print("Test case n=2:")
    print("A2 =")
    print_matrix(A2)
    print('')
    print("B2 =")
    print_matrix(B2)
    print('')
    print("-------------------------------------------------")
    
    # Test case n = 3
    A3, B3 = compute_AB(3)
    print("Test case n=3:")
    print("A3 =")
    print_matrix(A3)
    print('')
    print("B3 =")
    print_matrix(B3)
    print('')

if __name__ == "__main__":
    main()