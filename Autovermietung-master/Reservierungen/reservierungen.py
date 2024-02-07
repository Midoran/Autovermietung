# flake8: noqa:E501

from Database.database import connect_to_database


def add_reservierung(kilometerstand, startdatum, enddatum, status, fahrzeug_id, kunden_id, mitarbeiter_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """INSERT INTO Reservierungen (Kilometerstand, StartDatum, EndDatum, Status, FahrzeugID, KundenID, MitarbeiterID) 
               VALUES (:1, :2, :3, :4, :5, :6, :7)"""
    cursor.execute(query, (kilometerstand, startdatum, enddatum, status, fahrzeug_id, kunden_id, mitarbeiter_id))

    conn.commit()
    conn.close()


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
        (100, '01-JAN-2023', '15-JAN-2023', 'A', 1, 1, 1),
        (200, '15-FEB-2023', '28-FEB-2023', 'A', 2, 2, 2),
        (150, '10-MAR-2023', '25-MAR-2023', 'A', 3, 3, 3),
        (180, '05-APR-2023', '20-APR-2023', 'A', 4, 4, 4),
        (120, '20-APR-2023', '05-MAY-2023', 'A', 5, 5, 5)
    ]
    for reservierung in reservierungen:
        add_reservierung(*reservierung)
