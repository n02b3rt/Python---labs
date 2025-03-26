import numpy as np

unsorted_array = np.array([3, 1, 4, 1, 5, 9, 2, 6])
sorted_asc = np.sort(unsorted_array)
sorted_desc = np.sort(unsorted_array)[::-1]
sort_indices = np.argsort(unsorted_array)
min_index = np.argmin(unsorted_array)
max_index = np.argmax(unsorted_array)
indices_gt_3 = np.where(unsorted_array > 3)[0]

zero_array = np.array([1, 0, 2, 0, 3])
nonzero_indices = np.nonzero(zero_array)[0]

print("Posortowana rosnąco:", sorted_asc)
print("Posortowana malejąco:", sorted_desc)
print("Indeksy sortowania:", sort_indices)
print("Indeks najmniejszego elementu:", min_index)
print("Indeks największego elementu:", max_index)
print("Indeksy elementów > 3:", indices_gt_3)
print("Indeksy niezerowych elementów:", nonzero_indices)
