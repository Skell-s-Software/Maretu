# Importaciones
from flask import Flask, jsonify

# Servidor
Maretu = Flask("Maretu's BackEnd")

@Maretu.route('/', methods=['GET'])
def home():
    return jsonify(
        {
            "status": "OK",
            "message": "Maretu's BackEnd Running!"
        })

if __name__ == '__main__':
    Maretu.run(debug=True, host="0.0.0.0", port=5000)