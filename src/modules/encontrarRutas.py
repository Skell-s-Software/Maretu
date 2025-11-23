# Importaciones de Librerias
from pathlib import Path
from platformdirs import user_documents_dir as userDocumentsDir

def crearRutaArchivo(rutaOriginal: Path, archivo: str) -> Path:
    """
    Esta funcion retorna la ruta junto con el archivo
    """
    return rutaOriginal / archivo

def crearRutaCarpeta(carpeta: str) -> Path:
    """
   Esta funcion esta dedicada a crear rutas a carpetas propias en Documents del usuario. 
    """
    return Path(userDocumentsDir()) / carpeta

def main() -> None:
    """
    Funcion Principal de ejecucion en caso de ejecucion directa.
    """
    print(f"La ruta de Documentos del Usuario y del Sistema es:\n -> {Path(userDocumentsDir())}")
    print(f"La ruta de la carpeta del Sistema es:\n -> {crearRutaCarpeta("Maretu")}")
    print(f"La ruta del archivo configuracion.config:\n -> {crearRutaArchivo(crearRutaCarpeta("Maretu"), "configuracion.config")}")

if __name__ == "__main__":
    main()