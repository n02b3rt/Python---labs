"""
## Zadanie 6 - Dekoratory

Napisz dekorator `loguj_wywolanie`, który będzie wypisywał na konsolę informację o wywołaniu udekorowanej metody (nazwę metody i argumenty).

### Do zrobienia

1. Stwórz klasę `Kalkulator` z metodami (`dodaj`, `odejmij`, `pomnoz`).
2. Udekoruj metody dekoratorem `loguj_wywolanie`.
3. Dodaj poziomy logowania („DEBUG”, „INFO”, „WARNING”).
"""

import functools

def loguj_wywolanie(poziom="INFO"):
    def dekorator(funkcja):
        @functools.wraps(funkcja) # bez tej metody funkcja.__name__ zwróciło by "wapper"
        def wrapper(*args, **kwargs):
            nazwa_metody = funkcja.__name__
            print(f"[{poziom}] Wywołano: {nazwa_metody}({args[1:]}, {kwargs})")
            wynik = funkcja(*args, **kwargs)
            print(f"[{poziom}] Wynik: {wynik}")
            return wynik
        return wrapper
    return dekorator

class Kalkulator:
    @loguj_wywolanie("DEBUG")
    def dodaj(self,a,b):
        return a+b

    @loguj_wywolanie("INFO")
    def odejmij(self,a,b):
        return a-b

    @loguj_wywolanie("WARNING")
    def pomnoz(self,a,b):
        return a*b

kalkulator = Kalkulator()

print(kalkulator.dodaj(a=5,b=2))
print(kalkulator.odejmij(a=5,b=2))
print(kalkulator.pomnoz(a=5,b=2))