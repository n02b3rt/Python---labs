import pandas as pd

# Zadanie 2.1
data = {
    'imie': ['Anna', 'Jan', 'Piotr', 'Kasia'],
    'wiek': [24, 22, 25, 23],
    'miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Poznań']
}
df = pd.DataFrame(data)
print("Utworzony DataFrame:")
print(df)

# Zadanie 2.2

print("\nPierwsze 2 wiersze:")
print(df.head(2))

print("\nPodsumowanie informacji o DataFrame:")
df.info()

print("\nStatystyki opisowe:")
print(df.describe())

print("\nNazwy kolumn:")
print(df.columns)

# Zadanie 2.3

print("\nKolumna 'imie':")
print(df['imie'])

print("\nWiersz o indeksie 1:")
print(df.loc[1])

print("\nWiersze, gdzie wiek jest większy niż 23:")
print(df[df['wiek'] > 23])
