from fastapi import APIRouter, HTTPException, status
from ..modelos.clientes import Cliente
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar
from ..listas import lista_clientes, lista_facturas

rutas_facturas = APIRouter()


# ENDPOINTS DE FACTURAS

# Listar todas las facturas
@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas

# Listar una sola factura
@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail=f"La factura con id {factura_id}, no existe"
    )

# Crear facturas
@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
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
@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: FacturaEditar):
    pass

# Eliminar factura
@rutas_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):
    pass