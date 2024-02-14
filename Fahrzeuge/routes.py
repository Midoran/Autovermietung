# flake8: noqa:E501

# Importiert benötigte Funktionen und Klassen aus der Flask-Library und die Fahrzeugverwaltungsfunktionen
from flask import request, jsonify, Blueprint, render_template
from Fahrzeuge.fahrzeuge import add_vehicle, get_vehicles, update_vehicle, delete_vehicle

# Erstellt ein Blueprint-Objekt für die Fahrzeuge, welches zur Organisation und Registrierung der Routen dient
fahrzeuge_bp = Blueprint('fahrzeuge', __name__)

# Definiert eine Route zum Hinzufügen eines Fahrzeugs. Akzeptiert nur POST-Anfragen.
@fahrzeuge_bp.route('/add_vehicle', methods=['POST'])
def route_add_vehicle():
    # Extrahiert Daten aus der JSON-Anfrage
    data = request.json
    try:
        # Ruft die Funktion add_vehicle auf, um ein Fahrzeug zur Datenbank hinzuzufügen
        add_vehicle(**data)  # **data entpackt das dictionary direkt in die Funktionsargumente
        # Gibt eine Erfolgsmeldung zurück
        return jsonify({"message": "Fahrzeug erfolgreich hinzugefügt"}), 201 #HTML Statuscode für Created
    except Exception as e:
        # Gibt eine Fehlermeldung zurück, falls ein Fehler auftritt
        return jsonify({"error": str(e)}), 500 #HTML Statuscode für Internal Sever Error
# Definiert eine Route zum Abrufen aller Fahrzeuge. Akzeptiert nur GET-Anfragen.

@fahrzeuge_bp.route('/add_vehicle', methods=['GET'])
def show_add_vehicle_form():
    # Render eine Seite, die das Formular zum Hinzufügen eines Fahrzeugs enthält
    return render_template('add_vehicle.html')

@fahrzeuge_bp.route('/vehicles', methods=['GET'])
def route_get_vehicles():
    try:
        # Ruft die Funktion get_vehicles auf, um alle Fahrzeuge abzurufen
        vehicles = get_vehicles()
        # Gibt die Fahrzeugdaten als JSON zurück
        return jsonify(vehicles), 200 #HTML Statuscode für OK
    except Exception as e:
        # Gibt eine Fehlermeldung zurück, falls ein Fehler auftritt
        return jsonify({"error": str(e)}), 500

# Definiert eine Route zum Aktualisieren eines Fahrzeugs. Akzeptiert nur PUT-Anfragen.
@fahrzeuge_bp.route('/update_vehicle/<int:fahrzeug_id>', methods=['PUT'])
def route_update_vehicle(fahrzeug_id):
    # Extrahiert Daten aus der JSON-Anfrage
    data = request.json
    try:
        # Ruft die Funktion update_vehicle auf, um die Daten eines Fahrzeugs zu aktualisieren
        update_vehicle(fahrzeug_id, **data)
        # Gibt eine Erfolgsmeldung zurück
        return jsonify({"message": "Fahrzeug erfolgreich aktualisiert"}), 200
    except Exception as e:
        # Gibt eine Fehlermeldung zurück, falls ein Fehler auftritt
        return jsonify({"error": str(e)}), 500

# Definiert eine Route zum Löschen eines Fahrzeugs. Akzeptiert nur DELETE-Anfragen.
@fahrzeuge_bp.route('/delete_vehicle/<int:fahrzeug_id>', methods=['DELETE'])
def route_delete_vehicle(fahrzeug_id):
    try:
        # Ruft die Funktion delete_vehicle auf, um ein Fahrzeug aus der Datenbank zu löschen
        delete_vehicle(fahrzeug_id)
        # Gibt eine Erfolgsmeldung zurück
        return jsonify({"message": "Fahrzeug erfolgreich gelöscht"}), 200
    except Exception as e:
        # Gibt eine Fehlermeldung zurück, falls ein Fehler auftritt
        return jsonify({"error": str(e)}), 500