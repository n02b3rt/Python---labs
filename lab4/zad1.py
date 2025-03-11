def liczby_parzyste(n):
    liczba = 0
    for _ in range(n):
        yield liczba
        liczba += 2

# Przykład użycia:
gen = liczby_parzyste(5)
print(list(gen))  # Wynik: [0, 2, 4, 6, 8]
