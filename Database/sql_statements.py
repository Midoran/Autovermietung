# flake8: noqa:E501

def get_create_table_statements():
    
    # Gibt eine Liste von SQL CREATE TABLE-Anweisungen als Strings zurück.
    # Jede Anweisung in der Liste erstellt eine spezifische Tabelle in der Datenbank.

    return [
        """CREATE TABLE Standorte (
        StandortID NUMBER GENERATED BY DEFAULT AS IDENTITY,
        Standortname VARCHAR2(255) NOT NULL,
        AdressePLZ VARCHAR2(255) NOT NULL,
        AdresseStrasse VARCHAR2(255) NOT NULL,
        AdresseWohnort VARCHAR2(255) NOT NULL,
        AnzahlStellplatz NUMBER NOT NULL,
        PRIMARY KEY (StandortID)
        )""",

        """CREATE TABLE Fahrzeuge (
        FahrzeugID NUMBER GENERATED BY DEFAULT AS IDENTITY,
        StandortID NUMBER NOT NULL,
        Hersteller VARCHAR2(255) NOT NULL,
        Modell VARCHAR2(255) NOT NULL,
        Baujahr NUMBER,
        Verfuegbarkeit CHAR(1) NOT NULL,
        Preis FLOAT NOT NULL,
        Kilometerstand FLOAT NOT NULL,
        Kennzeichen VARCHAR2(255) NOT NULL,
        Fahrzeugklasse VARCHAR2(255) NOT NULL,
        Wartungsstatus VARCHAR2(255),
        PRIMARY KEY (FahrzeugID)
        )""",

        """CREATE TABLE Kunden (
        KundenID NUMBER GENERATED BY DEFAULT AS IDENTITY,
        Vorname VARCHAR2(255) NOT NULL,
        Nachname VARCHAR2(255) NOT NULL,
        Geburtsdatum DATE NOT NULL,
        AdressePLZ NUMBER NOT NULL,
        AdresseStrasse VARCHAR2(255) NOT NULL,
        AdresseWohnort VARCHAR2(255) NOT NULL,
        Fuehrerscheinnummer NUMBER NOT NULL,
        Fuehrerscheinklasse VARCHAR2(255) NOT NULL,
        Telefonnummer VARCHAR2(255) NOT NULL,
        Email VARCHAR2(255) NOT NULL,
        Passwort VARCHAR2(255) NOT NULL,
        PRIMARY KEY (KundenID)
        )""",

        """CREATE TABLE Mitarbeiter (
        MitarbeiterID NUMBER GENERATED BY DEFAULT AS IDENTITY,
        Vorname VARCHAR2(255) NOT NULL,
        Nachname VARCHAR2(255) NOT NULL,
        Position VARCHAR2(255) NOT NULL,
        Email VARCHAR2(255) NOT NULL,
        PRIMARY KEY (MitarbeiterID)
        )""",

        """CREATE TABLE Reservierungen (
        ReservierungsID NUMBER GENERATED BY DEFAULT AS IDENTITY,
        Kilometerstand FLOAT NOT NULL,
        StartDatum DATE NOT NULL,
        EndDatum DATE NOT NULL,
        Status CHAR(1) NOT NULL,
        FahrzeugID NUMBER NOT NULL,
        KundenID NUMBER NOT NULL,
        MitarbeiterID NUMBER NOT NULL,
        PRIMARY KEY (ReservierungsID)
        )""",

        """CREATE TABLE Rechnungen (
        RechnungID NUMBER GENERATED BY DEFAULT AS IDENTITY,
        Rechnungsdatum DATE NOT NULL,
        Rechnungsbetrag FLOAT NOT NULL,
        Status CHAR(1) NOT NULL,
        KundenID NUMBER NOT NULL,
        PRIMARY KEY (RechnungID)
        )""",

        """CREATE TABLE Wartungen (
        WartungsID NUMBER GENERATED BY DEFAULT AS IDENTITY,
        FahrzeugID NUMBER NOT NULL,
        Wartungsdatum DATE NOT NULL,
        Beschreibung VARCHAR2(1000),
        Bemerkungen VARCHAR2(1000),
        PRIMARY KEY (WartungsID)
        )"""
    ]


def get_alter_table_statements():
    
    # Gibt eine Liste von SQL ALTER TABLE-Anweisungen als Strings zurück.
    # Jede Anweisung fügt eine Fremdschlüsselbeziehung zwischen zwei Tabellen hinzu.

    return [
        """ALTER TABLE Fahrzeuge
        ADD FOREIGN KEY (StandortID) REFERENCES Standorte(StandortID)""",

        """ALTER TABLE Rechnungen
        ADD FOREIGN KEY (KundenID) REFERENCES Kunden(KundenID)""",

        """ALTER TABLE Reservierungen
        ADD FOREIGN KEY (KundenID) REFERENCES Kunden(KundenID)""",

        """ALTER TABLE Reservierungen
        ADD FOREIGN KEY (FahrzeugID) REFERENCES Fahrzeuge(FahrzeugID)""",

        """ALTER TABLE Reservierungen
        ADD FOREIGN KEY (MitarbeiterID) REFERENCES Mitarbeiter(MitarbeiterID)""",

        """ALTER TABLE Wartungen
        ADD FOREIGN KEY (FahrzeugID) REFERENCES Fahrzeuge(FahrzeugID)"""

    ]