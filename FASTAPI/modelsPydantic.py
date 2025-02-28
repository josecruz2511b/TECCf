from pydantic import BaseModel, Field, EmailStr
#modelo para validacion de datos
class modelUsuario(BaseModel):
    id : int = Field(...,gt=0,description="Id unico y solo numero")
    nombre: str = Field(...,min_length=3, max_length=15,description="Nombre debe contener solo letras y espacios")
    edad: int = Field(...,gt=0, lt=130,description="Edad debe ser mayor a 0")
    correo: str = Field(..., pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", example="usuario@example.com", description="Correo del usuario")

class modelAuth(BaseModel):
    correo:EmailStr 
    password:str = Field(...,min_length=8,strip_whitespace=True,description="Contraseña minimo 8 caracteres")