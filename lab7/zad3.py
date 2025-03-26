import numpy as np
arr = np.array([0, 10, 20, 30, 40, 50])

first_element = arr[0]
last_element = arr[-1]
second_to_fourth = arr[1:4]
every_second = arr[::2]

print("Pierwszy element:", first_element)
print("Ostatni element:", last_element)
print("Elementy od drugiego do czwartego:", second_to_fourth)
print("Co drugi element:", every_second)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

element = matrix[1, 2]
second_row = matrix[1]
third_column = matrix[:, 2]
top_left_2x2 = matrix[:2, :2]

print("\nElement z drugiego wiersza i trzeciej kolumny:", element)
print("Drugi wiersz:", second_row)
print("Trzecia kolumna:", third_column)
print("Podmacierz 2x2 z lewego górnego rogu:")
print(top_left_2x2)