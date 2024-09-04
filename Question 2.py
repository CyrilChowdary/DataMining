# I. Create a List
numbers = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]

# II. Iterate using a for loop
print("Iterating using a for loop:")
for num in numbers:
    print(num, end=' ')
print("\n")

# III. Iterate using a for loop and range
print("Iterating using a for loop and range:")
for i in range(len(numbers)):
    print(numbers[i], end=' ')
print("\n")

# IV. List Comprehension
squared_numbers = [num ** 2 for num in numbers]
print("Squared numbers using list comprehension:")
print(squared_numbers)
print("\n")

# V. Enumerate
print("Iterating using enumerate:")
for index, num in enumerate(numbers):
    print(f"Index {index}: {num}")
print("\n")

# VI. Iter function and next function
print("Using iter and next functions:")
numbers_iter = iter(numbers)
print(next(numbers_iter))  # prints the first element
print(next(numbers_iter))  # prints the second element
print("\n")

# VII. Map function
print("Using map function to double the numbers:")
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)
print("\n")

# VIII. Using zip
print("Using zip function to pair elements with their index:")
indexed_numbers = list(zip(range(len(numbers)), numbers))
print(indexed_numbers)
print("\n")

# IX. Using NumPy Module
import numpy as np

print("Using NumPy module to perform operations on the list:")
np_numbers = np.array(numbers)

# Adding 10 to each element
np_addition = np_numbers + 10
print("Adding 10 to each element:")
print(np_addition)

# Multiplying each element by 2
np_multiplication = np_numbers * 2
print("\nMultiplying each element by 2:")
print(np_multiplication)

# Calculating the mean of the list
np_mean = np.mean(np_numbers)
print("\nMean of the list:")
print(np_mean)

