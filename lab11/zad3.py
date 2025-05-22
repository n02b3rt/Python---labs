import tkinter as tk

def oblicz(operacja):
    try:
        liczba1 = float(entry1.get())
        liczba2 = float(entry2.get())

        if operacja == '+':
            wynik = liczba1 + liczba2
        elif operacja == '-':
            wynik = liczba1 - liczba2
        elif operacja == '*':
            wynik = liczba1 * liczba2
        elif operacja == '/':
            if liczba2 == 0:
                wynik = "Błąd: Dzielnie przez zero!"
            else:
                wynik = liczba1 / liczba2

        etykieta_wynik.config(text=f"Wynik: {wynik}")

    except ValueError:
        etykieta_wynik.config(text="Błąd: Wpisz liczby!")


okno = tk.Tk()
okno.title("Zadanie 3 - Kalkulator")

tk.Label(okno, text="Liczba 1:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry1 = tk.Entry(okno)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(okno, text="Liczba 2:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry2 = tk.Entry(okno)
entry2.grid(row=1, column=1, padx=5, pady=5)

ramka_przyciskow = tk.Frame(okno)
ramka_przyciskow.grid(row=2, column=0, columnspan=2, pady=10)

btn_plus = tk.Button(ramka_przyciskow, text="+", width=5, command=lambda: oblicz('+'))
btn_plus.pack(side=tk.LEFT, padx=5)
btn_minus = tk.Button(ramka_przyciskow, text="-", width=5, command=lambda: oblicz('-'))
btn_minus.pack(side=tk.LEFT, padx=5)
btn_mnozenie = tk.Button(ramka_przyciskow, text="*", width=5, command=lambda: oblicz('*'))
btn_mnozenie.pack(side=tk.LEFT, padx=5)
btn_dzielenie = tk.Button(ramka_przyciskow, text="/", width=5, command=lambda: oblicz('/'))
btn_dzielenie.pack(side=tk.LEFT, padx=5)

etykieta_wynik = tk.Label(okno, text="Wynik: ...")
etykieta_wynik.grid(row=3, column=0, columnspan=2, pady=10)

okno.mainloop()
