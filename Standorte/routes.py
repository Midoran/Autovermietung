# flake8: noqa:E501

from flask import request, jsonify, Blueprint
from Standorte.standorte import add_standort, get_standorte, update_standort, delete_standort

standorte_bp = Blueprint('standorte', __name__)


@standorte_bp.route('/standorte', methods=['POST'])
def add_standort_route():
    data = request.get_json()
    standortname = data['standortname']
    adresse_plz = data['adresse_plz']
    adresse_strasse = data['adresse_strasse']
    adresse_wohnort = data['adresse_wohnort']
    anzahl_stellplatz = data['anzahl_stellplatz']
    add_standort(standortname, adresse_plz, adresse_strasse, adresse_wohnort, anzahl_stellplatz)
    return jsonify({"message": "Standort hinzugefügt!"})


@standorte_bp.route('/standorte', methods=['GET'])
def get_standorte_route():
    standorte = get_standorte()
    return jsonify(standorte)


@standorte_bp.route('/standorte/<int:standort_id>', methods=['PUT'])
def update_standort_route(standort_id):
    data = request.get_json()
    standortname = data['standortname']
    adresse_plz = data['adresse_plz']
    adresse_strasse = data['adresse_strasse']
    adresse_wohnort = data['adresse_wohnort']
    anzahl_stellplatz = data['anzahl_stellplatz']
    update_standort(standort_id, standortname, adresse_plz, adresse_strasse, adresse_wohnort, anzahl_stellplatz)
    return jsonify({"message": "Standort aktualisiert!"})


@standorte_bp.route('/standorte/<int:standort_id>', methods=['DELETE'])
def delete_standort_route(standort_id):
    delete_standort(standort_id)
    return jsonify({"message": "Standort gelöscht!"})
