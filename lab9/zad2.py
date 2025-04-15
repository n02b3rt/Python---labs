import pandas as pd
import numpy as np

# 1 - Zbuduj DataFrame o indeksie DatetimeIndex, z krokiem co godzinę, np. na przestrzeni 5 dni (120 wierszy).
date_rng = pd.date_range(start="2025-01-01", periods=120, freq='h')
df = pd.DataFrame({
    'SensorID': np.random.choice([1, 2, 3], size=120),
    'Odczyt': np.random.uniform(0, 100, size=120)
}, index=date_rng)

print("Oryginalny DataFrame:")
print(df.head())
print(f"\nLiczba wierszy: {len(df)}")

# 2 - Wykorzystaj groupby('SensorID'), następnie metodę .filter(),
# aby odrzucić te grupy (sensory), w których średni odczyt jest mniejszy niż 30.
df_filtered = df.groupby('SensorID').filter(lambda group: group['Odczyt'].mean() >= 30)
print("\nDataFrame po filtrowaniu (średni odczyt >= 30):")
print(df_filtered.head())
print(f"\nLiczba wierszy po filtrowaniu: {len(df_filtered)}")

# 3 - Użyj .apply() lub .transform() do normalizacji (np. z-Score)
# kolumny Odczyt w obrębie każdego sensora, który pozostał w zbiorze.
df_filtered['Odczyt_norm'] = df_filtered.groupby('SensorID')['Odczyt'].transform(lambda x: (x - x.mean()) / x.std())
print("\nDataFrame po normalizacji (dodano kolumnę 'Odczyt_norm'):")
print(df_filtered.head())

# 4 - Na danych (zachowanych po filtrowaniu) zrób resampling w skali 6h:
# oblicz maksymalną wartość odczytu w każdym przedziale 6-godzinnym dla każdego sensora.
resampled = df_filtered.groupby('SensorID').resample('6h').max()

print("\nResampled DataFrame (maksymalny odczyt w przedziale 6h):")
print(resampled.head())

# 5 - Wypisz wyniki i sprawdź, czy liczba wierszy zmniejszyła się w wyniku resampling.
print("\nLiczba wierszy przed resampling:", len(df_filtered))
print("Liczba wierszy po resampling:", len(resampled))
