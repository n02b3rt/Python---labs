import pandas as pd

# Zadanie 1.1
data = [5, 10, 15, 20, 25]
series_default = pd.Series(data)
print("Series z domyślnym indeksem:")
print(series_default)

custom_index = ['a', 'b', 'c', 'd', 'e']
series_custom = pd.Series(data, index=custom_index)
print("\nSeries z własnym indeksem:")
print(series_custom)

# Zadanie 1.2
value_c = series_custom['c']
print("\nWartość spod indeksu 'c':", value_c)

value_second = series_custom.iloc[1]
print("Wartość na drugiej pozycji (iloc[1]):", value_second)

first_three = series_custom.iloc[0:3]
print("Pierwsze trzy wartości:")
print(first_three)
