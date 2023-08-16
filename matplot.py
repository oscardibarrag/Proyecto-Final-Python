# %%
import pandas as pd
import matplotlib.pyplot as plt
import chardet
# %%
# Cargar los datos desde el archivo CSV
df = pd.read_csv('datos_climaticos_cuu_ene23.csv')

# %%
# Convertir la columna 'Día' a valores numéricos para poder graficar
df['Día'] = pd.to_numeric(df['Día'])

# %%
# Convertir los valores de temperatura a numéricos, excluyendo valores vacíos
df['Temp Maxima'] = pd.to_numeric(df['Temp Maxima'], errors='coerce')
df['Temp Minima'] = pd.to_numeric(df['Temp Minima'], errors='coerce')

# Calcular la temperatura promedio máxima y mínima
promedio_temp_max = df['Temp Maxima'].mean()
promedio_temp_min = df['Temp Minima'].mean()

print(f"Temperatura promedio máxima: {promedio_temp_max:.2f}")
print(f"Temperatura promedio mínima: {promedio_temp_min:.2f}")


# %%
# Crear gráfico de Temperatura Máxima
plt.figure(figsize=(10, 6))
plt.plot(df['Día'], df['Temp Maxima'], marker='o', label='Temp Maxima')
plt.plot(df['Día'], df['Temp Minima'], marker='o', label='Temp Minima')
plt.xlabel('Día')
plt.ylabel('Temperatura')
plt.title('Temperaturas Máximas y Mínimas')
plt.legend()
plt.grid(True)
plt.show()
# %%
#Revisar que codificacion tiene l csv porque me marco error
#with open('Violencia_Familiar_enero.csv', 'rb') as file:
#    result = chardet.detect(file.read()) 
#print(result['encoding'])


#Cargar archivo CSV extraido de información de oficina - Confidencial -
df2 = pd.read_csv('Violencia_Familiar_enero.csv', encoding='ISO-8859-1')

# %%
#Grafica en relacion de llamadas por día
# Contar los valores únicos
conteo_dias = df2['dia'].value_counts().sort_index()

# Crea la gráfica de barras
plt.figure(figsize=(10, 6))
plt.bar(conteo_dias.index, conteo_dias.values, color='blue')

# Configura el título y las etiquetas de los ejes
plt.title('Cantidad de Llamadas 911 por Día')
plt.xlabel('Día del Mes')
plt.ylabel('Cantidad de Llamadas')

# Muestra la gráfica
plt.show()
# %%
# Grafico convinando los 2 CSV

df['Día'] = df['Día'].astype(int)
temp =df[['Día', 'Temp Maxima']].dropna()

# Crear la gráfica
fig, ax1 = plt.subplots(figsize=(10, 6))

# Gráfica de llamadas por día
color = 'tab:blue'
ax1.set_xlabel('Día del Mes')
ax1.set_ylabel('Cantidad de Llamadas', color=color)
ax1.bar(conteo_dias.index, conteo_dias.values, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Segundo eje y para las temperaturas
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Temperatura Máxima', color=color)
ax2.plot(temp['Día'], temp['Temp Maxima'], color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

# Título y leyendas
plt.title('Cantidad de Llamadas y Temperatura Máxima por Día')
plt.tight_layout()

# Mostrar la gráfica
plt.show()
# %%
