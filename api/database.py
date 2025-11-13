# Diese Datei kümmert sich um die Verbindung zur Datenbank. 
# Zum Erzeugen der Testdatenbank auf der Festplatte kann 
# dieses Skript ausgeführt werden.

import sqlite3
import os

relative_path_to_db: str = './shorts.sqlite'


def get_connection() -> sqlite3.Connection:
    """ Stellt eine Verbindung zur Datenbank her. """
    db_path:str = get_absolute_path(relative_path_to_db)
    con = sqlite3.connect(db_path)

    if database_is_empty(con):
        create_example_database(con)

    return con


def get_absolute_path(relative_path: str) -> str:
    """ Erstellt einen absoluten Pfad zur Datenbank, unabängig vom Betriebssystem. """
    # Abfragen, in welchem Verzeichnis dieses Skript liegt.
    scriptdir: str = os.path.dirname(__file__)

    # Beide Pfade zusammensetzen
    combined_path: str = os.path.join(scriptdir, relative_path)
    
    #print(combined_path)
    # --> C:\repos\flaskShowcase\datenbanken\db/example_db.sqlite

    # Pfad normalsieren (ans Betriebssystem anpassen)
    absolute_path = os.path.normcase(combined_path)
    
    #print(absolute_path)
    # --> c:\repos\flaskshowcase\datenbanken\db\example_db.sqlite

    return absolute_path


def database_is_empty(con: sqlite3.Connection) -> bool:
    """ Prüft, ob Tabellen in der Datenbank vorhanden sind. """
    c :sqlite3.Cursor = con.cursor()
    statement :str = "SELECT name FROM sqlite_master WHERE type='table';"
    c.execute(statement)
    if c.fetchone() is None:
        return True
    return False
    


def create_example_database(con: sqlite3.Connection) -> None:
    """ Erstellt Beispiel-Daten in der Datenbank. """
    drop_statement: str = "DROP TABLE IF EXISTS shorts;"
    con.execute(drop_statement)

    create_statement :str = """CREATE TABLE shorts (
                            id          INTEGER
                        ,   url         TEXT UNIQUE
                        ,   PRIMARY KEY (id)
                        );"""
    con.execute(create_statement)

    insert_statement = """INSERT INTO shorts (url) VALUES
                            ('https://youtube.com/shorts/dxqjrVuDLEo?si=mwWakcrMmgBA8vVe')
                        ,   ('https://www.youtube.com/shorts/8K_YqT16pYk')
                        ,   ('https://youtube.com/shorts/NZtfn2lj4Fs')
                        ,   ('https://youtube.com/shorts/TIP11RKLo80')
                        ;"""
    con.execute(insert_statement)

    con.commit()


if __name__ == "__main__":  
    con: sqlite3.Connection  = get_connection()
    print(con.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
    con.close()