def liczby_parzyste(n):
    liczba = 0
    for _ in range(n):
        yield liczba
        liczba += 2


gen = liczby_parzyste(5)
print(list(gen))
