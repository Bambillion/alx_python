def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    squared_matrix = [[0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
    # Compute the square value of each element in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squared_matrix[i][j] = matrix[i][j] ** 2
    return squared_matrix