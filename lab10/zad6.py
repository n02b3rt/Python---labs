import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Zadanie 6:
# - Z tego samego DataFrame wygeneruj macierz korelacji (`df.corr()`).
# - Narysuj mapę cieplną za pomocą `sns.heatmap`. Dodaj argument `annot=True`,
#   aby wyświetlić wartości korelacji na wykresie.

np.random.seed(42)

n = 150

cecha1 = np.random.normal(loc=50, scale=10, size=n)
cecha2 = np.random.normal(loc=30, scale=5, size=n)
cecha3 = np.random.normal(loc=100, scale=20, size=n)

kategorie = np.random.choice(['Grupa A', 'Grupa B', 'Grupa C'], size=n)

df = pd.DataFrame({
    'Cecha1': cecha1,
    'Cecha2': cecha2,
    'Cecha3': cecha3,
    'Kategoria': kategorie
})

print("Pierwsze 5 wierszy wygenerowanego DataFrame:")
print(df.head())

sns.pairplot(df, hue='Kategoria', diag_kind='kde', palette='Set2')
plt.suptitle("Pairplot z podziałem na Kategorię", y=1.02)
plt.show()

corr_matrix = df[['Cecha1', 'Cecha2', 'Cecha3']].corr()

print("\nMacierz korelacji:")
print(corr_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
plt.title("Mapa cieplna korelacji cech")
plt.show()
