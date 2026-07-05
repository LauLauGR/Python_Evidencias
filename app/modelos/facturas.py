from pydantic import computed_field
from sqlmodel import SQLModel, Field
from .transacciones import Transaccion
from datetime import datetime

# Modelo de facturas
class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)

    @computed_field
    @property
    def valor_total(self) -> float:
        # Calcula (cantidad * valor_unitario)
        # Consultar el id actual de factura
        factura_id_actual = getattr(self, "id", None)
        total_factura = 0.0

        # recorrer la lista de transacciones, según el factura_id
        if not factura_id_actual:
            return total_factura

        # Verificar si existe el atributo transacciones
        if hasattr(self, "transacciones"):
            for transaccion in self.transacciones:
                if transaccion.factura_id == factura_id_actual:
                    total_factura += (
                        transaccion.valor_unitario * transaccion.cantidad
                    )

        return total_factura


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id")