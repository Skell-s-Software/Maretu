# Importaciones necesarias para el modulo
from encontrarRutas import crearRutaArchivo, crearRutaCarpeta
from pathlib import Path

def crearCarpeta(destino: Path) -> bool:
    """
    Esta funcion se encarga de crear la carpeta indicada
    """
    try: # Intentara crearla, en caso de que ya exista no hace nada
        destino.mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return False

def crearArchivo(nombre: str, ruta: Path) -> None:
    """
    Esta funcion se encarga de crear el archivo indicado
    """
    # Primero verifica que la carpeta exista, independientemente creara la carpeta si no existe
    crearCarpeta(ruta)
    try:
        with open(ruta / nombre, "w") as archivo: archivo.write("")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def main() -> None:
    """
    Funcion Principal de ejecucion en caso de ejecucion directa.
    """
    archivo: str = input("Crear archivo: ") # Solicita para pruebas el nombre de algun archivo
    crearArchivo(archivo, crearRutaCarpeta("Maretu"))

if __name__ == "__main__":
    main()