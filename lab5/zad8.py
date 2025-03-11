"""
Zadanie 8 - Metaklasy

Stwórz metaklasę `WymaganaAtrybutyMetaklasa`, która sprawdza, czy klasa ma określone atrybuty.

Do zrobienia

1. `__new__()` metaklasy sprawdza obecność wymaganych atrybutów w `dct`.
2. Klasa `Produkt` z metaklasą, wymagająca `nazwa` i `cena`.
3. Klasa `Usluga`, która nie spełnia wymagań – powinna zgłosić `TypeError`.
"""

class WymaganaAtrybutyMetaklasa(type):
    def __new__(cls, name, bases, dct):
        wymagane_atrybuty = ["nazwa", "cena"]

        for attr in wymagane_atrybuty:
            if attr not in dct:
                raise TypeError(f"Klasa '{name}' musi posiadać atrybut '{attr}'")

        return super().__new__(cls, name, bases, dct)

class Produkt(metaclass=WymaganaAtrybutyMetaklasa):
    nazwa = "Komputer"
    cena = 5000

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return f"Produkt {self.nazwa}, Cena: {self.cena} zł"

produkt = Produkt("Tablet", "1600")
print(produkt)

class Usluga(metaclass=WymaganaAtrybutyMetaklasa):
    nazwa = "Naprawa Komputera"

    def __init__(self, nazwa):
        self.nazwa = nazwa


"""
raise TypeError(f"Klasa '{name}' musi posiadać atrybut '{attr}'")
TypeError: Klasa 'Usluga' musi posiadać atrybut 'cena'
"""
usluga = Usluga("Serwis tableta")



