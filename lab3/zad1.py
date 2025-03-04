def licz_wywolania(funkcja):
    licznik = 0  # Zmienna do liczenia wywołań

    def opakowanie():
        # Zmienna nonlocal pozwala zmieniać wartość zmiennej z funkcji wyżej, zamiast tworzyć nową. Używa się jej w funkcjach zagnieżdżonych.
        nonlocal licznik  # Używamy nonlocal, aby zmieniać licznik
        licznik += 1  # Zwiększamy licznik
        funkcja()  # Wywołujemy oryginalną funkcję
        print(f"Funkcja {funkcja.__name__} została wywołana {licznik} razy.")

    return opakowanie  # Zwracamy opakowaną funkcję


@licz_wywolania
def powitanie():
    print("Cześć!")


powitanie()
powitanie()
powitanie()
