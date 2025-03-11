"""
## Zadanie 5 - **Kompozycja vs. Dziedziczenie**

Stwórz klasy:

- **`Procesor`**, **`KartaGraficzna`**, **`PamiecRAM`**, **`DyskTwardy`**.
- **`Komputer`** – użyj kompozycji do budowy komputera.

### Do zrobienia

1. Implementacja komponentów.
2. `Komputer` powinien składać się z obiektów komponentów.
3. Spróbuj podejścia z dziedziczeniem – jakie pojawią się problemy?
"""

class Procesor:
    def __init__(self, model, taktowanie):
        self.model = model
        self.taktowanie = taktowanie

    def opis(self):
        return f"{self.model} - {self.taktowanie} GHz"

class KartaGraficzna:
    def __init__(self, model, pamiec_varm):
        self.model = model
        self.pamiec_varm = pamiec_varm

    def opis(self):
        return f"{self.model} - {self.pamiec_varm} GB VRAM"

class PamiecRAM:
    def __init__(self, pojemnosc, typ):
        self.pojemnosc = pojemnosc
        self.typ = typ

    def opis(self):
        return f"Pamięć RAM: {self.pojemnosc} GB, {self.typ}"

class DyskTwardy:
    def __init__(self, pojemnosc, typ):
        self.pojemnosc = pojemnosc
        self.typ = typ

    def opis(self):
        return f"Dysk: {self.pojemnosc} GB, {self.typ}"

class Komputer:
    def __init__(self, procesor, karta_graficzna, pamiec_ram, dysk_twardy):
        self.procesor = procesor
        self.karta_graficzna = karta_graficzna
        self.pamiec_ram = pamiec_ram
        self.dysk_twardy = dysk_twardy

    def opis(self):
        return "\n".join([
            self.procesor.opis(),
            self.karta_graficzna.opis(),
            self.pamiec_ram.opis(),
            self.dysk_twardy.opis()
        ])


procesor = Procesor("Ryzen 5 3600x", 4.4)
karta_graficzna = KartaGraficzna("NVIDIA GTX 1650 OC", 3)
pamiec_ram = PamiecRAM(32, "DDR4")
dysk = DyskTwardy(1000, "SSD") # Dysk tysiąc

komputer = Komputer(procesor, karta_graficzna, pamiec_ram, dysk)

print(komputer.opis(), "\n")

# class Komputer_dziedziczenie(Procesor, KartaGraficzna, PamiecRAM, DyskTwardy):
#     pass

# kom_dz = Komputer_dziedziczenie("Ryzen 5 3600x", 4.4, "NVIDIA GTX 1650 OC", 3, 32, "DDR4", 1000, "SSD")

"""
Traceback (most recent call last):
  File "{ścieżka}", line 76, in <module>
    kom_dz = Komputer_dziedziczenie("Ryzen 5 3600x", 4.4, "NVIDIA GTX 1650 OC", 3, 32, "DDR4", 1000, "SSD")
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Procesor.__init__() takes 3 positional arguments but 9 were given

Python przekazuje WSZYSTKIE argumenty tylko do Procesor.__init__(), bo to pierwsza klasa w kolejności MRO
"""

# poprawa

"""
Ta impolementacja działa, ale jest bardziej skomplikowana i mniej elastyczna niż kompozycja.
"""

class Komputer_dziedziczenie(Procesor, KartaGraficzna, PamiecRAM, DyskTwardy):
    def __init__(self, model_procesora, taktowanie, model_gpu, vram, ram_pojemnosc, ram_typ, dysk_pojemnosc, dysk_typ):
        Procesor.__init__(self, model_procesora, taktowanie)
        KartaGraficzna.__init__(self, model_gpu, vram)
        PamiecRAM.__init__(self, ram_pojemnosc, ram_typ)
        DyskTwardy.__init__(self, dysk_pojemnosc, dysk_typ)

    def opis(self):
        return "\n".join([
            Procesor.opis(self),
            KartaGraficzna.opis(self),
            PamiecRAM.opis(self),
            DyskTwardy.opis(self)
        ])



kom_dz2 = Komputer_dziedziczenie("Ryzen 5 3600x", 4.4, "NVIDIA GTX 1650 OC", 3, 32, "DDR4", 1000, "SSD")
print(kom_dz2.opis())