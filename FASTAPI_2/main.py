from fastapi import FastAPI, HTTPException 
from typing import Optional 
#declaramos un objeto 
app = FastAPI(
    title='Mi primer API 196', 
    description='Jose GUadalupe De la Cruz',
    version='1.0.1'
)

tareas=[
    {"id":1, "titulo":"Estudiar para el examen", "descripcion": "Reparar los apuntes de TAI", "vencimiento":"14-02-24", "Estado":"Completada"},
    {"id":2, "titulo":"Desayunar", "descripcion": "Desayunar para tener energias", "vencimiento":"15-02-24", "Estado":"Completada"},
    {"id":3, "titulo":"Ir al gimnasio", "descripcion": "Ir a reventar vena", "vencimiento":"16-02-24", "Estado":"No Completada"},
    {"id":4, "titulo":"Tarea", "descripcion": "Terminar la tarea", "vencimiento":"16-02-24", "Estado":"Completada"}
]

@app.get('/', tags=['Inicio'])
def main():
    return {'Listas Tareas':'Jose Guadalupe'}


@app.get('/listareas',tags=['Operaciones CRUD'])
def ConsultarTodos():
    return{"Lista de Tareas ": tareas}

@app.get('/listareas/{id}',tags=['Obtener una tarea específica por su ID.'])
def obtener(id:int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
        
@app.post('/listareas/',tags=['Crear una nueva tarea.'])
def nuevo(tarea:dict):
    for usr in tareas: 
        if usr ["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="El id ya esta hechale coco")
    tareas.append(tarea)
    return tarea