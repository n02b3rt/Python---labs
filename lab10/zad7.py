import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Zadanie 7:
# - Utwórz wykres pudełkowy (boxplot) pokazujący rozkład jednej
#   z kolumn liczbowych względem kategorii (np. rozkład wyniku testu w zależności od płci).
# - Nadaj tytuł i etykiety osi.

np.random.seed(42)

n = 100
df = pd.DataFrame({
    'Wynik': np.random.normal(loc=75, scale=10, size=n),
    'Płeć': np.random.choice(['K', 'M'], size=n)
})

plt.figure(figsize=(8, 6))
sns.boxplot(x='Płeć', y='Wynik', data=df, palette='Set3')

plt.title("Rozkład wyniku testu w zależności od płci")
plt.xlabel("Płeć")
plt.ylabel("Wynik testu")

plt.show()
