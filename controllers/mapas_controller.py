from flask import Blueprint, request, jsonify
from services.mapas_service import MapasService

mapas_bp = Blueprint("mapas", __name__)
service = MapasService()

@mapas_bp.route("/mapas", methods=["GET"])
def listar_lugares():
    return jsonify(service.listar_lugares()), 200

@mapas_bp.route("/mapas/filtrar", methods=["GET"])
def filtrar():
    categoria = request.args.get("categoria")
    return jsonify(service.filtrar_por_categoria(categoria)), 200
