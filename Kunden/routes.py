# flake8: noqa:E501

from flask import request, jsonify, Blueprint, redirect, url_for, render_template, session
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
    return redirect(url_for('registration_success'))

@kunden_bp.route('/registration/success')
def registration_success():
    return render_template('registration_success.html')

@kunden_bp.route('/login', methods=['POST'])
def login_kunde():
    data = request.form.to_dict()
    kunde = authenticate_kunde(data['email'], data['passwort'])
    
    if kunde:
        # Store user ID in the session upon successful login
        session['user_id'] = kunde[0]  # Assuming the user ID is the first column in the Kunden table
        return redirect(url_for('index'))
    
    return jsonify(message='Login fehlgeschlagen'), 401

@kunden_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@kunden_bp.route('/my_account')
def my_account():
    # Retrieve user information from the database using the user ID stored in the session
    user_id = session.get('user_id')
    if user_id:
        user = get_kunden(user_id)  # Replace with your actual function to retrieve user details
        return render_template('my_account.html', user=user)

    # If user is not logged in, redirect to the login page
    return redirect(url_for('login'))