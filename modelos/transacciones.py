from pydantic import BaseModel


class Facturas(BaseModel):
    id: int
    fecha: str
    valor_total: float
    factura_id: int