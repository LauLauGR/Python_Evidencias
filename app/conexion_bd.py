from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine

nombre_bd = "bd_clientes.sqlite3"
url_bd = f"sqlite:///{nombre_bd}"

# Motor de base de datos
motor_bd = create_engine(url_bd)

# Definir el método para crear las tablas
def crear_tablas(app: FastAPI):
    SQLModel.metadata.create_all(motor_bd)
    yield # no hay nada para ejecutar, pausa, sigue y regresa

# definir el metodo para la sesion
def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion #retorna la sesion

# Denominado inyeccion de dependencias
# Registrar la sesion como dependencia, utilizada en los endpoints
Sesion_dependencia = Annotated[Session, Depends(obtener_sesion)]