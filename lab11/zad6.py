import tkinter as tk
import random


def sprawdz_liczbe():
    global liczba_prob
    try:
        wpisana_liczba = int(pole_wpisu.get())

        if wpisana_liczba < tajna_liczba:
            wynik.config(text="Za mało!")
        elif wpisana_liczba > tajna_liczba:
            wynik.config(text="Za dużo!")
        else:
            wynik.config(text=f"TRAFIONY ZATOPIONY! Zgadłeś za {liczba_prob} razem!")
            pole_wpisu.config(state="disabled")
            przycisk_sprawdz.config(state="disabled")
            przycisk_nowa_gra.config(state="normal")

        liczba_prob += 1
    except ValueError:
        wynik.config(text="Proszę wprowadzić liczbę!")


def nowa_gra():
    global liczba_prob, tajna_liczba
    liczba_prob = 1
    tajna_liczba = random.randint(1, 100)
    wynik.config(text="Zgadnij liczbę od 1 do 100:")
    pole_wpisu.config(state="normal")
    przycisk_sprawdz.config(state="normal")
    przycisk_nowa_gra.config(state="disabled")


okno = tk.Tk()
okno.title("Zgadnij Liczbę")

tajna_liczba = random.randint(1, 100)
liczba_prob = 1

tk.Label(okno, text="Zgadnij liczbę od 1 do 100:").pack(pady=10)

pole_wpisu = tk.Entry(okno)
pole_wpisu.pack(pady=5)

przycisk_sprawdz = tk.Button(okno, text="Sprawdź!", command=sprawdz_liczbe)
przycisk_sprawdz.pack(pady=5)

wynik = tk.Label(okno, text="Wpisz liczbę i kliknij 'Sprawdź!'")
wynik.pack(pady=10)

przycisk_nowa_gra = tk.Button(okno, text="Nowa Gra", command=nowa_gra, state="disabled")
przycisk_nowa_gra.pack(pady=10)

okno.mainloop()
