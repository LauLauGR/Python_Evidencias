# CRUD con FastAPI

## Descripción del proyecto

Este proyecto consiste en una API REST desarrollada con **FastAPI** para gestionar clientes, facturas y transacciones. La información se almacena de forma persistente en una base de datos **SQLite** utilizando **SQLModel**.

La aplicación implementa operaciones CRUD (Crear, Consultar, Actualizar y Eliminar) para cada una de las entidades, manteniendo la relación entre ellas.

- **Clientes**: información básica de cada cliente (nombre, email y descripción).
- **Facturas**: pertenecen a un cliente y contienen una lista de transacciones. El valor total de cada factura se calcula automáticamente a partir de las transacciones registradas.
- **Transacciones**: pertenecen a una factura e incluyen la cantidad y el valor unitario de cada producto o servicio.

---

## Base de datos

El proyecto utiliza una base de datos **SQLite** llamada:

```
bd_clientes.sqlite3
```

La conexión se administra desde el archivo:

```
app/conexion_bd.py
```

Este archivo se encarga de:

- Configurar el motor de conexión con SQLite mediante **SQLModel**.
- Crear automáticamente las tablas de la base de datos cuando inicia la aplicación.
- Administrar las sesiones de conexión utilizando inyección de dependencias de FastAPI.
- Proporcionar una única sesión por petición para realizar operaciones sobre la base de datos.

---

## Estructura del proyecto

```text
app/
├── main.py
├── listas.py
├── conexion_bd.py            # Configuración de la base de datos y sesiones
├── __init__.py
├── modelos/
│   ├── clientes.py           # Modelos de Cliente
│   ├── facturas.py           # Modelos de Factura
│   ├── transacciones.py      # Modelos de Transacción
│   └── __init__.py
└── enrutadores/
    ├── clientes.py           # Endpoints CRUD de clientes
    ├── facturas.py           # Endpoints CRUD de facturas
    ├── transacciones.py      # Endpoints CRUD de transacciones
    └── __init__.py

.gitignore
README.md
bd_clientes.sqlite3
requirements.txt
```

---

## Endpoints disponibles

### Clientes

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/clientes` | Listar todos los clientes |
| GET | `/clientes/{cliente_id}` | Obtener un cliente por ID |
| POST | `/clientes` | Crear un cliente |
| PATCH | `/clientes/{cliente_id}` | Editar un cliente |
| DELETE | `/clientes/{cliente_id}` | Eliminar un cliente |

### Facturas

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/facturas` | Listar todas las facturas |
| GET | `/facturas/{factura_id}` | Obtener una factura por ID |
| POST | `/facturas/{cliente_id}` | Crear una factura asociada a un cliente |
| PATCH | `/facturas/{factura_id}` | Editar una factura |
| DELETE | `/facturas/{factura_id}` | Eliminar una factura |

### Transacciones

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/transacciones` | Listar todas las transacciones |
| GET | `/transacciones/{transaccion_id}` | Obtener una transacción por ID |
| POST | `/transacciones/{factura_id}` | Crear una transacción asociada a una factura |
| PATCH | `/transacciones/{transaccion_id}` | Editar una transacción |
| DELETE | `/transacciones/{transaccion_id}` | Eliminar una transacción |

---

## Proceso de desarrollo

El proyecto fue desarrollado de manera incremental. Inicialmente toda la lógica se encontraba en un único archivo `main.py` utilizando listas en memoria. Posteriormente se reorganizó mediante las carpetas `modelos` y `enrutadores`, y finalmente se incorporó una base de datos SQLite utilizando SQLModel para lograr persistencia de la información y una mejor organización del acceso a los datos.

---

## Autor

**Laurith Gil**  
Ficha: **3407187**