
from fastapi import FastAPI
#declaramos un objeto 
app = FastAPI()
        
#generamos nuestro primer endpoint 
# endpoint tipo get 
@app.get('/')
def main():
    return {'hello FastAPI':'Jose Guadalupe'}
    