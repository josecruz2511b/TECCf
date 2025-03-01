import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

def create_token(datos:dict):
    token:str = jwt.encode(payload=datos,key='secretkey',algorithm='HS256')
    return token

def validate_token(token:str):
    try:
        #decodificamos el token, 
        #decode valida y verifica el token
        data:dict = jwt.decode(token, key='secretkey', algorithms=['HS256'])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="El token expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token no autorizado")