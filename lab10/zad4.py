import matplotlib.pyplot as plt
import numpy as np

# Zadanie 4:
# - Wygeneruj 50 losowych punktów (x, y) podobnie jak w przykładzie (np. z rozkładu normalnego).
# - Narysuj wykres punktowy w stylu OO (Object-Oriented) – czyli stwórz `fig, ax = plt.subplots()`, a następnie `ax.scatter(...)`.
# - Dodaj etykiety osi i tytuł..

np.random.seed(42)

x = np.random.normal(loc=0, scale=1, size=50)
y = np.random.normal(loc=0, scale=1, size=50)

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(x, y, color='blue', marker='o')

ax.set_xlabel("Oś X")
ax.set_ylabel("Oś Y")
ax.set_title("Wykres punktowy losowych danych")

plt.show()
