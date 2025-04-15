import pandas as pd
import numpy as np
import plotly.express as px

# Zadanie 9:
# - Na bazie danych z ćwiczenia Seaborn (df z paroma kolumnami) stwórz interaktywny wykres punktowy (`px.scatter`).
# - Ustaw różne kolory i rozmiary punktów w zależności od dwóch różnych kolumn (np. `color='Gatunek', size='Długość Płatka'`).
# - Dodaj wyświetlanie dodatkowej kolumny przy najechaniu myszką na punkt (parametr `hover_data=['kolumna']`).

np.random.seed(10)

df = pd.DataFrame({
    'Długość Płatka': np.random.normal(loc=5, scale=1, size=100),
    'Szerokość Płatka': np.random.normal(loc=1.5, scale=0.5, size=100),
    'Długość Działki': np.random.normal(loc=6, scale=0.8, size=100),
    'Gatunek': np.random.choice(['setosa', 'versicolor', 'virginica'], size=100, p=[0.3, 0.4, 0.3])
})

fig = px.scatter(
    df,
    x='Długość Płatka',
    y='Szerokość Płatka',
    color='Gatunek',
    size='Długość Płatka',
    hover_data=['Długość Działki'],
    title='Interaktywny wykres punktowy z danymi kwiatów'
)

fig.show()
