from linear_algebra import *

# Some samples

A = [[1, 4], [-2, 3]]
B = [[-2, 5], [6, 7]]

print('Matrix A:')
print_matrix(A)

print('Matrix B:')
print_matrix(B)

print('Addition of matrices A and B:')

# Addition
print_matrix(add_matrix(A, B))

print('Subtraction of matrices A and B:')

# Subtraction
print_matrix(subtract_matrix(A, B))

print('Multiplication of matrices A and B:')

# Multiplication
print_matrix(multiply_matrix(A, B))

print('Division of matrices A and B (A * B ^ (-1)):')

# Division
print_matrix(divide_matrix(A, B))

print('Transpose of matrix A:')

# Transpose
print_matrix(transpose_matrix(A))

# Determinant
print(f'Determinant of matrix A: {determinant_matrix(A)}')
print(f'Determinant of matrix A: {determinant_matrix(B)}')
