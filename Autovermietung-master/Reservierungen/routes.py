# flake8: noqa:E501

from flask import request, jsonify, Blueprint
from Reservierungen.reservierungen import add_reservierung, get_reservierungen,update_reservierung, delete_reservierung

reservierungen_bp = Blueprint('reservierungen', __name__)

@reservierungen_bp.route('/reservierungen', methods=['POST'])
def create_reservierung():
    data = request.get_json()
    kilometer = data['kilometer']
    start_datum = data['start_datum']
    end_datum = data['end_datum']
    status = data['status']
    fahrzeug_id = data['fahrzeug_id']
    kunde_id = data['kunde_id']
    mitarbeiter_id = data['mitarbeiter_id']

    add_reservierung(kilometer, start_datum, end_datum, status, fahrzeug_id, kunde_id, mitarbeiter_id)

    return jsonify({"message": "Reservierung erstellt"}), 201


@reservierungen_bp.route('/reservierungen', methods=['GET'])
def get_all_reservierungen():
    reservierungen = get_reservierungen()
    return jsonify(reservierungen), 200


@reservierungen_bp.route('/reservierungen/<int:reservierung_id>', methods=['PUT'])
def update_one_reservierung(reservierung_id):
    data = request.get_json()
    kilometer = data['kilometer']
    start_datum = data['start_datum']
    end_datum = data['end_datum']
    status = data['status']
    fahrzeug_id = data['fahrzeug_id']
    kunde_id = data['kunde_id']
    mitarbeiter_id = data['mitarbeiter_id']

    update_reservierung(reservierung_id, kilometer, start_datum, end_datum, status, fahrzeug_id, kunde_id, mitarbeiter_id)

    return jsonify({"message": "Reservierung aktualisiert"}), 200


@reservierungen_bp.route('/reservierungen/<int:reservierung_id>', methods=['DELETE'])
def delete_one_reservierung(reservierung_id):
    delete_reservierung(reservierung_id)
    return jsonify({"message": "Reservierung gelöscht"}), 200
