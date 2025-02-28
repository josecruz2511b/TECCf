import jwt
def create_token(datos:dict):
    token:str = jwt.encode(payload=datos,key='secretkey',algorithm='HS256')
    return token