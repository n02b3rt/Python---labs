import numpy as np

X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

matrix_mult = X.dot(Y)
element_mult = X * Y
X_transpose = X.T
X_inverse = np.linalg.inv(X)
X_det = np.linalg.det(X)

print("Mnożenie macierzowe X * Y:")
print(matrix_mult)
print("\nMnożenie element po elemencie:")
print(element_mult)
print("\nTranspozycja X:")
print(X_transpose)
print("\nMacierz odwrotna X:")
print(X_inverse)
print("\nWyznacznik X:")
print(X_det)
