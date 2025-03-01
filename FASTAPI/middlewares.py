from fastapi import  HTTPException, Request
from fastapi.security import HTTPBearer
from tokenGen import validate_token

class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data= validate_token(auth.credentials)
        if not isinstance(data, dict):
            raise HTTPException(status_code=403, detail="Formato de Token no valido")
        if data.get('correo')!= 'ivan@example.com':
            raise HTTPException(status_code=403, detail="Credenciales No validas")