# flake8: noqa:E501
from flask import Flask
from Database.database import setup_database
from Fahrzeuge.routes import fahrzeuge_bp
from Kunden.routes import kunden_bp
from Mitarbeiter.routes import mitarbeiter_bp
from Rechnungen.routes import rechnungen_bp
from Reservierungen.routes import reservierungen_bp
from Standorte.routes import standorte_bp
from Wartungen.routes import wartungen_bp
from Fahrzeuge.fahrzeuge import populate_vehicles
from Kunden.kunden import populate_kunden
from Mitarbeiter.mitarbeiter import populate_mitarbeiter
from Rechnungen.rechnungen import populate_rechnungen
from Reservierungen.reservierungen import populate_reservierungen
from Standorte.standorte import populate_standorte
from Wartungen.wartungen import populate_wartungen

app = Flask(__name__)

app.register_blueprint(fahrzeuge_bp, url_prefix='/fahrzeuge')
app.register_blueprint(kunden_bp, url_prefix='/kunden')
app.register_blueprint(mitarbeiter_bp, url_prefix='/mitarbeiter')
app.register_blueprint(rechnungen_bp, url_prefix='/rechnungen')
app.register_blueprint(reservierungen_bp, url_prefix='/reservierungen')
app.register_blueprint(standorte_bp, url_prefix='/standorte')
app.register_blueprint(wartungen_bp, url_prefix='/wartungen')


def main():
    setup_database()
    populate_mitarbeiter()
    populate_standorte()
    populate_vehicles()
    populate_kunden()
    populate_reservierungen()
    populate_rechnungen()
    populate_wartungen()

    app.run(debug=False)


if __name__ == "__main__":
    main()
