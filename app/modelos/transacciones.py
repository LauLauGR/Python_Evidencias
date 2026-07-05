from sqlmodel import SQLModel, Field

# Modelo de transacciones
class TransaccionBase(SQLModel):
    cantidad: int = Field(default=0)
    valor_unitario: float = Field(default=0)


class TransaccionCrear(TransaccionBase):
    pass


class TransaccionEditar(TransaccionBase):
    pass


class Transaccion(TransaccionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura_id: int |None = Field(default=None, foreign_key="factura.id")