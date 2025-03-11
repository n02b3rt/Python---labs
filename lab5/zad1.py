"""
## Zadanie 1 - Dziedziczenie Wielokrotne i MRO

Rozbuduj przykład z amfibią. Stwórz następujące klasy:

- **`PojazdSzybkobiezny`** – dodaje metodę `maksymalna_predkosc()`.
- **`PojazdPlywajacyPoGlebokiejWodzie`** – dodaje metodę `zanurzenie()`.
- **`SuperAmfibia`** – dziedziczy po `PojazdLadowy`, `PojazdWodny`, `PojazdSzybkobiezny` i `PojazdPlywajacyPoGlebokiejWodzie`.

### Do zrobienia

1. Zaimplementuj metody `maksymalna_predkosc()` i `zanurzenie()` (niech zwracają odpowiednie opisy).
2. Sprawdź, jak dziedziczenie wielokrotne wpływa na działanie metod.
3. Dodaj metodę `opis()` do `PojazdSzybkobiezny` i `PojazdWodny`.
Sprawdź, która metoda zostanie wywołana dla `SuperAmfibia`. Przeanalizuj `SuperAmfibia.__mro__`.
"""

class PojazdLadowy():
    def jedz(self):
        return "Jadę po lądzie"

class PojazdWodny():
    def plyn(self):
        return "Płyne po wodzie"

    def opis(self):
        return "Jestem pojazdem wodnym"

class PojazdSzybkobiezy():
    def maksymalna_predkosc(self):
        return "Moja maksymalna predkosc to 250 km/h"

    def opis(self):
        return "Jestem pojazdem szybkim"

class PojazdPlywajacyPoGlebokiejWodzie():
    def zanurzenie(self):
        return "Moge zanurzyc sie!"

class SuperAmfibia(PojazdLadowy, PojazdWodny, PojazdSzybkobiezy, PojazdPlywajacyPoGlebokiejWodzie):
    pass

super_amfibia = SuperAmfibia()

print(super_amfibia.jedz())
print(super_amfibia.plyn())
print(super_amfibia.maksymalna_predkosc())
print(super_amfibia.zanurzenie(),"\n")

"""
Wywoła się metoda opis() z klasy, 'Pierwszej od lewej (w dziedziczeniu)
która ma metodę opis(), w tym wypadku z klasy Pojazd Wodny'

print(SuperAmfibia.__mro__)
Python szuka metod w kolejności:
1. SuperAmfibia
2. PojazdLadowy
3. PojazdWodny (z tej klasy wykona się metoda opis())
4. PojazdSzybkobiezny
5. PojazdPlywajacyPoGlebokiejWodzie
6. object  
"""
print(super_amfibia.opis())
print(SuperAmfibia.__mro__)
