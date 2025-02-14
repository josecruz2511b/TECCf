
from fastapi import FastAPI, HTTPException 
from typing import Optional 
#declaramos un objeto 
app = FastAPI(
    title='Mi primer API 196', 
    description='Jose GUadalupe De la Cruz',
    version='1.0.1'
)

usuarios=[
    {"id":1, "nombre":"juanito","edad": 37},
    {"id":2, "nombre":"isaac","edad": 22},
    {"id":3, "nombre":"bryan","edad": 21},
    {"id":4, "nombre":"emilito","edad": 23}
]

#generamos nuestro primer endpoint 
# endpoint tipo get 
@app.get('/', tags=['Inicio'])
def main():
    return {'hello FastAPI':'Jose Guadalupe'}

# endpoint Consultar todos 
@app.get('/usuarios',tags=['Operaciones CRUD'])
def ConsultarTodos():
    return{"Usuarios Registrados ": usuarios}

@app.post('/usuarios/',tags=['Operaciones CRUD'])
def guardar(usuario:dict):
    for usr in usuarios: 
        if usr ["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El id ya esta hechale coco")
    usuarios.append(usuario)
    return usuario

@app.put('/usuarios/{id}',tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:dict):
    for index, urs in enumerate(usuarios): 
        if urs ["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El id ya no existe")

#endpoint para eliminar usuario
@app.delete('/usuarios/{id}',tags=["Operaciones CRUD"])
def EliminarUsuario(id:int):
    for i in range(len(usuarios)):
        if usuarios[i]["id"]==id:
            usuarios.pop(i)
            return {"mensaje":"usuario eliminado"}
    raise HTTPException(status_code=404,detail="usuario no encontrado")