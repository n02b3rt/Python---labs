import numpy as np
import pandas as pd
import plotly.express as px

# Zadanie 10:
# - Wykorzystaj dane z poprzednich zadań (np. rozkład wag albo sprzedaży).
# - Stwórz histogram z 15-20 przedziałami (`nbins=15` lub `nbins=20`).
# - Dodaj pionową linię oznaczającą średnią (funkcja `add_vline`), aby studenci zobaczyli,
# jak można wzbogacić wykres o dodatkowe elementy interaktywne.

np.random.seed(42)

data = np.random.normal(loc=5, scale=1, size=100)
df = pd.DataFrame({'SpadekWagi': data})

srednia = df['SpadekWagi'].mean()

fig = px.histogram(df, x='SpadekWagi', nbins=15,
                   title='Histogram spadku wagi z 15 przedziałami',
                   labels={'SpadekWagi': 'Spadek wagi (kg)'},
                   opacity=0.8)

fig.add_vline(x=srednia, line_dash='dash', line_color='red',
              annotation_text=f"Średnia: {srednia:.2f}", annotation_position="top right")

fig.show()
