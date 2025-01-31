
from fastapi import FastAPI
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

@app.get('/promedio', tags=['Mi Calificacion TAI'])
def promedio():
    return 5*2

#endPOINT Parametro Obligatorio
@app.get('/usuario/{id}', tags=['Parametro Obligatorio'])
def consultaUsuario(id:int):
    #ConectamosBD
    #hacemos consulta retornarmos resultset
    return{"Se encontro el usuario": id}
    
#Parametro opcional se dejara solo con la diagonal
# para que no se necesario que espere 
#declarar el nombre de la funcion pero que no lleve el mismo que el anterior
#definiremos el typiado el cual sera opcional para que no sea obligatorio
@app.get('/usuariox/', tags=['Parametro Opcional'])
def consultaUsuario2(id:Optional[int]= None ):
    if id is not None: 
        for usuario in usuarios:
            if usuario["id"]== id:
                return {"mensaje":"Usuario encontrado", "usuario":usuario}
        return{"mensaje":f"No se encontro el id: {id}"}
    else: 
        return{"mensaje": "No se proporciono un Id"}

@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}