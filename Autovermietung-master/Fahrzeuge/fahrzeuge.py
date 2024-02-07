# flake8: noqa:E501

from Database.database import connect_to_database


def add_vehicle(standort_id, hersteller, modell, baujahr, verfuegbarkeit, preis, kilometerstand, kennzeichen, fahrzeugklasse):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = "INSERT INTO Fahrzeuge (StandortID, Hersteller, Modell, Baujahr, Verfuegbarkeit, Preis, Kilometerstand, Kennzeichen, Fahrzeugklasse) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)"
    cursor.execute(query, (standort_id, hersteller, modell, baujahr, verfuegbarkeit, preis, kilometerstand, kennzeichen, fahrzeugklasse))

    conn.commit()
    conn.close()


def get_vehicles():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Fahrzeuge")
    vehicles = cursor.fetchall()

    conn.close()
    return vehicles


def update_vehicle(fahrzeug_id, standort_id, hersteller, modell, baujahr, verfuegbarkeit, preis, kilometerstand, kennzeichen, fahrzeugklasse):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = "UPDATE Fahrzeuge SET StandortID = :1, Hersteller = :2, Modell = :3, Baujahr = :4, Verfuegbarkeit = :5, Preis = :6, Kilometerstand = :7, Kennzeichen = :8, Fahrzeugklasse = :9 WHERE FahrzeugID = :10"
    cursor.execute(query, (standort_id, hersteller, modell, baujahr, verfuegbarkeit, preis, kilometerstand, kennzeichen, fahrzeugklasse, fahrzeug_id))

    conn.commit()
    conn.close()


def delete_vehicle(fahrzeug_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Fahrzeuge WHERE FahrzeugID = :1", (fahrzeug_id,))

    conn.commit()
    conn.close()


def populate_vehicles():
    vehicles = [
        (3, "Volkswagen", "Golf 5", 2022, 'N', 58418.00, 128545, "KZ582", "Klasse A"),
        (4, "Nissan", "Micra", 2000, 'N', 38990.00, 91257, "KZ286", "Klasse B"),
        (4, "Ford", "Focus", 2006, 'J', 33799.00, 156914, "KZ662", "Klasse B"),
        (4, "Volkswagen", "Golf Variant", 2018, 'J', 34997.00, 199540, "KZ129", "Klasse A"),
        (4, "Hyundai", "i20", 2004, 'N', 66000.00, 137722, "KZ162", "Klasse A"),
        (1, "Nissan", "Qashquai", 2018, 'N', 34000.00, 74762, "KZ853", "Klasse B"),
        (3, "Honda", "Civic", 2008, 'N', 32603.00, 58931, "KZ258", "Klasse C"),
        (4, "Ford", "Fiesta", 2017, 'J', 48656.00, 166053, "KZ384", "Klasse A"),
        (1, "Volkswagen", "Tiguan", 2018, 'J', 39534.00, 125654, "KZ433", "Klasse A"),
        (3, "Mercedes", "E 350", 2009, 'N', 60915.00, 87034, "KZ460", "Klasse B")
    ]

    for vehicle in vehicles:
        add_vehicle(*vehicle)