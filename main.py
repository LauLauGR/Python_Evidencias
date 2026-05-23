from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista_clientes = []
     
class Cliente(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None

@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}

@app.get("/clientes/{id}")
def listar_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return {"Cliente": cliente}
        
    return {"Mensaje": "Cliente no encontrado"}

@app.post("/clientes", response_model=Cliente)
def crear_clientes(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return {"Mensaje": "Cliente creado exitosamente", "Cliente": datos_cliente}

@app.put("/clientes/{id}")
def editar_cliente(id: int, datos_actualizados: Cliente):
    for cliente in lista_clientes:
        if cliente.id == id:
            posicion = lista_clientes.index(cliente)
            lista_clientes[posicion] = datos_actualizados
            return {"Mensaje": "Cliente actualizado exitosamente", "Cliente": datos_actualizados}

    return {"Mensaje": "Cliente no encontrado"}

@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            lista_clientes.remove(cliente)
            return {"Mensaje": "Cliente eliminado exitosamente"}
            
    return {"Mensaje": "Cliente no encontrado"}