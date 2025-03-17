"""
## Zadanie 1
Mini-baza filmów w formatach CSV i JSON

1. Napisać program, który prosi użytkownika o wprowadzenie listy filmów (tytuł, rok, reżyser, gatunek).
2. Zapisuje je do pliku `filmy.csv`.
3. Następnie wczytuje `filmy.csv` i konwertuje dane do listy słowników Pythona.
4. Zapisuje tę listę do `filmy.json`.
5. Wczytuje ponownie `filmy.json` i wyświetla zawartość.
"""

import csv
import json


def wprowadz_filmy():
    filmy = []
    while True:
        tytul = input("Podaj tytuł filmu (lub ENTER aby zakończyć): ")
        if not tytul:
            break
        rok = input("Podaj rok produkcji: ")
        rezyser = input("Podaj reżysera: ")
        gatunek = input("Podaj gatunek filmu: ")

        filmy.append({
            "Tytul": tytul,
            "Rok": rok,
            "Rezyser": rezyser,
            "Gatunek": gatunek
        })
    return filmy


def zapisz_csv(filmy, plik_csv):
    with open(plik_csv, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["Tytul", "Rok", "Rezyser", "Gatunek"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(filmy)


def odczytaj_csv(plik_csv):
    with open(plik_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';')
        return list(reader)


def zapisz_json(filmy, plik_json):
    with open(plik_json, "w", encoding="utf-8") as f:
        json.dump(filmy, f, indent=4, ensure_ascii=False)


def odczytaj_json(plik_json):
    with open(plik_json, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    plik_csv = "filmy.csv"
    plik_json = "filmy.json"

    filmy = wprowadz_filmy()

    zapisz_csv(filmy, plik_csv)
    print("Dane zapisane do filmy.csv")

    filmy_z_csv = odczytaj_csv(plik_csv)

    zapisz_json(filmy_z_csv, plik_json)
    print("Dane zapisane do filmy.json")

    filmy_z_json = odczytaj_json(plik_json)
    print("Odczytane dane z filmy.json:")
    for film in filmy_z_json:
        print(film)


if __name__ == "__main__":
    main()
