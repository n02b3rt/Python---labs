"""
4. Generator sumy kolejnych liczb
Napisz generator, który dla podanej liczby n zwróci kolejne sumy liczb od 1 do n.
# Wynik dla n = 5

# 1
# 3
# 6
# 10
# 15
"""

def suma_kolejnych_liczb(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
        yield suma

n = 5
gen = suma_kolejnych_liczb(n)

for suma in gen:
    print(suma)
