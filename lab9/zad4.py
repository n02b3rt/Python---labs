import pandas as pd
import numpy as np

# 1:
# Przygotuj dwie tabele:
#   - Klienci: kolumny KlientID, NazwaKlienta, Kraj
#   - Zamowienia: kolumny ZamowienieID, KlientID, DataZamowienia, Kwota
# (wygeneruj kilkanaście/dziesiąt wierszy, tak by niektóre KlientID występowały tylko w jednej tabeli)

df_klienci = pd.DataFrame({
    'KlientID': [1, 2, 3, 4, 5],
    'NazwaKlienta': ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon'],
    'Kraj': ['Polska', 'Niemcy', 'Francja', 'Hiszpania', 'Włochy']
})

df_zamowienia = pd.DataFrame({
    'ZamowienieID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'KlientID': [2, 3, 2, 6, 7, 3, 4, 2, 5, 8, 4, 3],  # KlientID 6,7,8 nie występują w df_klienci
    'DataZamowienia': pd.to_datetime([
        "2025-03-01", "2025-03-05", "2025-03-10", "2025-03-15", "2025-03-20", 
        "2025-03-25", "2025-03-27", "2025-03-28", "2025-03-29", "2025-04-01", 
        "2025-04-02", "2025-04-03"
    ]),
    'Kwota': [100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 600.0, 650.0]
})

print("Tabela Klienci:")
print(df_klienci)
print("\nTabela Zamowienia:")
print(df_zamowienia)

# 2:
# Zrób łączenie (merge) typu inner – sprawdź, ile rekordów wyszło.
# Następnie zrób to samo z left, right i outer i porównaj wyniki.

# Merge inner
inner_merge = pd.merge(df_klienci, df_zamowienia, how='inner', on='KlientID')
print("\nMerge inner - liczba rekordów:", len(inner_merge))
print(inner_merge)

# Merge left
left_merge = pd.merge(df_klienci, df_zamowienia, how='left', on='KlientID')
print("\nMerge left - liczba rekordów:", len(left_merge))
print(left_merge)

# Merge right
right_merge = pd.merge(df_klienci, df_zamowienia, how='right', on='KlientID')
print("\nMerge right - liczba rekordów:", len(right_merge))
print(right_merge)

# Merge outer
outer_merge = pd.merge(df_klienci, df_zamowienia, how='outer', on='KlientID')
print("\nMerge outer - liczba rekordów:", len(outer_merge))
print(outer_merge)

# 3:
# Dodaj trzecią tabelę Reklamacje z kolumnami ZamowienieID i PowodReklamacji.
# Wybierz 3-4 zamówienia, gdzie są reklamacje.

df_reklamacje = pd.DataFrame({
    'ZamowienieID': [102, 105, 107, 110],
    'PowodReklamacji': ["Opóźnienie", "Błąd w produkcie", "Niezgodność zamówienia", "Uszkodzenie przesyłki"]
})
print("\nTabela Reklamacje:")
print(df_reklamacje)

# 4:
# Połącz wynikiowo wszystkie trzy tabele w jedną, tak aby finalnie mieć kolumny:
# KlientID, NazwaKlienta, DataZamowienia, Kwota, PowodReklamacji.
# (Możesz użyć kolejnych merge, lub najpierw skleić zamówienia z reklamacjami, a potem połączyć to z tabelą klientów.)

zamowienia_reklamacje = pd.merge(df_zamowienia, df_reklamacje, how='left', on='ZamowienieID')

final_df = pd.merge(zamowienia_reklamacje, df_klienci, how='left', on='KlientID')

final_df = final_df[['KlientID', 'NazwaKlienta', 'DataZamowienia', 'Kwota', 'PowodReklamacji']]
print("\nFinalna tabela po łączeniu wszystkich trzech tabel:")
print(final_df)

# 5:
# Stwórz dwa DataFrame z danymi z różnych lat (np. df_2024 i df_2025),
# a potem użyj pd.concat w pionie, aby uzyskać jedną tabelę z informacją o zamówieniach wieloletnich.
# Zobacz, co dzieje się z indeksami (jeśli się powtarzają, użyj ignore_index=True).

df_2024 = pd.DataFrame({
    'ZamowienieID': [201, 202, 203],
    'KlientID': [2, 3, 4],
    'DataZamowienia': pd.to_datetime(["2024-03-01", "2024-03-05", "2024-03-10"]),
    'Kwota': [100.0, 200.0, 300.0]
})

df_2025 = pd.DataFrame({
    'ZamowienieID': [204, 205, 206],
    'KlientID': [2, 4, 5],
    'DataZamowienia': pd.to_datetime(["2025-03-01", "2025-03-05", "2025-03-10"]),
    'Kwota': [150.0, 250.0, 350.0]
})

df_multi_year = pd.concat([df_2024, df_2025], ignore_index=True)
print("\nTabela zamówień wieloletnich (po pd.concat z ignore_index=True):")
print(df_multi_year)
