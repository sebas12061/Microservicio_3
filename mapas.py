from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Lugares visibles en el mapa (solo aprobados)
lugares = []
contador_id = 1

# URL del microservicio de solicitudes
URL_SOLICITUDES = "http://127.0.0.1:5007"

# Ver lugares aprobados en el mapa
@app.route("/mapa", methods=["GET"])
def ver_mapa():
    return jsonify(lugares), 200

# Filtrar lugares
@app.route("/mapa/filtrar", methods=["GET"])
def filtrar_mapa():
    categoria = request.args.get("categoria")
    if categoria:
        filtrados = [l for l in lugares if l["categoria"] == categoria]
        return jsonify(filtrados), 200
    return jsonify(lugares), 200

# Proponer un lugar (se envía a solicitudes.py)
@app.route("/mapa/proponer", methods=["POST"])
def proponer_lugar():
    data = request.get_json()
    try:
        resp = requests.post(f"{URL_SOLICITUDES}/solicitudes", json=data)
        if resp.status_code == 201:
            return jsonify({"mensaje": "Solicitud enviada a revisión"}), 201
        else:
            return jsonify({"error": "No se pudo enviar la solicitud"}), 500
    except:
        return jsonify({"error": "No se pudo conectar al microservicio de solicitudes"}), 500

# Agregar lugar al mapa (llamado desde solicitudes cuando se aprueba)
@app.route("/mapa/agregar", methods=["POST"])
def agregar_lugar():
    global contador_id
    data = request.get_json()
    nuevo_lugar = {
        "id": contador_id,
        "nombre": data.get("nombre"),
        "categoria": data.get("categoria"),
        "ubicacion": data.get("ubicacion"),
        "popularidad": 0
    }
    lugares.append(nuevo_lugar)
    contador_id += 1
    return jsonify({"mensaje": "Lugar agregado al mapa"}), 201

if __name__ == "__main__":
    app.run(port=5006, debug=True)
