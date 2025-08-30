import os
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# "Base de datos" simulada
lugares = [
    {
        "id": 1,
        "nombre": "Cascada La Chorrera",
        "categoria": "naturaleza",
        "lat": 4.596,
        "lng": -74.065,
        "popularidad": 95,
        "fecha_publicacion": "2025-08-01"
    },
    {
        "id": 2,
        "nombre": "Museo del Oro",
        "categoria": "cultura",
        "lat": 4.601,
        "lng": -74.072,
        "popularidad": 88,
        "fecha_publicacion": "2025-07-15"
    },
    {
        "id": 3,
        "nombre": "Parque Simón Bolívar",
        "categoria": "recreación",
        "lat": 4.652,
        "lng": -74.093,
        "popularidad": 70,
        "fecha_publicacion": "2025-06-10"
    }
]

# Función auxiliar para calcular distancia
def distancia(lat1, lng1, lat2, lng2):
    return ((lat1 - lat2)**2 + (lng1 - lng2)**2)**0.5 * 111  # ~km

# Endpoint: mapa completo
@app.route("/mapa", methods=["GET"])
def mostrar_mapa():
    return jsonify(lugares), 200

# Endpoint: filtrar por criterios
@app.route("/mapa/filtrar", methods=["GET"])
def filtrar_mapa():
    categoria = request.args.get("categoria")
    distancia_max = request.args.get("distancia")  # en km
    lat = request.args.get("lat", type=float)
    lng = request.args.get("lng", type=float)
    popularidad_min = request.args.get("popularidad", type=int)
    fecha_min = request.args.get("fecha")

    resultados = lugares

    if categoria:
        resultados = [l for l in resultados if l["categoria"] == categoria]

    if distancia_max and lat and lng:
        distancia_max = float(distancia_max)
        resultados = [
            l for l in resultados
            if distancia(lat, lng, l["lat"], l["lng"]) <= distancia_max
        ]

    if popularidad_min:
        resultados = [l for l in resultados if l["popularidad"] >= popularidad_min]

    if fecha_min:
        fecha_min = datetime.strptime(fecha_min, "%Y-%m-%d").date()
        resultados = [
            l for l in resultados
            if datetime.strptime(l["fecha_publicacion"], "%Y-%m-%d").date() >= fecha_min
        ]

    return jsonify(resultados), 200

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", "5006"))
    app.run(host="127.0.0.1", port=puerto, debug=True)
