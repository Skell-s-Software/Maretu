# Importaciones
import os
import mariadb
from dotenv import load_dotenv as LoadEnv
from rich import print

class MaretuDB:
    # Crear Conector de forma Manual
    def CrearConexion(instancia: object, credenciales: dict):
        try:
            conexion: mariadb.connect = mariadb.connect(**credenciales)
        except Exception as e:
            raise f"Error al crear Conexion: {e}"
        return conexion

    # Crear Cursor de forma Manual
    def CrearCursor(instancia: object, conexion: mariadb.connect):
        try:
            cursor = conexion.cursor(dictionary=True)
        except Exception as e:
            raise f"Error al crear Cursor: {e}"
        return cursor

    # Constructor
    def __init__(instancia: object, credenciales: dict):
        instancia.Credenciales: dict = credenciales
        instancia.Conexion: mariadb.connect = instancia.CrearConexion(credenciales)
        instancia.Cursor: mariadb.Cursor = instancia.CrearCursor(instancia.Conexion)

if __name__ == "__main__":
    LoadEnv()
    credenciales: dict = {
        "user": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PASSWORD"),
        "host": os.environ.get("DB_HOST"),
        "database": os.environ.get("DB_DATABASE")
    }
    consultor: MaretuDB = MaretuDB(credenciales)
    print(consultor)
    print(consultor.Credenciales)
    print(consultor.Conexion)
    print(consultor.Cursor)
