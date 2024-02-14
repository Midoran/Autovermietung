# flake8: noqa:E501

from Database.database import connect_to_database


def add_mitarbeiter(vorname, nachname, position, email):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """INSERT INTO Mitarbeiter (Vorname, Nachname, Position, Email) 
               VALUES (:1, :2, :3, :4)"""
    cursor.execute(query, (vorname, nachname, position, email))

    conn.commit()
    conn.close()


def get_mitarbeiter():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Mitarbeiter")
    mitarbeiter = cursor.fetchall()

    conn.close()
    return mitarbeiter


def update_mitarbeiter(mitarbeiter_id, vorname, nachname, position, email):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """UPDATE Mitarbeiter 
               SET Vorname = :1, Nachname = :2, Position = :3, Email = :4 
               WHERE MitarbeiterID = :5"""
    cursor.execute(query, (vorname, nachname, position, email, mitarbeiter_id))

    conn.commit()
    conn.close()


def delete_mitarbeiter(mitarbeiter_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Mitarbeiter WHERE MitarbeiterID = :1", (mitarbeiter_id,))

    conn.commit()
    conn.close()


def populate_mitarbeiter():
    mitarbeiter = [
        ("Max", "Mustermann", "Manager", "max@example.com"),
        ("Maria", "Musterfrau", "Verkäufer", "maria@example.com"),
        ("Peter", "Schmidt", "Techniker", "peter@example.com"),
        ("Anna", "Schulz", "Buchhalter", "anna@example.com"),
        ("Tom", "Müller", "Kundensupport", "tom@example.com")
    ]
    for mitarbeiter in mitarbeiter:
        add_mitarbeiter(*mitarbeiter)
