import numpy as np
import pandas as pd
import plotly.express as px

# Zadanie 8:
# - Stwórz DataFrame z dwiema lub trzema seriami danych (np. `sin`, `cos`, `tan`) i kolumną `x`.
# - Użyj Plotly Express (`px.line`), aby wyświetlić wszystkie serie na jednym interaktywnym wykresie.
# - Sprawdź możliwości przybliżania fragmentów wykresu (zoom), chowania serii w legendzie, itp.

x = np.linspace(-np.pi/2 + 0.1, np.pi/2 - 0.1, 100)

df = pd.DataFrame({
    'x': x,
    'sin': np.sin(x),
    'cos': np.cos(x),
    'tan': np.tan(x)
})

df_long = df.melt(id_vars='x', var_name='Funkcja', value_name='Wartość')

fig = px.line(df_long, x='x', y='Wartość', color='Funkcja',
              title='Interaktywny wykres funkcji trygonometrycznych',
              labels={'x': 'x (radiany)', 'Wartość': 'Wartość funkcji'})

fig.show()
