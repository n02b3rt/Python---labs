"""
3. Generator filtrujący wartości
Napisz generator, który zwróci tylko liczby większe niż np. 10 z podanej listy.
"""

def filtruj_wieksze_niz_10(lista):
    for liczba in lista:
        if liczba > 10:
            yield liczba

dane = [4, 11, 8, 15, 3, 22, 7, 18]
gen = filtruj_wieksze_niz_10(dane)

print(list(gen))
