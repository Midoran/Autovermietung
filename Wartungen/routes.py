# flake8: noqa:E501

from flask import request, jsonify, Blueprint
from Wartungen.wartungen import add_wartung, get_wartungen, update_wartung, delete_wartung

wartungen_bp = Blueprint('wartungen', __name__)

@wartungen_bp.route('/wartungen', methods=['POST'])
def add_wartung_route():
    data = request.get_json()
    fahrzeug_id = data.get('fahrzeug_id')
    wartungsdatum = data.get('wartungsdatum')
    beschreibung = data.get('beschreibung')
    bemerkungen = data.get('bemerkungen')

    add_wartung(fahrzeug_id, wartungsdatum, beschreibung, bemerkungen)

    return jsonify({"message": "Wartung hinzugefügt"}), 201


@wartungen_bp.route('/wartungen', methods=['GET'])
def get_wartungen_route():
    wartungen = get_wartungen()
    return jsonify(wartungen), 200


@wartungen_bp.route('/wartungen/<int:wartungs_id>', methods=['PUT'])
def update_wartung_route(wartungs_id):
    data = request.get_json()
    fahrzeug_id = data.get('fahrzeug_id')
    wartungsdatum = data.get('wartungsdatum')
    beschreibung = data.get('beschreibung')
    bemerkungen = data.get('bemerkungen')

    update_wartung(wartungs_id, fahrzeug_id, wartungsdatum, beschreibung, bemerkungen)

    return jsonify({"message": f"Wartung {wartungs_id} aktualisiert"}), 200


@wartungen_bp.route('/wartungen/<int:wartungs_id>', methods=['DELETE'])
def delete_wartung_route(wartungs_id):
    delete_wartung(wartungs_id)
    return jsonify({"message": f"Wartung {wartungs_id} gelöscht"}), 200
