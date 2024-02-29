# flake8: noqa:E501

import json
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_13")
from Database.sql_statements import get_create_table_statements, get_alter_table_statements


# Verbindet sich mit der Datenbank, indem die Konfiguration aus einer JSON-Datei gelesen wird.
def connect_to_database():
    # Öffnet die Konfigurationsdatei, um die Verbindungsdetails zu erhalten.

    
    # Liest die Benutzer-, Passwort-, Host-, Port- und Servicenamen aus der Konfigurationsdatei.
    user = 'Vermietung'
    password = 'Gruppe4'
    host = 'h2922093.stratoserver.net'
    port = '1521'
    service_name = 'orcl.stratoserver.net'
    
    # Erstellt einen DSN (Data Source Name) für die Oracle-Datenbankverbindung.
    dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)
    # Stellt die Verbindung zur Datenbank her und gibt das Verbindungsobjekt zurück.
    return cx_Oracle.connect(user=user, password=password, dsn=dsn_tns)

# Führt SQL-Anweisungen innerhalb einer Transaktion (Sequenz von ein oder mehreren Datenbankoperationen, die als eine einzige logische Einheit der Arbeit behandelt werden) aus.
def execute_sql_in_transaction(connection, statements):
    try:
        # Erstellt einen Cursor (Steuerelement, das verwendet wird, um durch die Zeilen eines Ergebnissets aus einer Datenbankabfrage zu iterieren. Er ermöglicht es, Datensätze aus der Datenbank zeilenweise zu bearbeiten oder zu lesen, statt das gesamte Ergebnisset auf einmal in den Speicher zu laden.) für die Verbindung, um SQL-Anweisungen auszuführen.
        with connection.cursor() as cursor:
            for sql in statements:
                cursor.execute(sql)  # Führt jede SQL-Anweisung aus.
        connection.commit()  # Bestätigt die Transaktion, wenn alle Anweisungen erfolgreich waren.
    except cx_Oracle.DatabaseError as e:
        connection.rollback()  # Macht Änderungen rückgängig, wenn ein Fehler auftritt.
        print(f"Fehler bei der Ausführung von SQL: {sql}")
        print(f"Oracle-Error: {e}")

# Richtet die Datenbank ein, indem Tabellen erstellt und modifiziert werden.
def setup_database():
    conn = connect_to_database()  # Stellt eine Verbindung zur Datenbank her.

    try:
        conn.begin()  # Startet eine Transaktion.

        # Ruft die SQL-Anweisungen zum Erstellen von Tabellen ab und führt sie aus.
        create_table_statements = get_create_table_statements()
        for statement in create_table_statements:
            execute_sql_in_transaction(conn, [statement])

        # Ruft die SQL-Anweisungen zum Ändern von Tabellen ab und führt sie aus.
        alter_table_statements = get_alter_table_statements()
        for statement in alter_table_statements:
            execute_sql_in_transaction(conn, [statement])

        conn.commit()  # Bestätigt die Transaktion, wenn alle Anweisungen erfolgreich waren.

    except cx_Oracle.DatabaseError as e:
        conn.rollback()  # Macht Änderungen rückgängig, wenn ein Fehler auftritt.
        print(f"Verbindungsfehler: {e}")

    finally:
        conn.close()  # Schließt die Datenbankverbindung.