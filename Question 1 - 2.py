#2 Using NumPy
import numpy as np
# Define matrices
A = np.array([[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087]])
B = np.array([[3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234]])
C = np.array([[3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]])

# Matrix addition
add_AB = A + B
add_BC = B + C

# Matrix subtraction
subtract_AB = A - B
subtract_BC = B - C

# Matrix multiplication (element-wise)
multiply_AB = A * B
multiply_BC = B * C

# Sum of each matrix
sum_A = np.sum(A)
sum_B = np.sum(B)
sum_C = np.sum(C)

# Print results
print("Addition of A and B:\n", add_AB)
print("Subtraction of A and B:\n", subtract_AB)
print("Element-wise multiplication of A and B:\n", multiply_AB)
print("Addition of B and C:\n", add_BC)
print("Subtraction of B and C:\n", subtract_BC)
print("Element-wise multiplication of B and C:\n", multiply_BC)
print("Sum of Matrix A:", sum_A)
print("Sum of Matrix B:", sum_B)
print("Sum of Matrix C:", sum_C) 

