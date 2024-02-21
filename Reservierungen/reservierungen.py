# flake8: noqa:E501

from Database.database import connect_to_database


def add_reservierung(kilometerstand, startdatum, enddatum, status, fahrzeug_id, kunden_id, mitarbeiter_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """INSERT INTO Reservierungen (Kilometerstand, StartDatum, EndDatum, Status, FahrzeugID, KundenID, MitarbeiterID) 
               VALUES (:1, TO_DATE(:2, 'DD-MM-YYYY'), TO_DATE(:3, 'DD-MM-YYYY'), :4, :5, :6, :7)"""
    cursor.execute(query, (kilometerstand, startdatum, enddatum, status, fahrzeug_id, kunden_id, mitarbeiter_id))

    conn.commit()
    conn.close()

    return {
        'kilometerstand': kilometerstand,
        'startdatum': startdatum,
        'enddatum': enddatum,
        'status': status,
        'fahrzeug_id': fahrzeug_id,
        'kunden_id': kunden_id,
        'mitarbeiter_id': mitarbeiter_id,

    }
def get_reservierungen():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Reservierungen")
    reservierungen = cursor.fetchall()

    conn.close()
    return reservierungen


def update_reservierung(reservierung_id, kilometerstand, startdatum, enddatum, status, fahrzeug_id, kunden_id, mitarbeiter_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """UPDATE Reservierungen 
               SET Kilometerstand = :1, StartDatum = :2, EndDatum = :3, Status = :4, FahrzeugID = :5, KundenID = :6, MitarbeiterID = :7
               WHERE ReservierungsID = :8"""
    cursor.execute(query, (kilometerstand, startdatum, enddatum, status, fahrzeug_id, kunden_id, mitarbeiter_id, reservierung_id))

    conn.commit()
    conn.close()


def delete_reservierung(reservierung_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Reservierungen WHERE ReservierungsID = :1", (reservierung_id,))

    conn.commit()
    conn.close()


def populate_reservierungen():
    reservierungen = [
        (100, '01-01-2023', '15-01-2023', 'A', 1, 1, 1),
        (200, '15-02-2023', '28-02-2023', 'A', 2, 2, 2),
        (150, '10-03-2023', '25-03-2023', 'A', 3, 3, 3),
        (180, '05-04-2023', '20-04-2023', 'A', 4, 4, 4),
        (120, '20-05-2023', '05-05-2023', 'A', 5, 5, 5)
    ]
    for reservierung in reservierungen:
        add_reservierung(*reservierung)
