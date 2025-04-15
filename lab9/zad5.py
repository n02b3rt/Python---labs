import pandas as pd
import numpy as np
import os
import time

# Zadanie 5.1:
# Wygeneruj w pamięci DataFrame o rozmiarze co najmniej 50000 wierszy.
# (np. z 3–4 kolumnami, w tym jedna kategoryczna i jedna liczbowa)

n_rows = 50000
df_large = pd.DataFrame({
    'ID': range(n_rows),
    'Kategoria': np.random.choice(['A', 'B', 'C', 'D'], size=n_rows),
    'Wartosc': np.random.uniform(0, 1000, size=n_rows),
    'Data': pd.date_range('2025-01-01', periods=n_rows, freq='min')
})

# Zadanie 5.2:
# Zapisz go do zwykłego CSV, a następnie do formatu HDF5.
# (z użyciem pd.HDFStore i parametru format='table')

csv_filename = 'large_data.csv'
df_large.to_csv(csv_filename, index=False)
print("CSV zapisany:", csv_filename)

hdf5_filename = 'large_data.h5'
store = pd.HDFStore(hdf5_filename, mode='w', complevel=9, complib='blosc')
store.put('data', df_large, format='table', data_columns=True)
store.close()
print("HDF5 zapisany:", hdf5_filename)

# Zadanie 5.3:
# Porównaj wielkość plików na dysku oraz czas odczytu.
# (Możesz użyć %timeit w notebooku lub innego sposobu na pomiar czasu.)

csv_size = os.path.getsize(csv_filename)
hdf5_size = os.path.getsize(hdf5_filename)
print("\nRozmiary plików:")
print("CSV: {} KB".format(round(csv_size / 1024, 2)))
print("HDF5: {} KB".format(round(hdf5_size / 1024, 2)))

start_time = time.time()
df_csv = pd.read_csv(csv_filename)
csv_read_time = time.time() - start_time

start_time = time.time()
store = pd.HDFStore(hdf5_filename, mode='r')
df_hdf5 = store.select('data')
store.close()
hdf5_read_time = time.time() - start_time

print("\nCzasy odczytu:")
print("CSV: {:.4f} s".format(csv_read_time))
print("HDF5: {:.4f} s".format(hdf5_read_time))
