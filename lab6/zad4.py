"""
## Zadanie 4
Kompresja i sumy kontrolne

1. Wygenerować dużą listę (np. 10 tysięcy liczb).
2. Zserializować pickle + gzip.open do pliku duze_dane.pickle.gz.
3. Obliczyć i zapisać sumę kontrolną SHA-256.
4. Odczytać ponownie i sprawdzić, czy suma kontrolna się zgadza.
"""

import json
import random
import pickle
import gzip
import hashlib

def zapisz_pickle_gzip(plik, dane):
    with gzip.open(plik, "wb") as f:
        pickle.dump(dane, f, protocol=pickle.HIGHEST_PROTOCOL)

def odczytaj_pickle_gzip(plik):
    with gzip.open(plik, "rb") as f:
        return pickle.load(f)

def oblicz_sha256(plik):
    with open(plik, "rb") as f:
        zawartosc = f.read()
    return hashlib.sha256(zawartosc).hexdigest()

def main():
    plik_pickle_gzip = "duze_dane.pickle.gz"

    duze_dane = list(range(10000))

    zapisz_pickle_gzip(plik_pickle_gzip, duze_dane)
    print(f"Dane zapisane do {plik_pickle_gzip}")

    suma_kontrolna = oblicz_sha256(plik_pickle_gzip)
    print(f"Suma kontrolna SHA-256: {suma_kontrolna}")

    odczytane_dane = odczytaj_pickle_gzip(plik_pickle_gzip)
    nowa_suma_kontrolna = oblicz_sha256(plik_pickle_gzip)

    print(f"Czy suma kontrolna jest zgodna? {suma_kontrolna == nowa_suma_kontrolna}")
    print(f"Odczytano {len(odczytane_dane)} elementów.")

if __name__ == "__main__":
    main()
