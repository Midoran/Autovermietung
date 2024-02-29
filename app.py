# flake8: noqa:E501 - Ignoriert Zeilenlängenbeschränkungen für den gesamten Datei

# Importiert Flask, das Framework für die Webanwendung, und verschiedene Hilfsfunktionen und Module
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, Blueprint
# Importiert die Funktion zur Einrichtung der Datenbank
from Database.database import setup_database, connect_to_database
# Importiert Blueprints für die verschiedenen Ressourcen
from Fahrzeuge.routes import fahrzeuge_bp
from Kunden.routes import kunden_bp
from Mitarbeiter.routes import mitarbeiter_bp
from Rechnungen.routes import rechnungen_bp
from Reservierungen.routes import reservierungen_bp
from Standorte.routes import standorte_bp
from Wartungen.routes import wartungen_bp
# Importiert Funktionen zum Befüllen der Datenbank mit Startdaten für jede Ressource
from Fahrzeuge.fahrzeuge import populate_vehicles
from Mitarbeiter.mitarbeiter import populate_mitarbeiter
from Rechnungen.rechnungen import populate_rechnungen
from Standorte.standorte import populate_standorte
from Wartungen.wartungen import populate_wartungen
from Database.database import connect_to_database
from Kunden.kunden import add_kunde, update_kunde, delete_kunde, get_kunden, authenticate_kunde, populate_kunden, get_kunde_by_id
from Reservierungen.reservierungen import add_reservierung, populate_reservierungen, update_reservierung, \
    connect_to_database, delete_reservierung, get_reservierungen, check_if_vehicle_is_reserved, \
    get_reservations_for_user
import json
import cx_Oracle
from Database.sql_statements import get_create_table_statements, get_alter_table_statements
# Initialisiert die Flask-Anwendung
app = Flask(__name__)

# Registriert Blueprints mit ihrer jeweiligen URL-Präfixen. Blueprints organisieren eine Gruppe von verwandten Routen.
app.register_blueprint(fahrzeuge_bp, url_prefix='/fahrzeuge')
app.register_blueprint(kunden_bp, url_prefix='/kunden')
app.register_blueprint(mitarbeiter_bp, url_prefix='/mitarbeiter')
app.register_blueprint(rechnungen_bp, url_prefix='/rechnungen')
app.register_blueprint(reservierungen_bp, url_prefix='/reservierungen')
app.register_blueprint(standorte_bp, url_prefix='/standorte')
app.register_blueprint(wartungen_bp, url_prefix='/wartungen')

app.secret_key = 'IhrGeheimesSchlüssel'

# Weiterleitung von der Wurzel-URL zur Login-Seite
@app.route('/')
def index():
    if 'user_id' in session:
        conn = connect_to_database()

        # Create a cursor
        cursor = conn.cursor()

        try:
            # Execute the SELECT statement
            cursor.execute("SELECT * FROM Kunden")

            # Fetch all records
            kunden_records = cursor.fetchall()

            # Print the records to the console
            for record in kunden_records:
                print(record)

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

        return render_template('index.html')
    else:
        return render_template('index.html')

# Admin-Benutzername und Passwort
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        kundeid = authenticate_kunde(username, password)

        if kundeid is not None:
            session['user_id'] = kundeid
            session['logged_in'] = True
            flash('Sie wurden erfolgreich eingeloggt.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Falscher Benutzername oder Passwort!', 'danger')
    else:
        return render_template('login.html')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    if session.get('logged_in'):
        session.pop('logged_in', False)
        session.pop('user_id', None)
        flash('Sie wurden erfolgreich ausgeloggt.', 'success')
    return redirect(url_for('index'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route('/list', methods=['GET', 'POST'])
def list():
    return render_template('list.html')

@app.route('/faq', methods=['POST', 'GET'])
def faq():
    return render_template('faq.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')
@app.route('/reservation', methods=['POST'])
def reservation():
    if session.get('logged_in'):
        if request.method == 'POST':
            data = request.form.to_dict()
            print(data)
            add_reservierung(1, data['startDate'] ,data['endDate'] , 'a', data['vehicle_id'] ,session.get('user_id') ,1)
            print(get_reservierungen())
            return redirect(url_for('reservation_success'))
        else:
            return render_template('reservation.html')
    else:
        return redirect(url_for('login'))

@app.route('/reservation/<int:fahrzeug_id>', methods=['GET'])
def reservation_by_vehicle(fahrzeug_id):
    if session.get('logged_in'):
        return render_template('reservation.html', fahrzeug_id=fahrzeug_id)
    else:
        return redirect(url_for('login'))

@app.route('/reservation_success', methods=['GET', 'POST'])
def reservation_success():
    return render_template('reservation_success.html')

@app.route('/my_reservations')
def my_reservations():
    # Assuming 'user_id' is stored in session when the user logs in
    user_id = session['user_id']
    # Fetch all reservations for the user from the database
    # This is a placeholder function, replace it with your actual implementation
    reservations = get_reservations_for_user(user_id)
    return render_template('my_reservations.html', reservations=reservations)
@app.route('/check_reservation', methods=['POST'])
def check_reservation():
    start_date = request.form['startDate']
    end_date = request.form['endDate']
    vehicle_id = request.form['vehicle_id']
    # Query your database to check if the vehicle is reserved for the given date range
    # This is a placeholder function, replace it with your actual implementation
    is_reserved = check_if_vehicle_is_reserved(start_date, end_date, vehicle_id)
    return jsonify({'is_reserved': is_reserved})

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        add_kunde(data['vorname'], data['nachname'], data['geburtsdatum'], data['adresse_plz'], data['adresse_strasse'],
              data['adresse_wohnort'], data['fuehrerscheinnummer'], data['fuehrerscheinklasse'], data['telefonnummer'],
              data['email'], data['passwort'])
    else:
        return render_template('registration.html')
    return redirect(url_for('registration_success'))
  

@app.route('/registration_success')
def registration_success():
    return render_template('registration_success.html')

@app.route('/my_account')
def my_account():
    if 'user_id' in session:
        user = get_kunde_by_id(session['user_id'])
        return render_template('my_account.html', user=user)

# Hauptfunktion zum Starten der Anwendung
def main():
    # Ruft Funktionen auf, um die Datenbank einzurichten und mit Startdaten zu befüllen
    #setup_database()  # Initialisiert die Datenbankstruktur
    #populate_mitarbeiter()  # Fügt Mitarbeiterdaten in die Datenbank ein
    #populate_standorte()  # Fügt Standortdaten in die Datenbank ein
    #populate_vehicles()  # Fügt Fahrzeugdaten in die Datenbank ein
    #populate_kunden()  # Fügt Kundendaten in die Datenbank ein
    #populate_reservierungen()  # Fügt Reservierungsdaten in die Datenbank ein
    #populate_rechnungen()  # Fügt Rechnungsdaten in die Datenbank ein
    #populate_wartungen()  # Fügt Wartungsdaten in die Datenbank ein

    # Startet die Flask-Anwendung
    app.run(debug=True)  # 'debug=False' deaktiviert den Debug-Modus für die Produktion

# Stellt sicher, dass die Hauptfunktion ausgeführt wird, wenn das Skript direkt aufgerufen wird
if __name__ == "__main__":
    main()
