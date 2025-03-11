"""
## Zadanie 7 - Dekoratory Klas

Stwórz klasę `Osoba` z atrybutem `wiek`, używając `@property`.

### Do zrobienia

1. Atrybut `_rok_urodzenia` (prywatny).
2. `@property wiek`, który oblicza wiek na podstawie aktualnego roku.
3. Setter `wiek`, który ustawia `_rok_urodzenia`, ale nie pozwala na bezpośrednie zmiany wieku.
4. `@staticmethod` `aktualny_rok()` zwracający bieżący rok.
"""

from datetime import datetime

class Osoba:
    def __init__(self, rok_urodzenia):
        self.rok_urodzenia = rok_urodzenia

    @property
    def wiek(self):
        return self.aktualny_rok() - self.rok_urodzenia

    @wiek.setter
    def wiek(self, nowy_wiek):
        self.rok_urodzenia = self.aktualny_rok() - nowy_wiek

    @staticmethod
    def aktualny_rok():
        return datetime.now().year


print(f"Aktualny rok: {Osoba.aktualny_rok()}")

osoba = Osoba(2003)

print(f"Wiek: {osoba.wiek}")

osoba.wiek = 26
print(f"Nowy wiek: {osoba.wiek}")
print(f"Nowy rok urodzenia: {osoba.rok_urodzenia}")

