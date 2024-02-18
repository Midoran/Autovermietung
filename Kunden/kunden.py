# flake8: noqa:E501

from Database.database import connect_to_database


def add_kunde(vorname, nachname, geburtsdatum, adresse_plz, adresse_strasse, adresse_wohnort, fuehrerscheinnummer, fuehrerscheinklasse, telefonnummer, email, passwort):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """INSERT INTO Kunden (Vorname, Nachname, Geburtsdatum, AdressePLZ, AdresseStrasse, AdresseWohnort, Fuehrerscheinnummer, Fuehrerscheinklasse, Telefonnummer, Email, Passwort) 
               VALUES (:1, :2, TO_DATE(:3, 'DD-MM-YYYY'), :4, :5, :6, :7, :8, :9, :10, :11)"""
    cursor.execute(query, (vorname, nachname, geburtsdatum, adresse_plz, adresse_strasse, adresse_wohnort, fuehrerscheinnummer, fuehrerscheinklasse, telefonnummer, email, passwort))

    conn.commit()
    conn.close()


def get_kunden():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Kunden")
    kunden = cursor.fetchall()

    conn.close()
    return kunden


def update_kunde(kunde_id, vorname, nachname, geburtsdatum, adresse_plz, adresse_strasse, adresse_wohnort, fuehrerscheinnummer, fuehrerscheinklasse, telefonnummer, email, passwort):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """UPDATE Kunden 
               SET Vorname = :1, Nachname = :2, Geburtsdatum = :3, AdressePLZ = :4, AdresseStrasse = :5, AdresseWohnort = :6, Fuehrerscheinnummer = :7, Fuehrerscheinklasse = :8, Telefonnummer = :9, Email = :10, Passwort = :11 
               WHERE KundenID = :12"""
    cursor.execute(query, (vorname, nachname, geburtsdatum, adresse_plz, adresse_strasse, adresse_wohnort, fuehrerscheinnummer, fuehrerscheinklasse, telefonnummer, email, passwort, kunde_id))

    conn.commit()
    conn.close()


def delete_kunde(kunde_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Kunden WHERE KundenID = :1", (kunde_id,))

    conn.commit()
    conn.close()


def populate_kunden():
    kunden = [
        ("Max", "Mustermann", "01-01-1990", 12345, "Musterstraße 1", "Musterstadt", 987654321, "Klasse B", "17612345", "max@example.com", "Khjdn23"),
        ("Anna", "Musterfrau", "15-02-1985", 67890, "Beispielweg 2", "Beispielstadt", 123456789, "Klasse A", "175382038", "anna@example.com", "NSK34k"),
        ("Peter", "Test", "20-03-1992", 54321, "Musterweg 3", "Musterort", 12344321, "Klasse C", "178391938" , "peter@example.com", "NKLK49j"),
        ("Maria", "Beispiel", "10-04-1988", 98765, "Beispielstraße 4", "Beispielort", 567890123, "123456", "Klasse B", "maria@example.com", "khsdjK3"),
        ("Thomas", "Tester", "05-05-1995", 13579, "Testweg 5", "Teststadt", 432109876, "Klasse A", "176492", "thomas@example.com", "Kkdn3k223")
    ]
    for kunde in kunden:
        add_kunde(*kunde)

def authenticate_kunde(email, passwort):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = "SELECT * FROM Kunden WHERE Email = :1 AND Passwort = :2"
    cursor.execute(query, (email, passwort))
    kunde = cursor.fetchone()

    conn.close()
    return kunde