import pandas as pd
import numpy as np

# 1 - Utworzenie DataFrame z danymi
names = ['Anna', 'Piotr', 'Katarzyna', 'Marek', 'Ewa', 'Jan', 'Aleksandra', 'Tomasz', 'Monika', 'Robert']
ages = np.random.randint(20, 51, size=10)  # Wiek z przedziału 20-50
cities = np.random.choice(['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław'], size=10)
salaries = np.random.randint(3000, 8001, size=10)  # Zarobki z przedziału 3000-8000

df = pd.DataFrame({
    'Imie': names,
    'Wiek': ages,
    'Miasto': cities,
    'Zarobki': salaries
})

print("Oryginalny DataFrame:\n", df)

# 2 - Filtrowanie za pomocą metody .query()
filtered_df = df.query("Wiek >= 25 and Wiek <= 40 and (Miasto == 'Kraków' or Miasto == 'Wrocław') and Zarobki > 5000").copy()
print("\nFiltrowany DataFrame (Wiek 25-40, Miasto Kraków lub Wrocław, Zarobki > 5000):\n", filtered_df)

# 3 - Definicja funkcji transformujących

def calculate_tax(dataframe):
    dataframe.loc[:, 'Podatek'] = dataframe['Zarobki'] * 0.2
    return dataframe

def add_net_salary(dataframe):
    dataframe.loc[:, 'Netto'] = dataframe['Zarobki'] - dataframe['Podatek']
    return dataframe


# 4 - Łańcuchowe wywołanie funkcji przy pomocy .pipe()
result = (
    filtered_df
    .pipe(calculate_tax)
    .pipe(add_net_salary)
)

print("\nFinalny DataFrame po transformacjach (dodano 'Podatek' i 'Netto'):\n", result)
