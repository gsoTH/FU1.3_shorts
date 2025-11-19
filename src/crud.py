#  Hier liegen Hilfsfunktionen zur Kommunikation mit der Datenbank.
#
# CRUD steht für Create, Read, Update und Delete, den vier grundlegenden
# Operationen einer Datenbank.

import database

def create_short(url: str) -> int:
    """ Fügt einen neuen Short-Link in die Datenbank ein. """
    con = database.get_connection()
    c = con.cursor()
    c.execute("INSERT INTO shorts (url) VALUES (?)", (url,))
    con.commit()
    id = c.lastrowid
    con.close()
    return id

def read_short(id: int) -> str:
    """ Holt einen bestimmten Short-Link aus der Datenbank. """
    con = database.get_connection()
    c = con.cursor()
    c.execute("SELECT url FROM shorts WHERE id = ?", (id,))
    url:list[str] = c.fetchone()
    con.close()
    return url[0]


def read_all() -> list[str]:
    """ Holt alle Short-Links aus der Datenbank. """
    con = database.get_connection()
    c = con.cursor()
    c.execute("SELECT url FROM shorts")
    url = c.fetchall()
    con.close()
    return url


def read_short_random() -> str:
    """ Holt einen zufälligen Short-Link aus der Datenbank. """
    con = database.get_connection()
    c = con.cursor()
    c.execute("SELECT url FROM shorts ORDER BY RANDOM() LIMIT 1")
    url = c.fetchone()
    con.close()
    return url[0]

def delete_short(id: int) -> bool:
    """ Löscht einen Short-Link aus der Datenbank. """
    con = database.get_connection()
    c = con.cursor()
    c.execute("DELETE FROM shorts WHERE id = ?", (id,))
    con.commit()
    con.close()
    return True


if __name__ == "__main__":
    pass