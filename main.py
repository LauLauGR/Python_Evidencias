from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear
from modelos.facturas import Factura

app = FastAPI()

lista_clientes = []
lista_facturas = []


@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}


@app.get("/clientes/{id}")
async def listar_cliente(id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            return obj_cliente
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {id}, no se encuentra. "
    )


@app.post("/clientes", response_model=Cliente)  # respuest todos los datos del cliente
def crear_clientes(datos_cliente: ClienteCrear):  # creacion sin el id.
    # validar datos_cliente, pasar json a dicccionario
    cliente_dict = Cliente.model_validate(datos_cliente.model_dump())
    # genere un id segun la lista_clientes
    id_cliente = len(lista_clientes) + 1
    cliente_dict.id = id_cliente
    # agregar a la lista
    lista_clientes.append(cliente_dict)
    # return {"Mensaj": "Cliente creado", "Cliente": datos_cliente}
    return cliente_dict


@app.patch("/clientes/{id}")
async def editar_cliente(id: int, datos_cliente: Cliente):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = id
            lista_clientes[i] = cliente_val

    return {
        "mensaje": "Se actualizo el cliente satisfactoriamente.",
        "Cliente": cliente_val,
    }


# endpoint
@app.delete("/clientes/{id}")
def eliminar_clientes(cliente_id):
    lista_clientes.pop(cliente_id)
    return {"mensaje": "Cliente eliminado"}


# endpoint de listar facturas
@app.get("/facturas")
def listar_facturas():
    return lista_facturas


# endopoint de crear facturas
@app.post("/facturas")
def crear_facturas(datos_factura: Factura):
    lista_facturas.append(datos_factura)
    return {"Factura": datos_factura}