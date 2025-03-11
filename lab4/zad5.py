"""
5. Generator odwracający stringa
Napisz generator, który zwróci kolejne litery stringa od końca.
# Wynik dla "python":

# n
# o
# h
# t
# y
# p
"""

def odwracanie_stringa(tekst):
    for litera in reversed(tekst):
        yield litera

string = "python"
gen = odwracanie_stringa(string)

for litera in gen:
    print(litera)
