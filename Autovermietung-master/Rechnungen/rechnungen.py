# flake8: noqa:E501

from Database.database import connect_to_database


def add_rechnung(rechnungsdatum, rechnungsbetrag, status, reservierung_id, kunden_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """INSERT INTO Rechnungen (Rechnungsdatum, Rechnungsbetrag, Status, ReservierungID, KundenID) 
               VALUES (:1, :2, :3, :4, :5)"""
    cursor.execute(query, (rechnungsdatum, rechnungsbetrag, status, reservierung_id, kunden_id))

    conn.commit()
    conn.close()


def get_rechnungen():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Rechnungen")
    rechnungen = cursor.fetchall()

    conn.close()
    return rechnungen


def update_rechnung(rechnung_id, rechnungsdatum, rechnungsbetrag, status, reservierung_id, kunden_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """UPDATE Rechnungen 
               SET Rechnungsdatum = :1, Rechnungsbetrag = :2, Status = :3, ReservierungID = :4, KundenID = :5 
               WHERE RechnungID = :6"""
    cursor.execute(query, (rechnungsdatum, rechnungsbetrag, status, reservierung_id, kunden_id, rechnung_id))

    conn.commit()
    conn.close()


def delete_rechnung(rechnung_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Rechnungen WHERE RechnungID = :1", (rechnung_id,))

    conn.commit()
    conn.close()


def populate_rechnungen():
    rechnungen = [
        ('01-JAN-2023', 250.0, 'B', 1, 1),
        ('15-FEB-2023', 350.0, 'O', 2, 2),
        ('10-MAR-2023', 200.0, 'O', 3, 3),
        ('05-APR-2023', 300.0, 'O', 4, 4),
        ('20-APR-2023', 180.0, 'B', 5, 5)
    ]
    for rechnung in rechnungen:
        add_rechnung(*rechnung)
