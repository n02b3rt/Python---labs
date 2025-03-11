"""
Zadanie 3 - Metody Specjalne

Stwórz klasę `Ulamek` reprezentującą ułamek (licznik/mianownik) i zaimplementuj metody specjalne:

- `__init__()` – konstruktor z walidacją (mianownik ≠ 0).
- `__str__()` – zwraca ułamek w formacie "3/4".
- `__repr__()` – do debugowania ("Ulamek(3, 4)").
- `__add__()` – dodawanie ułamków.
- `__eq__()` – porównywanie ułamków.
- `__mul__()` – mnożenie ułamków.
"""

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

class Ulamek:
    def __init__(self, licznik, mianownik):
        if mianownik == 0:
            raise ValueError("Mianownik nie może być zerem")

        nwd_wartosc = nwd(licznik, mianownik)
        self.licznik = licznik // nwd_wartosc
        self.mianownik = mianownik // nwd_wartosc

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    def __repr__(self):
        return f"Ulamek({self.licznik}, {self.mianownik})"

    def __add__(self, other):
        nowy_licznik = self.licznik * other.mianownik + other.licznik * self.mianownik
        nowy_mianownik = self.mianownik * other.mianownik
        return Ulamek(nowy_licznik, nowy_mianownik)

    def __eq__(self, other):
        return self.licznik == other.licznik and self.mianownik == other.mianownik

    def __mul__(self, other):
        return Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

# Testowanie
u1 = Ulamek(3, 4)
u2 = Ulamek(1, 2)

print(u1)
print(repr(u1))

print(u1 + u2)

print(u1 * u2)

print(u1 == Ulamek(6, 8))
print(u1 == u2)