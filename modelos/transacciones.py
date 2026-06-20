from pydantic import BaseModel

# Modelo de transacciones
class TransaccionBase(BaseModel):
    cantidad: int
    valor_unitario: float
    factura_id: int

class TransaccionCrear(TransaccionBase):
    pass

class TransaccionEditar(TransaccionBase):
    pass

class Transaccion(TransaccionBase):
    id: int | None = None #relación con el modelo