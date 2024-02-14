# flake8: noqa:E501

from flask import request, jsonify, Blueprint
from Rechnungen.rechnungen import add_rechnung,update_rechnung,delete_rechnung, get_rechnungen

rechnungen_bp = Blueprint('rechnungen', __name__)


@rechnungen_bp.route('/rechnungen', methods=['POST'])
def create_rechnung():
    data = request.get_json()
    try:
        datum = data['datum']
        status = data['status']
        reservierung_id = data['reservierung_id']
        kunde_id = data['kunde_id']
        wartung_id = data['wartung_id']
    except KeyError:
        return jsonify({'error': 'Ungültige Eingabe'}), 400

    add_rechnung(datum, status, reservierung_id, kunde_id, wartung_id)
    return jsonify({'message': 'Rechnung wurde hinzugefügt'}), 201


@rechnungen_bp.route('/rechnungen', methods=['GET'])
def read_rechnungen():
    rechnungen = get_rechnungen()
    return jsonify({'rechnungen': rechnungen}), 200


@rechnungen_bp.route('/rechnungen/<int:rechnung_id>', methods=['PUT'])
def update_rechnung_by_id(rechnung_id):
    data = request.get_json()
    try:
        datum = data['datum']
        status = data['status']
        reservierung_id = data['reservierung_id']
        kunde_id = data['kunde_id']
        wartung_id = data['wartung_id']
    except KeyError:
        return jsonify({'error': 'Ungültige Eingabe'}), 400

    update_rechnung(rechnung_id, datum, status, reservierung_id, kunde_id, wartung_id)
    return jsonify({'message': f'Rechnung {rechnung_id} wurde aktualisiert'}), 200


@rechnungen_bp.route('/rechnungen/<int:rechnung_id>', methods=['DELETE'])
def delete_rechnung_by_id(rechnung_id):
    delete_rechnung(rechnung_id)
    return jsonify({'message': f'Rechnung {rechnung_id} wurde gelöscht'}), 200
