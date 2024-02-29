# flake8: noqa:E501

from Database.database import connect_to_database


def add_reservierung(kilometerstand, startdatum, enddatum, status, fahrzeug_id, kunden_id, mitarbeiter_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = """INSERT INTO Reservierungen (Kilometerstand, StartDatum, EndDatum, Status, FahrzeugID, KundenID, MitarbeiterID) 
               VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7)"""
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


def check_if_vehicle_is_reserved(start_date, end_date, vehicle_id):
    """
    Checks if a vehicle is reserved for a specific date range.

    Parameters:
        start_date (str): The start date of the range to check.
        end_date (str): The end date of the range to check.
        vehicle_id (int): The ID of the vehicle to check.

    Returns:
        bool: True if the vehicle is reserved for any date within the range, False otherwise.
    """
    # Connect to the database
    conn = connect_to_database()
    cursor = conn.cursor()

    # Define the SQL statement to check the reservation
    query = "SELECT * FROM Reservierungen WHERE FahrzeugID = :1 AND ((StartDatum BETWEEN :2 AND :3) OR (EndDatum BETWEEN :2 AND :3))"

    # Execute the SQL statement, replacing :1 with `vehicle_id`, :2 with `start_date`, and :3 with `end_date`
    cursor.execute(query, (vehicle_id, start_date, end_date))

    # Fetch the results
    results = cursor.fetchall()

    # Close the database connection
    conn.close()

    return len(results) > 0

def get_reservations_for_user(user_id):
    """
    Fetches all reservations for a specific user from the database.

    Parameters:
        user_id (int): The ID of the user.

    Returns:
        list: A list of all reservations for the user.
    """
    # Connect to the database
    conn = connect_to_database()
    cursor = conn.cursor()

    # Define the SQL statement to fetch the reservations
    query = "SELECT * FROM Reservierungen WHERE KundenID = :1"


    # Execute the SQL statement, replacing :1 with `user_id`
    cursor.execute(query, (user_id,))

    # Fetch the results
    results = cursor.fetchall()

    reservations = [
        {
            'id': row[0],
            'start_date': row[2],
            'end_date': row[3],
            'vehicle_id': row[4]
        }
        for row in results
    ]

    # Close the database connection
    conn.close()

    return reservations