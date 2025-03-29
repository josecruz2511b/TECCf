from fastapi.responses import JSONResponse 
from modelsPydantic import modelAuth
from tokenGen import create_token
from fastapi import APIRouter

routerAuth = APIRouter()

@routerAuth.post('/auth/', tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.correo =='ivan@example.com' and autorizado.password == '12345678':
        token:str = create_token(autorizado.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return{"Aviso":"Usuario no autorizado"}