## Descripción del proyecto - FASTAPI

- **Clientes**: información básica de cada cliente (nombre, email, descripción).
- **Facturas**: pertenecen a un cliente y contienen una lista de transacciones. El valor total se calcula automáticamente sumando `cantidad * valor_unitario` de cada transacción asociada.
- **Transacciones**: pertenecen a una factura, con cantidad y valor unitario.

## Estructura del proyecto

```
app/
├── main.py
├── listas.py
├── conexion_bd.py
├── __init__.py
├── modelos/
│   ├── clientes.py            # Modelos Pydantic de Cliente
│   ├── facturas.py            # Modelos Pydantic de Factura
│   ├── transacciones.py       # Modelos Pydantic de Transaccion
│   └── __init__.py
└── enrutadores/
    ├── clientes.py             # Endpoints CRUD de clientes
    ├── facturas.py             # Endpoints CRUD de facturas
    ├── transacciones.py        # Endpoints CRUD de transacciones
    └── __init__.py
.gitignore
README.md
bd_clientes.sqlite3
requirements.txt
```

## Endpoints disponibles

### Clientes
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/clientes` | Listar todos los clientes |
| GET | `/clientes/{cliente_id}` | Listar un cliente por id |
| POST | `/clientes` | Crear un cliente |
| PATCH | `/clientes/{cliente_id}` | Editar un cliente |
| DELETE | `/clientes/{cliente_id}` | Eliminar un cliente |

### Facturas
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/facturas` | Listar todas las facturas |
| GET | `/facturas/{factura_id}` | Listar una factura por id |
| POST | `/facturas/{cliente_id}` | Crear una factura asociada a un cliente |
| PATCH | `/facturas/{factura_id}` | Editar una factura |
| DELETE | `/facturas/{factura_id}` | Eliminar una factura |

### Transacciones
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/transacciones` | Listar todas las transacciones |
| GET | `/transacciones/{transaccion_id}` | Listar una transacción por id |
| POST | `/transacciones/{factura_id}` | Crear una transacción asociada a una factura |
| PATCH | `/transacciones/{transaccion_id}` | Editar una transacción |
| DELETE | `/transacciones/{transaccion_id}` | Eliminar una transacción |


## Proceso de desarrollo (historial de commits)

El proyecto se desarrolló de forma incremental, empezando sin estructura (todo en un solo `main.py`) y evolucionando hacia una estructura organizada por carpetas (`modelos` y `enrutadores`). El historial de commits refleja este proceso.

## Autor

Laurith Gil - 3407187.