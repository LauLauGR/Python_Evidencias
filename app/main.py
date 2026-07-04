from fastapi import FastAPI, HTTPException, status
from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar
from app.modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar 

app = FastAPI()

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []


# ENDPOINTS DE CLIENTES

# Listar todos los clientes
@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes

# Listar un solo cliente
@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe"
    )

# Crear cliente
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    id_cliente = len(lista_clientes) + 1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

# Editar cliente
@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            # Validar datos cliente
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes[i] = cliente_val
            return cliente_val
    raise HTTPException(
        status_code=400, detail=f"Cliente con id {cliente_id} no existe."
    )

# Eliminar cliente
@app.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"Cliente con id {cliente_id} no existe."
    )


# ENDPOINTS DE FACTURAS

# Listar todas las facturas
@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas

# Listar una sola factura
@app.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail=f"La factura con id {factura_id}, no existe"
    )

# Crear facturas
@app.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear):
    # buscar cliente
    cliente_encontrado = None
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente

    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El cliente con id {cliente_id}, no existe."
        )
    
    # Validar datos de la factura
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado
    factura_val.id = len(lista_facturas)+1
    lista_facturas.append(factura_val)
    return factura_val

# Editar factura
@app.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: FacturaEditar):
    pass

# Eliminar factura
@app.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):
    pass


# ENDPOINTS DE TRANSACCIONES

# Listar todas las transacciones
@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones

# Listar una sola transaccion
@app.get("/transacciones/{transaccion_id}", response_model=Transaccion)
async def listar_transaccion(transaccion_id: int):
    pass
    

# Crear transacción
@app.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear):
    # buscar factura
    factura_encontrada = None
    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura
            #mensaje si no existe la factura

    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"La factura con id {factura_id}, no existe."
        )
    
    # Validar datos de la transaccion
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.factura_id = factura_id
    factura_encontrada.transacciones.append(transaccion_val)

    transaccion_val.id = len(lista_transacciones)+1
    return transaccion_val

# Editar transacción
@app.patch("/transacciones/{transaccion_id}", response_model=Transaccion)
async def editar_transaccion(transaccion_id: int, datos_transaccion: TransaccionEditar):
    pass

# Eliminar transacción
@app.delete("/transacciones/{transaccion_id}", response_model=Transaccion)
async def eliminar_transaccion(transaccion_id: int):
    pass