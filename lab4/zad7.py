"""
7. Generator liczb pierwszych
Napisz generator, który zwróci `n` liczb pierwszych.
"""

def generator_liczb_pierwszych(n):
    liczba = 2
    znalezione = 0

    while znalezione < n:
        if all(liczba % d != 0 for d in range(2, int(liczba ** 0.5) + 1)):
            yield liczba
            znalezione += 1
        liczba += 1

gen = generator_liczb_pierwszych(10)
print(list(gen))