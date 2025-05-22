import tkinter as tk

def przycisk_klikniety():
    imie = pole_imie.get()
    if not imie:
        imie = "Nieznajomy"
    etykieta_wynik.config(text=f"Cześć, {imie}! Wyglądasz dziś....")

okno = tk.Tk()
okno.title("Zadanie 2")

etykieta_instrukcja = tk.Label(okno, text="Podaj swoje imię:")
etykieta_instrukcja.pack(pady=10)

pole_imie = tk.Entry(okno)
pole_imie.pack(pady=5)

przycisk_ok = tk.Button(okno, text="OK", command=przycisk_klikniety)
przycisk_ok.pack(pady=10)

etykieta_wynik = tk.Label(okno, text="Cześć, ...! Wyglądasz dziś....")
etykieta_wynik.pack(pady=10)

okno.mainloop()
