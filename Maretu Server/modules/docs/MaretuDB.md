# Módulo: MaretuDB

![Static Badge](https://badgers.space/badge/python/+3.14/blue)
![Static Badge](https://badgers.space/badge/database/MariaDB/green)

Módulo diseñado únicamente para la ejecución de consultas SQL a la base de datos correspondiente mediante una clase en python.

```mermaid
classDiagram
direction TB
    class MaretuDB {
      self.Credenciales: dict
      self.Conexion: MariaDB.Connection
      self.Cursor: self.Conexion.Cursor
      ConsultaPersonalizada(Query: str) list[dict]
      AutenticarUsuario(Credenciales: dict) bool
      ConsultarUsuarios() list[dict]
      ConsultarUsuario(user: str) list[dict]
    }
```

> La clase es propensa a actualizarse con más funciones.

Esta clase permite obtener de forma directa consultas SQL específicas a la base de datos, se implementó el uso de POO para facilitar su manejo en el hilo principal de ejecución.

Por defecto, en el código mismo se debe proporcionar las credenciales para el acceso a la base de datos. Otra opción es usar .env pero esto afectará al momento de compilar la aplicación para producción.

## Secuencia de Ejecución

```mermaid
sequenceDiagram
    MaretuDB-->>+MariaDB: (Abrir Conexion)
    MaretuDB->>+MariaDB: Cursor(Query)
    MariaDB->>+MaretuDB: Data Response
    MaretuDB-->>+MariaDB: (Cerrar Conexion)
```
