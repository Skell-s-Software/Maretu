# Importaciones
import os
from flask import Flask, jsonify, request
from modules.maretudb import MaretuDB, MaretuSQL
from dotenv import load_dotenv as LoadEnv
from rich import print

# Servidor
maretuServer = Flask("Maretu's BackEnd")

# Consultor
LoadEnv()
credenciales: dict = {
        "user": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PASSWORD"),
        "host": os.environ.get("DB_HOST"),
        "database": os.environ.get("DB_DATABASE")
    }
maretuDB: MaretuDB = MaretuDB(credenciales)

# Lector de Consultas Predefinidas
maretuSQL: MaretuSQL = MaretuSQL("querys/")

# Consultas de Prueba
@maretuServer.route('/test', methods=['POST'])
def test():
    try:
        credenciales = request.get_json()
    except Exception as e:
        print(e)
        return jsonify(
            {
                "success": False,
                "message": "Formato de solicitud no valido (esperado: JSON)"
            }), 400

    # Mapeo de datos
    username: str = credenciales.get('username')
    email: str = credenciales.get('email')

    # Validacion de que no esten vacios
    if not username or not email:
        return jsonify(
            {
                "success": False,
                "message": "Faltan credenciales de usuario o contraseña"
            }), 400
    
    # Consultar Base de Datos
    diccionario: dict = {
        "<nombre>": username,
        "<email>": email
    }
    maretuDB.Cursor.execute(
        maretuSQL.RemplazarArgumentos(
            maretuSQL.ConsultaSQL("DEBUG-LOGIN.sql"),
            diccionario
        )
    )
    datos: list[dict[str]] = maretuDB.Cursor.fetchall()
    print(datos)
    if datos == []: return jsonify({"success": False, "message": "Credenciales incorrectas"}), 401

    # Respuesta
    return jsonify({
        "success": True,
        "status": 200,
        "message": "Ingreso Exitoso"
    }), 200

# Asegurar Conexion
@maretuServer.route('/', methods=['GET'])
def home():
    return jsonify(
        {
            "status": "OK",
            "message": "Maretu's BackEnd Running!"
        })

if __name__ == '__main__':
    maretuServer.run(debug=True, host="0.0.0.0", port=5000)