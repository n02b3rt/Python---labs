def na_liste(funkcja):
    def opakowanie(*args, **kwargs):
        wynik = funkcja(*args, **kwargs)
        return [wynik]
    return opakowanie

@na_liste
def liczba():
    return 42

print(liczba())  # Wynik: [42]
