def na_wielkie_litery(funkcja):
    def opakowanie(*args, **kwargs):
        wynik = funkcja(*args, **kwargs)
        if isinstance(wynik, str):
            return wynik.upper()
        return wynik
    return opakowanie

@na_wielkie_litery
def powiedz():
    return "to jest test"

print(powiedz())  # Wynik: "TO JEST TEST"