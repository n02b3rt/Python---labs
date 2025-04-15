import pandas as pd
import numpy as np

# 1 - Utworzenie „szerokiego” DataFrame:
#    - Indeks: 'Produkt1', 'Produkt2', 'Produkt3'
#    - Kolumny: 'Sty_2025', 'Lut_2025', 'Mar_2025' z przykładowymi wartościami sprzedaży
df_wide = pd.DataFrame({
    'Sty_2025': [120, 150, 200],
    'Lut_2025': [130, 160, 210],
    'Mar_2025': [140, 170, 220]
}, index=['Produkt1', 'Produkt2', 'Produkt3'])

print("DataFrame w formacie szerokim:")
print(df_wide)

# 2 - Przekształcenie do formatu "długiego" z użyciem .melt():
# Najpierw resetujemy indeks, aby 'Produkt' stał się zwykłą kolumną.
df_long = df_wide.reset_index().melt(id_vars='index', 
                                      var_name='Miesiąc', 
                                      value_name='WartośćSprzedaży')
# Zmieniamy nazwę kolumny 'index' na 'Produkt'
df_long = df_long.rename(columns={'index': 'Produkt'})

print("\nDataFrame w formacie długim (po melt):")
print(df_long)

# 3 - Dodanie kolumny 'Tagi' do tabeli z produktami:
# Przykładowe przypisanie tagów dla poszczególnych produktów.
tags = {
    'Produkt1': ['promocja', 'hit'],
    'Produkt2': ['nowy', 'drogi'],
    'Produkt3': ['wyprzedaż', 'hit', 'ekskluzywny']
}
# Mapowanie tagów do kolumny 'Produkt'
df_long['Tagi'] = df_long['Produkt'].map(tags)

print("\nDataFrame po dodaniu kolumny 'Tagi':")
print(df_long)

# 4 - Rozpakowanie list w kolumnie 'Tagi' przy pomocy .explode():
df_exploded = df_long.explode('Tagi')

print("\nDataFrame po explode kolumny 'Tagi':")
print(df_exploded)

# Sprawdzenie, ile wierszy było przed i po explode
print("\nLiczba wierszy przed explode:", len(df_long))
print("Liczba wierszy po explode:", len(df_exploded))
