from pydantic import BaseModel
from datetime import date
from .clientes import Cliente

class Factura(BaseModel):
    id: int
    fecha: date
    valor_total: float
    cliente_id: int