# flake8: noqa:E501

from flask import request, jsonify, Blueprint, redirect, url_for
from Kunden.kunden import add_kunde, update_kunde, delete_kunde, get_kunden, authenticate_kunde

kunden_bp = Blueprint('kunden', __name__)


@kunden_bp.route('/kunden', methods=['POST'])
def create_kunde():
    data = request.get_json()
    add_kunde(data['vorname'], data['nachname'], data['geburtsdatum'], data['adresse_plz'], data['adresse_strasse'],
              data['adresse_wohnort'], data['fuehrerscheinnummer'], data['fuehrerscheinklasse'], data['telefonnummer'],
              data['email'], data['passwort'])
    return jsonify(message='Kunde wurde hinzugefügt'), 201


@kunden_bp.route('/kunden', methods=['GET'])
def get_all_kunden():
    kunden = get_kunden()
    return jsonify(kunden), 200


@kunden_bp.route('/kunden/<int:kunde_id>', methods=['PUT'])
def update_one_kunde(kunde_id):
    data = request.get_json()
    update_kunde(kunde_id, data['vorname'], data['nachname'], data['geburtsdatum'], data['adresse_plz'],
                 data['adresse_strasse'], data['adresse_wohnort'], data['fuehrerscheinnummer'],
                 data['fuehrerscheinklasse'], data['telefonnummer'], data['email'], data['passwort'])
    return jsonify(message='Kunde wurde aktualisiert'), 200


@kunden_bp.route('/kunden/<int:kunde_id>', methods=['DELETE'])
def delete_one_kunde(kunde_id):
    delete_kunde(kunde_id)
    return jsonify(message='Kunde wurde gelöscht'), 200


@kunden_bp.route('/registration', methods=['POST'])
def register_kunde():
    data = request.form.to_dict()
    add_kunde(data['vorname'], data['nachname'], data['geburtsdatum'], data['adresse_plz'], data['adresse_strasse'],
              data['adresse_wohnort'], data['fuehrerscheinnummer'], data['fuehrerscheinklasse'], data['telefonnummer'],
              data['email'], data['passwort'])
    return jsonify(message='Benutzer wurde registriert'), 201

@kunden_bp.route('/login', methods=['POST'])
def login_kunde():
    data = request.form.to_dict()
    kunde = authenticate_kunde(data['email'], data['passwort'])

    if kunde:
         return redirect(url_for('index'))
    return jsonify(message='Login fehlgeschlagen'), 401