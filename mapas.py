from flask import Flask, request, jsonify

app = Flask(__name__)

# Lugares visibles en el mapa (ya aprobados por admin)
lugares = [
    {
        "id": 1,
        "nombre": "Mirador de los Nevados",
        "categoria": "naturaleza",
        "ubicacion": "5.067,-75.517",
        "popularidad": 5
    },
    {
        "id": 2,
        "nombre": "Museo de Arte Moderno",
        "categoria": "cultura",
        "ubicacion": "4.711,-74.072",
        "popularidad": 4
    }
]

# Lista de solicitudes pendientes (simulación de integración con microservicio Solicitudes)
solicitudes_pendientes = []
contador_id = 3
contador_solicitudes = 1

# Ver lugares en el mapa
@app.route("/mapa", methods=["GET"])
def ver_mapa():
    return jsonify(lugares), 200

# 2. Filtrar lugares
@app.route("/mapa/filtrar", methods=["GET"])
def filtrar_mapa():
    categoria = request.args.get("categoria")
    filtrados = [l for l in lugares if not categoria or l["categoria"] == categoria]
    return jsonify(filtrados), 200

# 3. Proponer un nuevo lugar
@app.route("/mapa/proponer", methods=["POST"])
def proponer_lugar():
    global contador_solicitudes
    data = request.get_json()
    solicitud = {
        "id": contador_solicitudes,
        "usuario": data.get("usuario"),
        "nombre": data.get("nombre"),
        "categoria": data.get("categoria"),
        "ubicacion": data.get("ubicacion"),
        "estado": "pendiente"  # por defecto
    }
    solicitudes_pendientes.append(solicitud)
    contador_solicitudes += 1
    return jsonify({"mensaje": "Lugar propuesto. Pendiente de aprobación por admin.", "solicitud": solicitud}), 201

# 4. Ver solicitudes pendientes (para que el admin luego use Solicitudes)
@app.route("/mapa/solicitudes", methods=["GET"])
def ver_solicitudes():
    return jsonify(solicitudes_pendientes), 200

# 5. Simulación de aprobación (cuando admin aprueba en microservicio Solicitudes
@app.route("/mapa/aprobar/<int:id>", methods=["POST"])
def aprobar_lugar(id):
    global contador_id
    for solicitud in solicitudes_pendientes:
        if solicitud["id"] == id:
            nuevo_lugar = {
                "id": contador_id,
                "nombre": solicitud["nombre"],
                "categoria": solicitud["categoria"],
                "ubicacion": solicitud["ubicacion"],
                "popularidad": 0
            }
            lugares.append(nuevo_lugar)
            solicitud["estado"] = "aceptada"
            contador_id += 1
            return jsonify({"mensaje": "Lugar aprobado y agregado al mapa", "lugar": nuevo_lugar}), 200
    return jsonify({"error": "Solicitud no encontrada"}), 404

if __name__ == "__main__":
    app.run(port=5006, debug=True)
