import pandas as pd

# Zadanie 3.1

data_nan = {
    'kolumna1': [1, 2, None, 4],
    'kolumna2': [5, None, 7, 8]
}
df_nan = pd.DataFrame(data_nan)

print("DataFrame df_nan (z NaN):")
print(df_nan)


df_nan_filled = df_nan.fillna(0)
print("\nDataFrame df_nan po wypełnieniu NaN zerami:")
print(df_nan_filled)

# Zadanie 3.2

data_tekst = {'tekst': ['  duże LITERY ', 'małe litery  ', 'Mieszane Litery ']}
df_tekst = pd.DataFrame(data_tekst)

print("\nOryginalny DataFrame z tekstem:")
print(df_tekst)

df_tekst_lower = df_tekst.copy()
df_tekst_lower['tekst'] = df_tekst_lower['tekst'].str.lower()
print("\nTekst zamieniony na małe litery:")
print(df_tekst_lower)

df_tekst_stripped = df_tekst.copy()
df_tekst_stripped['tekst'] = df_tekst_stripped['tekst'].str.strip()
print("\nTekst po usunięciu białych znaków z początku i końca:")
print(df_tekst_stripped)
