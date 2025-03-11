"""
## Zadanie 2 - Polimorfizm i Duck Typing

Stwórz klasy:

- **`Fortepian`**, **`Skrzypce`**, **`Gitara`** – każda ma metodę `graj()`, która wypisuje specyficzny dźwięk instrumentu.

### Do zrobienia

1. Napisz funkcję `koncert(instrumenty)`, która iteruje po liście instrumentów i wywołuje `graj()`.
2. Stwórz instancje i przekaż je do `koncert()`.
3. Dodaj klasę `Flet` z metodą `graj()` i sprawdź, czy funkcja `koncert()` nadal działa.
"""

class Fortepian:
    def graj(self):
        print("Fortepian gra")

class Skrzypce:
    def graj(self):
        print("Skrzypce grają")

class Gitara:
    def graj(self):
        print("Gitara gra")

def koncert(instrumenty):
    for instrument in instrumenty:
        instrument.graj()

fortepian = Fortepian()
skrzypce = Skrzypce()
gitara = Gitara()

instrumenty = [fortepian, skrzypce, gitara]

koncert(instrumenty)

class Flet:
    def graj(self):
        print("Flet gra")

flet = Flet()

instrumenty.append(flet)

print("\npo dodaniu fleta\n")
koncert(instrumenty) # nadal działa