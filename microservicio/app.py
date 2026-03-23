# Importamos las librerías necesarias de Flask
from flask import Flask, jsonify, request

# Creamos la instancia principal de la aplicación Flask
app = Flask(__name__)

# Ruta raíz del API: sirve como punto de bienvenida o prueba de conexión
@app.route('/')
def home():
    # Retorna un mensaje en formato JSON
    return jsonify({"mensaje": "Bienvenido al API de MCIB-B"})

# Endpoint para sumar dos números
# Se accede mediante POST enviando un JSON con los parámetros "a" y "b"
@app.route('/api/sumar', methods=['POST'])
def sumar():
    # Obtenemos el cuerpo de la petición en formato JSON
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    # Validamos que los parámetros existan
    if a is None or b is None:
        return jsonify({"error": "Los parámetros a y b deben existir."}), 400

    # Validamos que los parámetros sean enteros
    if type(a) != int or type(b) != int:
        return jsonify({"error": "Los parámetros a y b deben ser enteros."}), 400

    # Retornamos el resultado de la suma en formato JSON
    return jsonify({"resultado": a + b})

# Endpoint informativo del API
# Se accede mediante GET y devuelve datos estáticos
@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({
        "nombre": "Luis Fernando",  # Autor o responsable del API
        "version": "1.0.0"          # Versión actual del servicio
    })

'''
Punto de entrada principal de la aplicación. Esta condición asegura que el servidor solo se ejecute si 
el archivo se corre directamente (python app.py) y no cuando se importa como módulo.
'''
if __name__ == '__main__':
    # Ejecutamos el servidor Flask en modo debug
    app.run(debug=True, host='0.0.0.0', port=8080)
