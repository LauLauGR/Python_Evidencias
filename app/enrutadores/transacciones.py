from fastapi import APIRouter, HTTPException, status
from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..modelos.facturas import Factura
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_transacciones = APIRouter()


# ENDPOINTS DE TRANSACCIONES

# Listar todas las transacciones
@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones(sesion: Sesion_dependencia):
    # select * from transaccion
    consulta = select(Transaccion)
    lista_transacciones = sesion.exec(consulta).all()
    return lista_transacciones


# Listar una sola transaccion
@rutas_transacciones.get("/transacciones/{transaccion_id}", response_model=Transaccion)
async def listar_transaccion(transaccion_id: int, sesion: Sesion_dependencia):
    transaccion_encontrada = sesion.get(Transaccion, transaccion_id)

    if not transaccion_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La transacción con id {transaccion_id}, no existe."
        )

    return transaccion_encontrada


# Crear transacción
@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear, sesion: Sesion_dependencia):
    # buscar factura
    factura_encontrada = sesion.get(Factura, factura_id)

    # mensaje si no existe la factura
    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )

    # Validar datos de la transaccion
    transaccion_dict = datos_transaccion.model_dump()
    transaccion_dict["factura_id"] = factura_id
    transaccion_val = Transaccion.model_validate(transaccion_dict)

    # guardar en bd
    sesion.add(transaccion_val)
    sesion.commit()
    sesion.refresh(transaccion_val)

    return transaccion_val


# Editar transacción
@rutas_transacciones.patch("/transacciones/{transaccion_id}", response_model=Transaccion)
async def editar_transaccion(transaccion_id: int, datos_transaccion: TransaccionEditar, sesion: Sesion_dependencia):
    pass


# Eliminar transacción
@rutas_transacciones.delete("/transacciones/{transaccion_id}", response_model=Transaccion)
async def eliminar_transaccion(transaccion_id: int, sesion: Sesion_dependencia):
    # buscar transacción
    transaccion_encontrada = sesion.get(Transaccion, transaccion_id)

    # mensaje si no existe la transacción
    if not transaccion_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La transacción con id {transaccion_id}, no existe."
        )

    # eliminar de la bd
    sesion.delete(transaccion_encontrada)
    sesion.commit()

    return transaccion_encontrada