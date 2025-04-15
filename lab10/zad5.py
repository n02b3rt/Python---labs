import numpy as np
import matplotlib.pyplot as plt

# Zadanie 5:
# - Z danych wygenerowanych w ćwiczeniu statystycznym (np. Grupa A z dietą)
#   stwórz histogram przedstawiający rozkład wag po diecie.
#   Wybierz np. 10 przedziałów klasowych (`bins=10`).
# - Dodaj etykiety i opcjonalnie siatkę (`grid(axis='y')`).

np.random.seed(42)

grupa_A = np.random.normal(loc=5, scale=1, size=30)

plt.figure(figsize=(8, 6))
plt.hist(grupa_A, bins=10, color='skyblue', edgecolor='black')

plt.xlabel("Spadek wagi (kg)")
plt.ylabel("Liczba osób")
plt.title("Rozkład spadku wagi po diecie (Grupa A)")

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
