# %%

import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
# %%

class Item(BaseModel):
    fid: int
    fecha: str
    hora: str
    dia: int
    mes: int
    prioridad: str
    estatus: str
    localidad: str
    colonia: str
    genero:str
    coordx: int
    coordy: int
    
app = FastAPI()

# %%
ruta = 'C:\\Users\\DIEID\\Desktop\\Proyecto Final Python Intermedio\\Base_datos\\mi_base_de_datos.db'
@app.post("/agregar_elemento/")
async def agregar_elemento(item: Item):
    
    conn = sqlite3.connect(ruta)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO llamadas (fid,fecha,hora,dia,mes,prioridad,estatus,localidad,colonia,genero rel,coordx,coordy) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (item.fid, item.fecha, item.hora, item.dia, item.mes, item.prioridad, item.estatus, item.localidad, item.colonia, item.genero, item.coordx, item.coordy ))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos agregados exitosamente"}

# %%

@app.get("/leer_elementos/")
async def leer_elementos():
    
    conn = sqlite3.connect(ruta)
    cursor = conn.cursor()
    cursor.execute("SELECT fid,fecha,hora,dia,mes,prioridad,estatus,localidad,colonia,genero rel FROM llamadas")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"fid": resultado[0], "fecha": resultado[1], "hora": resultado[2], "dia": resultado[3], "mes": resultado[4], "prioridad":[5],"estatus":[6],"localidad":[7],"colonia":[8], "genero rel":[9]} for resultado in resultados]
    else:
        return {"mensaje": "No hay datos en la base de datos"}
    
# %%

@app.get("/leer_elemento/{id}/")
async def leer_elemento(id: int):
    
    conn = sqlite3.connect(ruta)
    cursor = conn.cursor()
    cursor.execute("SELECT fid,fecha,hora,dia,mes,prioridad,estatus,localidad,colonia,genero rel FROM llamadas WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado is not None:
        return {"fid": resultado[0], "fecha": resultado[1], "hora": resultado[2], "dia": resultado[3], "mes": resultado[4], "prioridad":[5],"estatus":[6],"localidad":[7],"colonia":[8], "genero rel":[9]}
    else:
        return {"mensaje": "Datos no encontrados"}
    
# %%

@app.put("/actualizar_elemento/{id}/")
async def actualizar_elemento(id: int, item: Item):
    
    conn = sqlite3.connect(ruta)
    cursor = conn.cursor()
    cursor.execute("UPDATE llamadas SET fid=?, fecha=?, hora=?, dia=?, mes=?, prioridad=?, estatus=?, localidad=?, colonia=?, genero rel=?, coordx=?, coordy=?", (item.fid, item.fecha, item.hora, item.dia, item.mes, item.prioridad, item.estatus, item.localidad, item.colonia, item.genero, item.coordx, item.coordy ))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos actualizados exitosamente"}

# %%

@app.delete("/eliminar_elemento/{id}/")
async def eliminar_elemento(id: int):
    
    conn = sqlite3.connect(ruta)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM llamadas WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos eliminados exitosamente"}


# %%
