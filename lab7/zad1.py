import numpy as np

array_10_to_20 = np.arange(10, 21)
print(array_10_to_20)

zeros = np.zeros((3, 3))
print(zeros)

ones = np.ones((2, 5), dtype=int)
print(ones)

even_numbers = np.arange(0, 31, 2)
print(even_numbers)

np.random.seed(123)

random_matrix = np.random.randint(-10, 11, size=(4, 4))
print(random_matrix)
