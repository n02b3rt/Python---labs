"""
2. Generator liczb Fibonacciego
Napisz generator, który zwróci kolejne liczby Fibonacciego.
"""

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()
for _ in range(10):
    print(next(gen), end=" ")
