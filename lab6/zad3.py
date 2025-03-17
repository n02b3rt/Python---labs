"""
## Zadanie 3
Serializacja obiektów własnej klasy do `pickle` i `json`

1. Utworzyć klasę `Pracownik` (pola: imię, nazwisko, stanowisko, pensja).
2. Utworzyć listę obiektów klasy `Pracownik`.
3. Zserializować do `pickle`.
4. Odczytać z `pickle`.
5. Następnie spróbować zapisać do `json` (trzeba będzie napisać metodę `to_dict()`).
6. Odczytać z `json` (utworzyć znów obiekty `Pracownik`, np. przez konstruktor).
"""

import json
import random
import pickle


class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.pensja = pensja

    def to_dict(self):
        return {
            "imie": self.imie,
            "nazwisko": self.nazwisko,
            "stanowisko": self.stanowisko,
            "pensja": self.pensja
        }

    @staticmethod
    def from_dict(data):
        return Pracownik(data["imie"], data["nazwisko"], data["stanowisko"], data["pensja"])


def zapisz_pickle(plik, obiekty):
    with open(plik, "wb") as f:
        pickle.dump(obiekty, f, protocol=pickle.HIGHEST_PROTOCOL)


def odczytaj_pickle(plik):
    with open(plik, "rb") as f:
        return pickle.load(f)


def zapisz_json(plik, obiekty):
    with open(plik, "w", encoding="utf-8") as f:
        json.dump([obiekt.to_dict() for obiekt in obiekty], f, indent=4, ensure_ascii=False)


def odczytaj_json(plik):
    with open(plik, "r", encoding="utf-8") as f:
        return [Pracownik.from_dict(data) for data in json.load(f)]


def main():
    plik_pickle = "pracownicy.pickle"
    plik_json = "pracownicy.json"

    pracownicy = [
        Pracownik("Jan", "Kowalski", "Inżynier", 6000),
        Pracownik("Anna", "Nowak", "Księgowa", 5500),
        Pracownik("Piotr", "Wiśniewski", "Menadżer", 8000)
    ]

    zapisz_pickle(plik_pickle, pracownicy)
    print(f"Dane zapisane do {plik_pickle}\n")

    wczytani_pracownicy = odczytaj_pickle(plik_pickle)
    print("Odczytani pracownicy (pickle):")
    for p in wczytani_pracownicy:
        print(vars(p))

    zapisz_json(plik_json, pracownicy)
    print(f"Dane zapisane do {plik_json}\n")

    wczytani_pracownicy_json = odczytaj_json(plik_json)
    print("Odczytani pracownicy (JSON):")
    for p in wczytani_pracownicy_json:
        print(vars(p))


if __name__ == "__main__":
    main()