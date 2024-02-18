# flake8: noqa:E501

# Importiert die Funktion zur Herstellung einer Datenbankverbindung aus einem benutzerdefinierten Modul
from Database.database import connect_to_database

def add_vehicle(standort_id, hersteller, modell, baujahr, verfuegbarkeit, preis, kilometerstand, kennzeichen, fahrzeugklasse):
    """
    Fügt ein neues Fahrzeug zur Datenbank hinzu.

    Parameter:
        standort_id (int): Die ID des Standorts, an dem das Fahrzeug verfügbar ist.
        hersteller (str): Der Hersteller des Fahrzeugs.
        modell (str): Das Modell des Fahrzeugs.
        baujahr (int): Das Baujahr des Fahrzeugs.
        verfuegbarkeit (str): Die Verfügbarkeit des Fahrzeugs ('J' für verfügbar, 'N' für nicht verfügbar).
        preis (float): Der Preis des Fahrzeugs.
        kilometerstand (float): Der Kilometerstand des Fahrzeugs.
        kennzeichen (str): Das Kennzeichen des Fahrzeugs.
        fahrzeugklasse (str): Die Klassifizierung des Fahrzeugs.

    Returns:
        None
    """
    # Herstellen einer Verbindung zur Datenbank
    conn = connect_to_database()
    cursor = conn.cursor()

    # Definiert die SQL-Anweisung zum Einfügen eines neuen Fahrzeugs
    query = "INSERT INTO Fahrzeuge (StandortID, Hersteller, Modell, Baujahr, Verfuegbarkeit, Preis, Kilometerstand, Kennzeichen, Fahrzeugklasse) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)"
    # Führt die SQL-Anweisung aus
    cursor.execute(query, (standort_id, hersteller, modell, baujahr, verfuegbarkeit, preis, kilometerstand, kennzeichen, fahrzeugklasse))

    # Bestätigt die Transaktion
    conn.commit()
    # Schließt die Verbindung zur Datenbank
    conn.close()

def get_vehicles():
    """
    Ruft alle Fahrzeugdaten aus der Datenbank ab.

    Returns:
        list: Eine Liste von Tupeln, wobei jedes Tupel die Daten eines Fahrzeugs enthält.
    """
    # Herstellen einer Verbindung zur Datenbank
    conn = connect_to_database()
    cursor = conn.cursor()

    # Führt eine SQL-Abfrage aus, um alle Fahrzeuge abzurufen
    cursor.execute("SELECT * FROM Fahrzeuge")
    vehicles = cursor.fetchall()

    # Schließt die Verbindung zur Datenbank
    conn.close()
    return vehicles

def update_vehicle(fahrzeug_id, standort_id, hersteller, modell, baujahr, verfuegbarkeit, preis, kilometerstand, kennzeichen, fahrzeugklasse):
    """
    Aktualisiert die Daten eines bestehenden Fahrzeugs in der Datenbank.

    Parameter:
        Die Funktion nimmt die gleichen Parameter wie `add_vehicle` plus die `fahrzeug_id` an.

    Returns:
        None
    """
    # Herstellen einer Verbindung zur Datenbank
    conn = connect_to_database()
    cursor = conn.cursor()

    # Definiert die SQL-Anweisung zur Aktualisierung der Fahrzeugdaten
    query = "UPDATE Fahrzeuge SET StandortID = :1, Hersteller = :2, Modell = :3, Baujahr = :4, Verfuegbarkeit = :5, Preis = :6, Kilometerstand = :7, Kennzeichen = :8, Fahrzeugklasse = :9 WHERE FahrzeugID = :10"
    # Führt die SQL-Anweisung mit den gegebenen Parametern aus
    cursor.execute(query, (standort_id, hersteller, modell, baujahr, verfuegbarkeit, preis, kilometerstand, kennzeichen, fahrzeugklasse, fahrzeug_id))
    
def delete_vehicle(fahrzeug_id):
    """
    Löscht ein Fahrzeug aus der Datenbank basierend auf seiner ID.

    Parameter:
        fahrzeug_id (int): Die eindeutige ID des zu löschenden Fahrzeugs.

    Returns:
        None
    """
    # Herstellen einer Verbindung zur Datenbank
    conn = connect_to_database()
    cursor = conn.cursor()

    # Definiert die SQL-Anweisung zum Löschen eines Fahrzeugs
    query = "DELETE FROM Fahrzeuge WHERE FahrzeugID = :1"
    # Führt die SQL-Anweisung aus, wobei :1 durch die `fahrzeug_id` ersetzt wird
    cursor.execute(query, (fahrzeug_id,))

    # Bestätigt die Transaktion, um die Löschoperation durchzuführen
    conn.commit()
    # Schließt die Verbindung zur Datenbank
    conn.close()

def populate_vehicles():
    vehicles = [
        (3, "Volkswagen", "Golf 5", 2022, 'N', 58418.92, 128545, "KZ582", "Klasse A"),
        (4, "Nissan", "Micra", 2000, 'N', 38283.29, 91257, "KZ286", "Klasse B"),
        (4, "Ford", "Focus", 2006, 'J', 33799.79, 156914, "KZ662", "Klasse B"),
        (4, "Volkswagen", "Golf Variant", 2018, 'J', 34997.24, 199540, "KZ129", "Klasse A"),
        (4, "Hyundai", "i20", 2004, 'N', 66068.17, 137722, "KZ162", "Klasse A"),
        (1, "Nissan", "Qashquai", 2018, 'N', 77075.99, 74762, "KZ853", "Klasse B"),
        (3, "Honda", "Civic", 2008, 'N', 32603.31, 58931, "KZ258", "Klasse C"),
        (4, "Ford", "Fiesta", 2017, 'J', 48656.65, 166053, "KZ384", "Klasse A"),
        (1, "Volkswagen", "Tiguan", 2018, 'J', 39534.56, 125654, "KZ433", "Klasse A"),
        (3, "Mercedes", "E 350", 2009, 'N', 60915.85, 87034, "KZ460", "Klasse B")
    ]

    for vehicle in vehicles:
        add_vehicle(*vehicle)

def search_vehicles(rental_date, location):
    # Implement your logic to search for vehicles based on rental_date and location
    # This might involve querying a database or some other data source

    # For example, assuming you have a list of vehicles, you can filter them:
    filtered_vehicles = [vehicle for vehicle in get_vehicles() if
                         vehicle['rental_date'] == rental_date and vehicle['location'] == location]

    return filtered_vehicles