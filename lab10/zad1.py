import numpy as np
from scipy.integrate import quad

# 1: Zdefiniuj funkcję f(x) = x^2 * sin(2x).
def f(x):
    return x**2 * np.sin(2 * x)

# 2: Oblicz całkę oznaczoną tej funkcji w przedziale od 0 do 2$π$ za pomocą scipy.integrate.quad.
a = 0
b = 2 * np.pi

result, error = quad(f, a, b)

# 3: Wyświetl wynik i szacowany błąd obliczeń.
print(f"Całka oznaczona funkcji f(x) = x^2 * sin(2x) od {a} do {b} wynosi: {result:.4f}")
print(f"Szacowany błąd obliczeń: {error:.4e}")
