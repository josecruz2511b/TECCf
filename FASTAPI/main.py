from fastapi import FastAPI, HTTPException
from DB.conexion import  engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

from fastapi.middleware.cors import CORSMiddleware

#declaramos un objeto 
app = FastAPI(
    title='Mi primer API 196', 
    description='Jose GUadalupe De la Cruz',
    version='1.0.1'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#levanta las tablas definidas en modelos
Base.metadata.create_all(bind=engine)

app.include_router(routerUsuario)
app.include_router(routerAuth)


#generamos nuestro primer endpoint 
# endpoint tipo get 
@app.get('/', tags=['Inicio'])
def main():
    return {'hello FastAPI':'Jose Guadalupe'}





