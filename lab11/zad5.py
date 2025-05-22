import tkinter as tk

def aktualizuj_kolor():
    r = suwak_r.get()
    g = suwak_g.get()
    b = suwak_b.get()

    kolor_hex = f"#{r:02x}{g:02x}{b:02x}"

    etykieta.config(bg=kolor_hex)

    etykieta_kolor.config(text=f"Kolor: {kolor_hex}")

okno = tk.Tk()
okno.title("Zadanie 5 - Wybór Koloru")

suwak_r = tk.Scale(okno, from_=0, to=255, orient="horizontal", label="R (Czerwony)", command=lambda x: aktualizuj_kolor())
suwak_r.pack(fill="x", padx=10, pady=5)

suwak_g = tk.Scale(okno, from_=0, to=255, orient="horizontal", label="G (Zielony)", command=lambda x: aktualizuj_kolor())
suwak_g.pack(fill="x", padx=10, pady=5)

suwak_b = tk.Scale(okno, from_=0, to=255, orient="horizontal", label="B (Niebieski)", command=lambda x: aktualizuj_kolor())
suwak_b.pack(fill="x", padx=10, pady=5)

etykieta = tk.Label(okno, text="Kolor", width=30, height=5)
etykieta.pack(pady=20)

etykieta_kolor = tk.Label(okno, text="Kolor: #000000", font=("Arial", 12))
etykieta_kolor.pack()

okno.mainloop()
