from pydantic import BaseModel
from .clientes import Cliente


class Factura(BaseModel):
    id: int
    fecha: str
    valor_total: float
    cliente: Cliente