# RENTOOLS-API

Rentools es una aplicación para la gestión del alquiler de herra-
mientas, que permite la creación de productos, categorias, clien-
tes, generación de salidas y entradas de los productos alquilados.

## Caracteristicas:

- Visualización de los productos en bodega disponible y total
- Visualización de los productos alquilados y a que personas
- Visualización del registro de la salida de los productos
- Visualización del registro del ingreso de los productos
- Generación de PDF de los registros


## Serialización de datos de BD MySQL por medio de uso de API Get

### Tecnologias usadas:

- SQLAlchemy
- PyMySQL
- Flask
- Flask-restx

El objetivo de este proyecto es acceder a una base de datos remoto,
y a partir de cada una de sus tablas, crear una clase que pueda ser
leída y serializada, para una posterior adquisición de un documento
JSON, que pueda ser usado para la importación de archivo a una NOSQL
como parte de una migración de base de datos.


### Rutas:

#### Categorias
- <host>/api/cat o <host>/api/cat/

#### Productos
- <host>/api/product o <host>/api/product/

#### Clientes
- <host>/api/client o <host>/api/client/

#### Salidas
- <host>/api/outcome o <host>/api/outcome/

#### Entradas
- <host>/api/income o <host>/api/income/
