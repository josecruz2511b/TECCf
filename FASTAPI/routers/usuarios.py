from fastapi import  HTTPException, Depends
from fastapi.responses import JSONResponse 
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modelUsuario
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()

# endpoint Consultar todos 
@routerUsuario.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    db= Session()
    try:
        consulta= db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500,content={"mensaje":"No fue posible consultar", "Excepcion":str(x)})

    finally:
        db.close()

@routerUsuario.get('/usuarios/{id}', tags=['Operaciones CRUD'])
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
@routerUsuario.post('/usuarios/', response_model= modelUsuario,tags=['Operaciones CRUD'])
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

@routerUsuario.put('/usuarios/{id}',tags=['Operaciones CRUD'])
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
@routerUsuario.delete('/usuarios/{id}',tags=["Operaciones CRUD"])
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