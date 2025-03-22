
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse 
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from tokenGen import create_token
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User
#declaramos un objeto 
app = FastAPI(
    title='Mi primer API 196', 
    description='Jose GUadalupe De la Cruz',
    version='1.0.1'
)

#levanta las tablas definidas en modelos
Base.metadata.create_all(bind=engine)


usuarios=[
    {"id":1, "nombre":"juanito","edad": 37, "correo":"ivan@example.com"},
    {"id":2, "nombre":"isaac","edad": 22, "correo":"juan@example.com"},
    {"id":3, "nombre":"bryan","edad": 21, "correo":"isaac@example.com"},
    {"id":4, "nombre":"emilito","edad": 23, "correo":"jose@example.com"}
]

#generamos nuestro primer endpoint 
# endpoint tipo get 
@app.get('/', tags=['Inicio'])
def main():
    return {'hello FastAPI':'Jose Guadalupe'}

@app.post('/auth/', tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.correo =='ivan@example.com' and autorizado.password == '12345678':
        token:str = create_token(autorizado.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return{"Aviso":"Usuario no autorizado"}


# endpoint Consultar todos 
@app.get('/usuarios',dependencies=[Depends(BearerJWT())], response_model= List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

#agregar 
@app.post('/usuarios/', response_model= modelUsuario,tags=['Operaciones CRUD'])
def guardar(usuario: modelUsuario):
    db= Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,content={"mensaje":"usuario creado", "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,content={"mensaje":"Error al guardar usuario", "Excepcion":str(e)})
    finally:
        db.close()

@app.put('/usuarios/{id}',response_model= modelUsuario,tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:modelUsuario):
    for index, urs in enumerate(usuarios): 
        if urs ["id"] == id:
            usuarios[index]= usuarioActualizado.model_dump()
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
