# Importaciones
import os
import mariadb
from dotenv import load_dotenv as LoadEnv
from rich import print

class MaretuSQL:
    def ConsultaSQL(instancia, rutaArchivo: str):
        try:
            with open(rutaArchivo, 'rb') as archivo:
                archivoBytes = archivo.read()
            return archivoBytes.decode('utf-8')
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: El archivo no fue encontrado en la ruta: {rutaArchivo}")
        except IOError as e:
            raise IOError(f"Error de E/S al leer el archivo '{rutaArchivo}': {e}")
        except UnicodeDecodeError:
            return archivoBytes.decode('latin-1', errors='ignore')
        except Exception as e:
            raise Exception(f"Ocurrió un error inesperado al procesar el archivo '{rutaArchivo}': {e}")

    # Constructor
    def __init__(instancia):
        pass

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
    print(consultor.Conexion)
    print(consultor.Cursor)
    consultor.Cursor.execute("SELECT * FROM debug")
    print(consultor.Cursor.fetchall())
    print("------- Consulta mediante MaretuSQL -------")
    lector: MaretuSQL = MaretuSQL()
    print(lector.ConsultaSQL("querys/DEBUG-LOGIN.sql"))
    consultor.Cursor.execute(lector.ConsultaSQL("querys/DEBUG-LOGIN.sql").replace("<nombre>", "Robert Rodriguez").replace("<email>", "skellent69@gmail.com"))
    print(consultor.Cursor.fetchall())

