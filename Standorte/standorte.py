# flake8: noqa:E501

from Database.database import connect_to_database


def add_standort(standortname, adresse_plz, adresse_strasse, adresse_wohnort, anzahl_stellplatz):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """INSERT INTO Standorte (Standortname, AdressePLZ, AdresseStrasse, AdresseWohnort, AnzahlStellplatz) 
               VALUES (:1, :2, :3, :4, :5)"""
    cursor.execute(query, (standortname, adresse_plz, adresse_strasse, adresse_wohnort, anzahl_stellplatz))

    conn.commit()
    conn.close()


def get_standorte():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Standorte")
    standorte = cursor.fetchall()

    conn.close()
    return standorte


def update_standort(standort_id, standortname, adresse_plz, adresse_strasse, adresse_wohnort, anzahl_stellplatz):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """UPDATE Standorte 
               SET Standortname = :1, AdressePLZ = :2, AdresseStrasse = :3, AdresseWohnort = :4, AnzahlStellplatz = :5 
               WHERE StandortID = :6"""
    cursor.execute(query, (standortname, adresse_plz, adresse_strasse, adresse_wohnort, anzahl_stellplatz, standort_id))

    conn.commit()
    conn.close()


def delete_standort(standort_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Standorte WHERE StandortID = :1", (standort_id,))

    conn.commit()
    conn.close()


def populate_standorte():
    standorte = [
        ("Göttingen 1", "37085", "Musterstraße 1", "Göttingen", 1),
        ("Göttingen 2", "37048", "Beispielweg 2", "Göttingen", 2),
        ("Göttingen 3", "37048", "Musterweg 3", "Göttingen", 3),
        ("Göttingen 4", "37085", "Beispielstraße 4", "Göttingen", 4)
        ]

    for standort in standorte:
        add_standort(*standort)
