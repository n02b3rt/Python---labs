def wielokrotne_wywolanie(n):
    def dekorator(funkcja):
        def opakowanie(*args, **kwargs):
            for _ in range(n):
                funkcja(*args, **kwargs)
        return opakowanie
    return dekorator

@wielokrotne_wywolanie(3)
def hej():
    print("Hej!")

hej()