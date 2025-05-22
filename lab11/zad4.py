import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import font

def aktualizuj_liczniki(event=None):
    tekst = text_box.get("1.0", tk.END)
    liczba_znakow = len(tekst) - 1
    liczba_slow = len(tekst.split())
    licznik_znakow.config(text=f"Znaki: {liczba_znakow}")
    licznik_slow.config(text=f"Słowa: {liczba_slow}")

def zmien_czcionke():
    nowa_czcionka = simpledialog.askstring("Zmiana czcionki", "Podaj nazwę czcionki (np. Arial):")
    if nowa_czcionka:
        text_box.config(font=(nowa_czcionka, 12))

def nowy_plik():
    if len(text_box.get("1.0", tk.END)) > 1:
        if not messagebox.askyesno("Nowy plik", "Czy na pewno chcesz wyczyścić? Niezapisane zmiany przepadną!"):
            return
    text_box.delete("1.0", tk.END)

def otworz_plik():
    sciezka = filedialog.askopenfilename(filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")])
    if not sciezka: return
    try:
        with open(sciezka, 'r', encoding='utf-8') as plik:
            zawartosc = plik.read()
            text_box.delete("1.0", tk.END)
            text_box.insert("1.0", zawartosc)
            okno.title(f"Notatnik - {sciezka}")
    except Exception as e:
        messagebox.showerror("Błąd otwarcia", f"Nie udało się otworzyć pliku: {e}")

def zapisz_plik_jako():
    sciezka = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")])
    if not sciezka: return
    try:
        with open(sciezka, 'w', encoding='utf-8') as plik:
            plik.write(text_box.get("1.0", tk.END))
            okno.title(f"Notatnik - {sciezka}")
    except Exception as e:
        messagebox.showerror("Błąd zapisu", f"Nie udało się zapisać pliku: {e}")

okno = tk.Tk()
okno.title("Notatnik")
okno.geometry("600x400")

text_box = tk.Text(okno, wrap='word', undo=True)
text_box.pack(expand=True, fill='both')

licznik_znakow = tk.Label(okno, text="Znaki: 0")
licznik_znakow.pack(side=tk.LEFT, padx=5, pady=5)

licznik_slow = tk.Label(okno, text="Słowa: 0")
licznik_slow.pack(side=tk.LEFT, padx=5, pady=5)

menubar = tk.Menu(okno)

menu_plik = tk.Menu(menubar, tearoff=0)
menu_plik.add_command(label="Nowy", command=nowy_plik, accelerator="Ctrl+N")
menu_plik.add_command(label="Otwórz", command=otworz_plik, accelerator="Ctrl+O")
menu_plik.add_command(label="Zapisz jako...", command=zapisz_plik_jako, accelerator="Ctrl+S")
menu_plik.add_separator()
menu_plik.add_command(label="Wyjście", command=okno.quit)
menubar.add_cascade(label="Plik", menu=menu_plik)

menu_edytuj = tk.Menu(menubar, tearoff=0)
menu_edytuj.add_command(label="Zmiana czcionki", command=zmien_czcionke)
menubar.add_cascade(label="Edycja", menu=menu_edytuj)

okno.config(menu=menubar)

okno.bind_all("<Control-n>", lambda event: nowy_plik())
okno.bind_all("<Control-o>", lambda event: otworz_plik())
okno.bind_all("<Control-s>", lambda event: zapisz_plik_jako())

text_box.bind("<KeyRelease>", aktualizuj_liczniki)

okno.mainloop()
