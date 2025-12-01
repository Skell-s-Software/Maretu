# Importaciones
import os
import mariadb
from dotenv import load_dotenv as LoadEnv
from rich import print

class MaretuSQL:
    # Remplazar Argumentos
    def RemplazarArgumentos(instancia, texto:str, diccionario: dict) -> str:
        nuevoTexto: str = texto
        for llave in diccionario:
            nuevoTexto = nuevoTexto.replace(llave, diccionario[llave])
        return nuevoTexto

    # Consultar Archivos SQL y retornar texto str
    def ConsultaSQL(instancia, nombreArchivo: str) -> str:
        try:
            with open(instancia.RutaCarpeta + nombreArchivo, 'rb') as archivo:
                archivoBytes = archivo.read()
            return archivoBytes.decode('utf-8')
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: El archivo no fue encontrado en la ruta: {nombreArchivo}")
        except IOError as e:
            raise IOError(f"Error de E/S al leer el archivo '{nombreArchivo}': {e}")
        except UnicodeDecodeError:
            return archivoBytes.decode('latin-1', errors='ignore')
        except Exception as e:
            raise Exception(f"Ocurrió un error inesperado al procesar el archivo '{nombreArchivo}': {e}")

    # Constructor
    def __init__(instancia, rutaCarpeta):
        instancia.RutaCarpeta: str = rutaCarpeta

class MaretuDB:
    # Crear Conector de forma Manual
    def CrearConexion(instancia: object, credenciales: dict) -> mariadb.connect:
        try:
            conexion: mariadb.connect = mariadb.connect(**credenciales)
        except Exception as e:
            raise f"Error al crear Conexion: {e}"
        return conexion

    # Crear Cursor de forma Manual
    def CrearCursor(instancia: object, conexion: mariadb.connect) -> mariadb.Cursor:
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
    lector: MaretuSQL = MaretuSQL("querys/")
    diccionario: dict = {
        "<nombre>": "Robert Rodriguez",
        "<email>": "skellent69@gmail.com"
    }
    print(f"Consulta: {lector.RemplazarArgumentos(lector.ConsultaSQL("DEBUG-LOGIN.sql"), diccionario)}")
    consultor.Cursor.execute(lector.RemplazarArgumentos(lector.ConsultaSQL("DEBUG-LOGIN.sql"), diccionario))
    print(consultor.Cursor.fetchall())

