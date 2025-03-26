import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([9, 10])

# 1. Połącz A i B pionowo.
vertical_AB = np.vstack((A, B))

# 2. Połącz A i B poziomo.
horizontal_AB = np.hstack((A, B))

# 3. Połącz A i B, a następnie dodaj C jako nowy wiersz.
combined_AB = np.vstack((A, B))
combined_with_C = np.vstack((combined_AB, C))

# 4. Podziel D na dwie części pionowo.
D = np.arange(16).reshape((4,4))
vertical_split = np.vsplit(D, 2)

# 5. Podziel D na cztery równe części poziomo.
horizontal_split = np.hsplit(D, 4)

print("1. Połącz A i B pionowo:")
print(vertical_AB)

print("\n2. Połącz A i B poziomo:")
print(horizontal_AB)

print("\n3. Połącz A i B, a następnie dodaj C jako nowy wiersz:")
print(combined_with_C)

print("\n4. Podziel D na dwie części pionowo:")
print("Część 1:")
print(vertical_split[0])
print("Część 2:")
print(vertical_split[1])

print("\n5. Podziel D na cztery równe części poziomo:")
for i, part in enumerate(horizontal_split, 1):
    print(f"Część {i}:")
    print(part)
