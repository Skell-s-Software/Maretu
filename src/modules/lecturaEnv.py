# Importacion de Librerias necesarias
import os
from dotenv import load_dotenv

# Hay que actualizar esta lista en caso de que aumenten las variables
CONSTANTES: list = [
    "USUARIODB",
    "PWUSUARIODB",
    "URL",
    "PUERTO",
    "BASE"
]

def obtenerEnv() -> dict:
    """
    Esta funcion devuelve un diccionario con todas las constantes
    """
    load_dotenv()
    constantes: dict = {}
    for clave in CONSTANTES:
        valor: str = os.getenv(clave)
        constantes[clave] = valor
    return constantes

def main() -> None:
    """
    Funcion Principal de ejecucion en caso de ejecucion directa.
    """
    print("Accediendo a Variables de entorno de trabajo...")
    print(obtenerEnv())

if __name__ == "__main__":
    main()