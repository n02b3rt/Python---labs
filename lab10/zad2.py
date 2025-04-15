import numpy as np
from scipy.optimize import fsolve

# 1. Zdefiniuj funkcję g(x) = e^x - 2*x.
def g(x):
    return np.exp(x) - 2 * x

# Lista punktów startowych do sprawdzenia
punkty_startowe = [0, -1, 1, 5]

# 2. Użyj fsolve, by znaleźć wartość x, dla której g(x) = 0.
# 3. Sprawdź, jak zmienia się rozwiązanie (lub brak rozwiązania) przy różnych punktach startowych x0.
print("Rozwiązywanie równania g(x) = exp(x) - 2*x = 0 przy różnych punktach startowych:")
for x0 in punkty_startowe:
    rozwiazanie = fsolve(g, x0)
    wartosc_funkcji = g(rozwiazanie[0])
    print(f"Punkt startowy x0 = {x0:.1f} --> x = {rozwiazanie[0]:.4f}, g(x) = {wartosc_funkcji}")

# Funkcja g(x) = exp(x) - 2*x nie ma rzeczywistego miejsca zerowego.
# fsolve "znajduje" punkt, w którym funkcja osiąga minimum (w okolicach x ~ ln(2) ≈ 0.6931),
# ale g(0.6931) ≈ 0.6138, czyli nie równa się 0.
