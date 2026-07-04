from fastapi import FastAPI, HTTPException, status
from .enrutadores.facturas import rutas_facturas 
from .enrutadores.clientes import rutas_clientes
from .enrutadores.transacciones import rutas_transacciones

app = FastAPI()

# Incluir ruta de clientes
app.include_router(rutas_clientes, tags=["Clientes"])
app.include_router(rutas_facturas, tags=["Facturas"])
app.include_router(rutas_transacciones, tags=["Transacciones"])