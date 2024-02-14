# flake8: noqa:E501

from Database.database import connect_to_database


def add_wartung(fahrzeug_id, wartungsdatum, beschreibung, bemerkungen):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """INSERT INTO Wartungen (FahrzeugID, Wartungsdatum, Beschreibung, Bemerkungen) 
               VALUES (:1, TO_DATE(:2, 'DD-MM-YYYY'), :3, :4)"""
    cursor.execute(query, (fahrzeug_id, wartungsdatum, beschreibung, bemerkungen))

    conn.commit()
    conn.close()


def get_wartungen():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Wartungen")
    wartungen = cursor.fetchall()

    conn.close()
    return wartungen


def update_wartung(wartungs_id, fahrzeug_id, wartungsdatum, beschreibung, bemerkungen):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """UPDATE Wartungen 
               SET FahrzeugID = :1, Wartungsdatum = :2, Beschreibung = :3, Bemerkungen = :4 
               WHERE WartungsID = :5"""
    cursor.execute(query, (fahrzeug_id, wartungsdatum, beschreibung, bemerkungen, wartungs_id))

    conn.commit()
    conn.close()


def delete_wartung(wartungs_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Wartungen WHERE WartungsID = :1", (wartungs_id,))

    conn.commit()
    conn.close()


def populate_wartungen():
    wartungen = [
        (1, '01-01-2023', 'Ölwechsel', 'Keine besonderen Bemerkungen'),
        (2, '15-02-2023', 'Bremsenüberholung', 'Bremsbeläge ersetzt'),
        (3, '10-03-2023', 'Reifenwechsel', 'Neue Winterreifen installiert'),
        (1, '05-04-2023', 'Inspektion', 'Allgemeine Inspektion durchgeführt'),
        (4, '20-05-2023', 'Luftfilterwechsel', 'Neuer Luftfilter eingebaut')
    ]
    for wartung in wartungen:
        add_wartung(*wartung)