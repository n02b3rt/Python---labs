import numpy as np

data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
selected_indices = data[[1, 3, 5]]
data[[0, 2, 4]] = 99
selected_greater_than_20 = data[data > 20]
data[data < 15] = 1

print("Elementy o indeksach [1, 3, 5]:", selected_indices)
print("Tablica po zmianie elementów o indeksach [0, 2, 4] na 99:", data)
print("Elementy większe niż 20:", selected_greater_than_20)
print("Tablica po ustawieniu elementów mniejszych niż 15 na 1:", data)
