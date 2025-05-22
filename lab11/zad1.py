import tkinter as tk

def przycisk_klikniety():
    print("A NIE MÓWIŁEM?!")

okno = tk.Tk()
okno.title("Zadanie 1")

etykieta = tk.Label(okno, text="Nie klikaj tego przycisku!")
etykieta.pack(pady=10)

przycisk = tk.Button(okno, text="TEN PRZYCISK", command=przycisk_klikniety)
przycisk.pack(pady=10)

okno.mainloop()
