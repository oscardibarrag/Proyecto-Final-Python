# %%

import pandas as pd
import sqlite3
# %%

llamadas = pd.read_csv('../Violencia_Familiar_enero.csv', encoding='ISO-8859-1')
temperaturas = pd.read_csv('../datos_climaticos_cuu_ene23.csv')

# %%

# Conexión a la base de datos (creará un nuevo archivo si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')

# Guardar el DataFrame de violencia_familiar en una tabla llamadas en este caso se reemplaza los datos
llamadas.to_sql('llamadas', conn, index=False, if_exists='replace')

# Guardar el DataFrame de temperaturas en una tabla temperaturas en este caso se reemplaza los datos
temperaturas.to_sql('temperaturas', conn, index=False, if_exists='replace')

# Cerrar la conexión
conn.close()
# %%
