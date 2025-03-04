aktualny_uzytkownik = "admin"

def sprawdz_uzytkownika(wymagany_uzytkownik):
    def dekorator(funkcja):
        def opakowanie(*args, **kwargs):
            if aktualny_uzytkownik == wymagany_uzytkownik:
                return funkcja(*args, **kwargs)
            else:
                print("Brak dostępu!")
        return opakowanie
    return dekorator

@sprawdz_uzytkownika("admin")
def usun_dane():
    print("Dane zostały usunięte.")

usun_dane()
aktualny_uzytkownik = "user"
usun_dane()
