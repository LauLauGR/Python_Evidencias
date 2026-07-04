from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relashionship
from .transacciones import Transaccion
from .clientes import Cliente
from datetime import datetime

# Modelo de facturas
class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now())
   # cliente: Cliente
    #transacciones: list[Transaccion]

    @computed_field
    @property
    def valor_total(self) -> float:
        # Calculae (cantidad *  valor_unitario)
        # Consultar el id actual de factura
        factura_id_actual = getattr(self, "id", None)
        total_factura = 0.0
        if not factura_id_actual or not self.transacciones:
            return total_factura
        #  recorrer la lista de transacciones, segun el factura_id
        for transaccion in self.transacciones:
            if transaccion.factura_id == factura_id_actual:
                total_factura +=transaccion.valor_unitario * transaccion.cantidad

        return 0.0

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)