import json
import random


def generuj_uzytkownikow(liczba):
    imiona = ["Jan", "Anna", "Piotr", "Maria", "Tomasz", "Katarzyna", "Marek", "Agnieszka"]
    nazwiska = ["Kowalski", "Nowak", "Wiśniewski", "Wójcik", "Kamiński", "Lewandowski"]
    
    for _ in range(liczba):
        yield {
            "imie": random.choice(imiona),
            "nazwisko": random.choice(nazwiska),
            "wiek": random.randint(10, 60)
        }


def zapisz_jsonl(plik, uzytkownicy):
    with open(plik, "w", encoding="utf-8") as f:
        for uzytkownik in uzytkownicy:
            f.write(json.dumps(uzytkownik, ensure_ascii=False) + "\n")


def policz_powyzej_20_lat(plik):
    licznik = 0
    with open(plik, "r", encoding="utf-8") as f:
        for linia in f:
            uzytkownik = json.loads(linia)
            if uzytkownik["wiek"] > 20:
                licznik += 1
    return licznik


def main():
    plik_jsonl = "uzytkownicy.jsonl"
    liczba_uzytkownikow = 1000

    uzytkownicy = generuj_uzytkownikow(liczba_uzytkownikow)

    zapisz_jsonl(plik_jsonl, uzytkownicy)
    print(f"Dane zapisane do {plik_jsonl}")

    liczba_powyzej_20 = policz_powyzej_20_lat(plik_jsonl)
    print(f"Liczba użytkowników powyżej 20 lat: {liczba_powyzej_20}")


if __name__ == "__main__":
    main()
