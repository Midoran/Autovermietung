# flake8: noqa:E501

from flask import request, jsonify, Blueprint
from Fahrzeuge.fahrzeuge import add_vehicle, get_vehicles, update_vehicle, delete_vehicle

fahrzeuge_bp = Blueprint('fahrzeuge', __name__)


@fahrzeuge_bp.route('/add_vehicle', methods=['POST'])
def route_add_vehicle():
    data = request.json
    try:
        add_vehicle(**data)  # **data entpackt das dictionary direkt in die Funktionsargumente
        return jsonify({"message": "Fahrzeug erfolgreich hinzugefügt"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@fahrzeuge_bp.route('/vehicles', methods=['GET'])
def route_get_vehicles():
    try:
        vehicles = get_vehicles()
        return jsonify(vehicles), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@fahrzeuge_bp.route('/update_vehicle/<int:fahrzeug_id>', methods=['PUT'])
def route_update_vehicle(fahrzeug_id):
    data = request.json
    try:
        update_vehicle(fahrzeug_id, **data)
        return jsonify({"message": "Fahrzeug erfolgreich aktualisiert"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@fahrzeuge_bp.route('/delete_vehicle/<int:fahrzeug_id>', methods=['DELETE'])
def route_delete_vehicle(fahrzeug_id):
    try:
        delete_vehicle(fahrzeug_id)
        return jsonify({"message": "Fahrzeug erfolgreich gelöscht"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
