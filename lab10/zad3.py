import numpy as np
from scipy import stats

# 1:
# Wygeneruj dwie grupy danych (np. wielkość spadku wagi przy różnych dietach) za pomocą `np.random.normal`:
# - Grupa A (średnia = 5 kg, odchylenie standardowe = 1 kg).
# - Grupa B (średnia = 4 kg, odchylenie standardowe = 1.5 kg).

np.random.seed(42)

grupa_A = np.random.normal(loc=5, scale=1, size=30)
grupa_B = np.random.normal(loc=4, scale=1.5, size=30)

print("Grupa A - Średnia:", np.mean(grupa_A), "Odchylenie standardowe:", np.std(grupa_A, ddof=1))
print("Grupa B - Średnia:", np.mean(grupa_B), "Odchylenie standardowe:", np.std(grupa_B, ddof=1))

# 2:
# Załóż, że to wyniki z 30-osobowych grup. Sprawdź testem t-Studenta (funkcja scipy.stats.ttest_ind),
# czy różnica średnich jest istotna statystycznie na poziomie $α=0.05$.

t_stat, p_value = stats.ttest_ind(grupa_A, grupa_B, equal_var=False)  # Test z założeniem nierówności wariancji

print("\nTest t-Studenta:")
print(f"Statystyka t = {t_stat:.4f}")
print(f"P-wartość = {p_value:.4f}")

# 3:
# Zinterpretuj wynik (czy można stwierdzić istotną różnicę między grupami?):
# Jeśli p-wartość < 0.05, możemy stwierdzić, że różnica średnich jest istotna statystycznie.
# Jeśli p-wartość >= 0.05, brak podstaw do stwierdzenia istotnej różnicy.

alpha = 0.05
if p_value < alpha:
    print("\nWynik testu: Istotna statystycznie różnica między grupami (odrzucamy H0).")
else:
    print("\nWynik testu: Brak istotnej statystycznie różnicy między grupami (nie odrzucamy H0).")
