from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente

app = FastAPI()

lista_clientes = []
lista_facturas = []
lista_transacciones = []

@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}

@app.get("/clientes/{id}")
def listar_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return {"Cliente": cliente}
        
    return {"Mensaje": "Cliente no encontrado"}

@app.post("/clientes", response_model=Cliente)
def crear_cliente(datos_cliente: ClienteCrear):
    lista_clientes.append(datos_cliente)
    return datos_cliente

@app.put("/clientes/{id}")
def editar_cliente(id: int, datos_actualizados: Cliente):
    for cliente in lista_clientes:
        if cliente.id == id:
            posicion = lista_clientes.index(cliente)
            lista_clientes[posicion] = datos_actualizados
            return {"Mensaje": "Cliente actualizado exitosamente", "Cliente": datos_actualizados}

    return {"Mensaje": "Cliente no encontrado"}

@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            lista_clientes.remove(cliente)
            return {"Mensaje": "Cliente eliminado exitosamente"}
            
    return {"Mensaje": "Cliente no encontrado"}

# FACTURAS

@app.get("/facturas")
def listar_facturas():
    return {"Facturas": lista_facturas}
 
@app.get("/facturas/{id}")
def listar_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            return {"Factura": factura}
    return {"Mensaje": "Factura no encontrada"}
 
@app.post("/facturas")
def crear_factura(datos_factura: Factura):
    cliente_existe = any(c.id == datos_factura.cliente_id for c in lista_clientes)
    if not cliente_existe:
        return {"Mensaje": f"Cliente con id {datos_factura.cliente_id} no encontrado"}
 
    lista_facturas.append(datos_factura)
    return datos_factura
 
@app.put("/facturas/{id}")
def editar_factura(id: int, datos_actualizados: Factura):
    cliente_existe = any(c.id == datos_actualizados.cliente_id for c in lista_clientes)
    if not cliente_existe:
        return {"Mensaje": f"Cliente con id {datos_actualizados.cliente_id} no encontrado"}
 
    for factura in lista_facturas:
        if factura.id == id:
            lista_facturas[lista_facturas.index(factura)] = datos_actualizados
            return {"Mensaje": "Factura actualizada exitosamente", "Factura": datos_actualizados}
    return {"Mensaje": "Factura no encontrada"}
 
@app.delete("/facturas/{id}")
def eliminar_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            lista_facturas.remove(factura)
            return {"Mensaje": "Factura eliminada exitosamente"}
    return {"Mensaje": "Factura no encontrada"}
 
# TRANSACCIONES

@app.get("/transacciones")
def listar_transacciones():
    return {"Transacciones": lista_transacciones}
 
@app.get("/transacciones/{id}")
def listar_transaccion(id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            return {"Transaccion": transaccion}
    return {"Mensaje": "Transacción no encontrada"}
 
@app.post("/transacciones")
def crear_transaccion(datos_transaccion: Transaccion):
    factura_existe = any(f.id == datos_transaccion.factura_id for f in lista_facturas)
    if not factura_existe:
        return {"Mensaje": f"Factura con id {datos_transaccion.factura_id} no encontrada"}
 
    lista_transacciones.append(datos_transaccion)
    return datos_transaccion
 
@app.put("/transacciones/{id}")
def editar_transaccion(id: int, datos_actualizados: Transaccion):
    factura_existe = any(f.id == datos_actualizados.factura_id for f in lista_facturas)
    if not factura_existe:
        return {"Mensaje": f"Factura con id {datos_actualizados.factura_id} no encontrada"}
 
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            lista_transacciones[lista_transacciones.index(transaccion)] = datos_actualizados
            return {"Mensaje": "Transacción actualizada exitosamente", "Transaccion": datos_actualizados}
    return {"Mensaje": "Transacción no encontrada"}
 
@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            lista_transacciones.remove(transaccion)
            return {"Mensaje": "Transacción eliminada exitosamente"}
    return {"Mensaje": "Transacción no encontrada"}