# %%
# Importar librerias necesarias para webscraping
import requests
from bs4 import BeautifulSoup
import pandas as pd

#%%

pagina = requests.get('https://www.tutiempo.net/clima/01-2023/ws-762253.html')
# Verificar si se puede realizar webscraping
#print(pagina)
#Obtener  Html
soup = BeautifulSoup(pagina.text, 'html.parser') 
#print(soup.prettify())

# %%
# Extraer nombre de los camposde la clase "medias mensuales numspan".
tabla = soup.find('table', class_='medias mensuales numspan')

# Encuentra todos los elementos <th> dentro de la primera fila <tr> en la tabla.
columnas = tabla.find('tr').find_all('th')

# Inicializa un arreglo para almacenar los encabezados de las columnas.
encabezados = []

#Los elementos encontrados se guarda el texto.
for columna in columnas:
    encabezados_text = columna.text.strip()
    encabezados.append(encabezados_text)
    
#print(encabezados)

# %%
#Extraer los días, temp maxima y minima 
tabla = soup.find('table', class_='medias mensuales numspan')
dias = []
temp_max = []
temp_min = []
info =[]

rows = tabla.find_all('tr')
for row in rows:
    dia_dato = row.find('strong')
    if dia_dato:
        dia_text = dia_dato.get_text()
        dias.append(dia_text)
for row in rows:
    datostemp = row.find_all('td')
    if len(datostemp) >= 4:
        max = datostemp[2].get_text()
        min = datostemp[3].get_text()
        temp_max.append(max)
        temp_min.append(min)
for row in rows:
         info.append(soup.find('h3', class_='bluecab').get_text())
#print(dias)
#print(temp_max)
#print(temp_min)
#print(info)

# %%
#Guardar en un data frame
clima = {
    'Día': dias,
    'Temp Maxima': temp_max,
    'Temp Minima': temp_min,
    'Informacion': info   
}

print(clima)


# %%
# Limpieza de datos
# Eliminar el ultimo dato de Dia, Temp Max y Temp Min, ya que no corresponde a los días

clima['Día'] = clima['Día'][:-1]
clima['Temp Maxima'] = clima['Temp Maxima'][:-1]
clima['Temp Minima'] = clima['Temp Minima'][:-1]
clima['Informacion'] = clima['Informacion'][:-3]
# Reemplazar los valores nulos por "Sin registro"
for i in range(len(clima['Temp Maxima'])):
    if clima['Temp Maxima'][i] == '':
        clima['Temp Maxima'][i] = 'Sin registro'
    if clima['Temp Minima'][i] == '':
        clima['Temp Minima'][i] = 'Sin registro'
     
     
# %%

enero_clima = pd.DataFrame(clima)

# %%
# Guardar datos en CSV
enero_clima.to_csv('datos_climaticos_cuu_ene23.csv', index=False)

