from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    email: str
    descripcion: str | None = None

class ClienteCrear(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int | None = None