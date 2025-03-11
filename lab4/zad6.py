"""
6. Generator nieskończonej sekwencji imion
Masz listę imion. Napisz generator, który nieskończenie długo zwraca kolejne imiona z listy (i zaczyna od nowa, gdy skończy).
# Wynik dla imion = ["Ala", "Janek", "Heniek"] :

# "Ala"
# "Janek"
# "Heniek"
# "Ala"  (zaczyna od nowa)
"""

def nieskonczony_generator(imiona):
    while True:
        for imie in imiona:
            yield imie

imiona = ["Ala", "Janek", "Heniek"]
gen = nieskonczony_generator(imiona)

for i, imie in zip(range(10), gen):
    print(i,imie)