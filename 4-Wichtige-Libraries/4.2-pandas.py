# %%
import numpy as np
import pandas as pd

# %%

daten = pd.read_csv('..\\namen.csv', sep=';')

# %%

daten.head()

# %%

daten.columns = [col.capitalize() for col in daten.columns]

# %%

daten

# %%

# Spalte
daten['Name']

# %%

# Zeile
daten.iloc[0]

# %%

daten['Alter'].aggregate(['mean', 'std', 'min', 'max'])

# %%

rand_int = np.random.randint(50,100,100)

# %%

log_rend = pd.DataFrame(np.log(rand_int)).diff()

# %%

# Installieren Sie Matplotlib um DatenFrame zu einfach plotten.
log_rend.plot(xlabel='Tagen', ylabel='Log. Rendite', title='Aktie', legend=False)

# %%
