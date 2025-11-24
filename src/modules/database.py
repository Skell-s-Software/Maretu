# Importaciones necesarias
from rich import print
from .lecturaEnv import obtenerEnv
import mariadb

# Creacion de clase para manejar la base de datos
class MaretuDataBase():
    """
    Esta clase tiene todos los metodos necesarios para operar a la base de datos
    """
    # Conexion a la base de Datos
    def CrearConexion(instancia, credenciales: dict) -> object:
        """
        Esta funcion retorna el conector y el cursor
        """
        # Manejamos el cursor y el conector por separado por manejo de errores eficaz
        try:
            conexion = mariadb.connect(
                user = credenciales["USUARIODB"],
                password = credenciales["PWUSUARIODB"],
                host = credenciales["URL"],
                port = int(credenciales["PUERTO"]),
                database = credenciales["BASE"]
            )
            cursor = conexion.cursor()
            return conexion, cursor
        except Exception as e:
            print(f"Ocurrio un error al conectarse a la base de datos:\n{e}")
            # Devolver (None, None) para evitar unpacking error en el __init__
            return None, None
    
    # Visualizar objetos en la memoria
    def visualizar(instancia) -> None:
        print(instancia.Conexion)
        print(instancia.Cursor)

    # FUNCION PARA CONSULTAS
    def Query(instancia: object, consulta: str) -> list[tuple]:
        """
        Esta funcion simplemente ejecuta consultas plantilla con parametros dados
        """
        try:
            if instancia.Cursor is None:
                raise ConnectionError("No hay conexión a la base de datos configurada.")
            instancia.Cursor.execute(consulta)
            return instancia.Cursor.fetchall()
        except Exception as e:
            print(f"Ocurrio un error:\n{e}")
            return []

    # Constructor
    def __init__(instancia: object, constantes: dict) -> None:
        """
        Funcion de creacion de la instancia, utiliza el .env para crear la conexion
        """
        # Se crea el cursor y la conexion
        instancia.Conexion, instancia.Cursor = instancia.CrearConexion(constantes)
        if instancia.Conexion is None or instancia.Cursor is None:
            raise ConnectionError("No se pudo establecer la conexión a la base de datos. Verifica las credenciales en el archivo .env.")

def main() -> None:
    """
    Funcion Principal para pruebas
    """
    db: MaretuDataBase = MaretuDataBase(obtenerEnv())
    db.visualizar()
    print()
    print( db.Query( input(" -> Consulta: ") ) )

if __name__ == "__main__":
    main()