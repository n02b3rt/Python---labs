import numpy as np

linear_array = np.arange(20)
matrix_4_5 = linear_array.reshape(4, 5)
matrix_with_5_columns = linear_array.reshape(-1, 5)
flattened = matrix_4_5.flatten()
transposed = matrix_4_5.T
expanded_dim = linear_array.reshape(20, 1)

print("Macierz o wymiarach (4,5):")
print(matrix_4_5)
print("\nMacierz z 5 kolumnami (NumPy dobierze liczbę wierszy):")
print(matrix_with_5_columns)
print("\nSpłaszczona macierz:")
print(flattened)
print("\nTransponowana macierz:")
print(transposed)
print("\nLinear_array z dodanym wymiarem (20,1):")
print(expanded_dim)
