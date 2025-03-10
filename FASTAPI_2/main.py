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
    raise HTTPException(status_code=400, detail="El id  no existe")
        
        
@app.post('/listareas/',tags=['Crear una nueva tarea.'])
def nuevo(tarea:dict):
    for usr in tareas: 
        if usr ["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="El id ya esta hechale coco")
    tareas.append(tarea)
    return tarea

@app.put('/listatareas/{id}',tags=['Actualizar una tarea existente.'])
def actualizar(id:int, tareaActualizado:dict):
    for index, urs in enumerate(tareas): 
        if urs ["id"] == id:
            tareas[index].update(tareaActualizado)
            return tareas[index]
    raise HTTPException(status_code=400, detail="El id ya no existe")

@app.delete('/listatareas/{id}',tags=["Eliminar una tarea."])
def EliminarTarea(id:int):
    for i in range(len(tareas)):
        if tareas[i]["id"]==id:
            tareas.pop(i)
            return {"mensaje":"tarea eliminado"}
    raise HTTPException(status_code=404,detail="tarea no encontrado")
