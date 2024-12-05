def matrix_sum(matrix):
    total_sum = 0
    for row in  matrix:
        total_sum += sum(row)
    return total_sum

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_sum(matrix))  # Output: 45