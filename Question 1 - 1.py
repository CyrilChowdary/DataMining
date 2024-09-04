
#1. Using Python Lists
# Define matrices
A = [[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087]]
B = [[3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234]]
C = [[3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]]

# Matrix addition
def add_matrices(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# Matrix subtraction
def subtract_matrices(mat1, mat2):
    return [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# Matrix multiplication (element-wise)
def multiply_matrices(mat1, mat2):
    return [[mat1[i][j] * mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# Sum of each matrix
def sum_matrix(mat):
    return sum(sum(row) for row in mat)

# Perform operations
add_AB = add_matrices(A, B)
subtract_AB = subtract_matrices(A, B)
multiply_AB = multiply_matrices(A, B)

add_BC = add_matrices(B, C)
subtract_BC = subtract_matrices(B, C)
multiply_BC = multiply_matrices(B, C)

# Print results
print("Addition of A and B:", add_AB)
print("\nSubtraction of A and B:", subtract_AB)
print("\nElement-wise multiplication of A and B:", multiply_AB)
print("\nSum of Matrix A:", sum_matrix(A))
print("\nSum of Matrix B:", sum_matrix(B))
print("\nSum of Matrix C:", sum_matrix(C))