from fastapi import APIRouter, HTTPException, status
from ..modelos.clientes import Cliente
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_facturas = APIRouter()


# ENDPOINTS DE FACTURAS

# Listar todas las facturas
@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas(sesion: Sesion_dependencia):
    # select * from factura
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas


# Listar una sola factura
@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int, sesion: Sesion_dependencia):
    factura_encontrada = sesion.get(Factura, factura_id)

    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe"
        )

    return factura_encontrada


# Crear facturas
@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion: Sesion_dependencia):
    # buscar cliente
    cliente_encontrado = sesion.get(Cliente, cliente_id)

    # mensaje si no existe el cliente
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe."
        )

    # Validar datos de la factura -json, pasar dict
    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id

    factura_val = Factura.model_validate(factura_dict)

    # guardar en bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)

    return factura_val


# Editar factura
@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: FacturaEditar, sesion: Sesion_dependencia):
    pass


# Eliminar factura
@rutas_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int, sesion: Sesion_dependencia):
    # buscar factura
    factura_encontrada = sesion.get(Factura, factura_id)

    # mensaje si no existe la factura
    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )

    # eliminar de la bd
    sesion.delete(factura_encontrada)
    sesion.commit()

    return factura_encontrada