from pydantic import BaseModel, computed_field
from .transacciones import Transaccion
from .clientes import Cliente
from datetime import datetime

# Modelo de facturas
class FacturaBase(BaseModel):
    fecha: str = datetime.now()
    cliente: Cliente
    transacciones: list[Transaccion]

    @computed_field
    @property
    def valor_total(self) -> float:
        return 0

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None