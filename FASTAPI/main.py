
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse 
from fastapi.encoders import jsonable_encoder
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


#generamos nuestro primer endpoint 
# endpoint tipo get 
@app.get('/', tags=['Inicio'])
def main():
    return {'hello FastAPI':'Jose Guadalupe'}


# endpoint Consultar todos 
@app.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    db= Session()
    try:
        consulta= db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500,content={"mensaje":"No fue posible consultar", "Excepcion":str(x)})

    finally:
        db.close()

@app.get('/usuarios/{id}', tags=['Operaciones CRUD'])
def ConsultarUno(id:int):
    db= Session()
    try:
        consulta= db.query(User).filter(User.id==id).first()
        if not consulta:
            return JSONResponse(status_code=404,content={"mensaje":"Usuario no encontrado"})
        return JSONResponse(content= jsonable_encoder(consulta))
    
    except Exception as b:
        return JSONResponse(status_code=500,content={"mensaje":"No fue posible consultar", "Excepcion":str(b)})

    finally:
        db.close()


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

@app.put('/usuarios/{id}',tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:modelUsuario):
    db= Session()
    try:
        consulta= db.query(User).filter(User.id==id).first()
        if not consulta:
            return JSONResponse(status_code=404,content={"mensaje":"Usuario no encontrado"})
        db.query(User).filter(User.id==id).update(usuarioActualizado.model_dump())
        db.commit()
        return JSONResponse(status_code=200,content={"mensaje":"usuario actualizado", "usuario": usuarioActualizado.model_dump()})
    except Exception as t:
        db.rollback()
        return JSONResponse(status_code=500,content={"mensaje":"Error al actualizar usuario", "Excepcion":str(t)})
    finally:
        db.close()

#endpoint para eliminar usuario
@app.delete('/usuarios/{id}',tags=["Operaciones CRUD"])
def EliminarUsuario(id:int):
    db= Session()
    try:
        consulta= db.query(User).filter(User.id==id).first()
        if not consulta:
            return JSONResponse(status_code=404,content={"mensaje":"Usuario no encontrado"})
        db.query(User).filter(User.id==id).delete()
        db.commit()
        return JSONResponse(status_code=200,content={"mensaje":"usuario eliminado"})
    except Exception as a:
        db.rollback()
        return JSONResponse(status_code=500,content={"mensaje":"Error al eliminar usuario", "Excepcion":str(a)})
    finally:
        db.close()


@app.post('/auth/', tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.correo =='ivan@example.com' and autorizado.password == '12345678':
        token:str = create_token(autorizado.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return{"Aviso":"Usuario no autorizado"}
