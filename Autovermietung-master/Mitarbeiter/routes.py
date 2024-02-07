# flake8: noqa:E501

from flask import request, jsonify, Blueprint
from Mitarbeiter.mitarbeiter import add_mitarbeiter, get_mitarbeiter, delete_mitarbeiter, update_mitarbeiter

mitarbeiter_bp = Blueprint('mitarbeiter', __name__)


@mitarbeiter_bp.route('/mitarbeiter', methods=['POST'])
def create_mitarbeiter():
    data = request.get_json()
    vorname = data.get('vorname')
    nachname = data.get('nachname')
    position = data.get('position')
    email = data.get('email')

    add_mitarbeiter(vorname, nachname, position, email)
    return jsonify({'message': 'Mitarbeiter hinzugefügt'}), 201


@mitarbeiter_bp.route('/mitarbeiter', methods=['GET'])
def get_all_mitarbeiter():
    mitarbeiter = get_mitarbeiter()
    return jsonify(mitarbeiter), 200


@mitarbeiter_bp.route('/mitarbeiter/<int:mitarbeiter_id>', methods=['PUT'])
def update_single_mitarbeiter(mitarbeiter_id):
    data = request.get_json()
    vorname = data.get('vorname')
    nachname = data.get('nachname')
    position = data.get('position')
    email = data.get('email')

    update_mitarbeiter(mitarbeiter_id, vorname, nachname, position, email)
    return jsonify({'message': 'Mitarbeiter aktualisiert'}), 200


@mitarbeiter_bp.route('/mitarbeiter/<int:mitarbeiter_id>', methods=['DELETE'])
def delete_single_mitarbeiter(mitarbeiter_id):
    delete_mitarbeiter(mitarbeiter_id)
    return jsonify({'message': 'Mitarbeiter gelöscht'}), 200
