from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


app = FastAPI(
    title="Examen 2do Parcial",
    description="API para el examen de 2do parcial",
    version="1.0.1"
)

envios=[
    {"CodigoPostal": 12345, "Destino": "UPQ", "Peso": 10},
    {"CodigoPostal": 23456, "Destino": "Galeras", "Peso": 10},
    {"CodigoPostal": 34567, "Destino": "Hercules", "Peso": 10}
]

@app.get('/', tags=["Inicio"])
def main():
    return {'mensaje':'Bienvenido a examen'}

@app.get('/envios',tags=["Operaciones CRUD"])
def ConsultarTodos():
    return{"Usuarios Registrados ": envios}


@app.delete('/envio/{CodigoPostal}', tags=['Operacion Examen'])
def EliminarEnvio(CodigoPostal: int):
    for i in range(len(envios)):
        if envios[i]["CodigoPostal"]==CodigoPostal:
            envios.pop(i)
            return{"mensaje":"Envio eliminado"}
    raise HTTPException(status_code=404, detail="Envio no encontrado") 