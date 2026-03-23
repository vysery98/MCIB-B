from flask import Flask, jsonify, request

app = Flask(__name__)

# https://API.com/

@app.route('/')
def home():
    return jsonify({"mensaje": "Bienvenido al API de MCIB-B"})

@app.route('/api/sumar', methods = ['POST'])
def sumar():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Los parámetros a y b deben existir."}), 400

    if type(a) != int or type(b) != int:
        return jsonify({"error": "Los parámetros a y b deben ser enteros."}), 400

    return jsonify({"resultado": a + b})

@app.route('/api/info', methods = ['GET'])
def info():
    return jsonify({
        "nombre": "Carlos Vintimilla",
        "version": "1.0.0"    
    })

if __name__ == '__main__': # Esta línea ejecuta la app cuando yo en el terminal haga python app.py
    app.run(debug = True, host = '0.0.0.0', port = 8080)
        