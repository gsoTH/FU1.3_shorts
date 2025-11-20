# Shorts

:dart: Ziele:
 - Einen besseren Namen für diese Lernsituation finden
 - Implementierung und Test mit [FastAPI](https://fastapi.tiangolo.com/)
 - Kennenlerenen der [BestPractices für Namenskonventionen](https://dev.to/msnmongare/best-practices-for-naming-api-endpoints-2n5o)

:no_entry: Abgrenzungen:
 - Keine Authentifizierung
 - Kein Frontend (FU1 interessiert sich nur für JSON ;) )

:clipboard: Wissenlücken
 - Notieren Sie an dieser Stelle stichpunktartig Ihre Wissenslücken

## Auszug aus dem Lastenheft
### Beschreibung des Ist-Zustands
Youtube hat ~~Innovation betrieben~~ es der Konkurrenz nachgemacht und Kurzvideos, sogenannte shorts, implementiert. Leider gibt es keine gute Funktion zum speichern, kategorisieren und organisieren der shorts. 

Um Abhilfe zu schaffen wurde bereits eine Datenbank entwickelt, die mit einer einfachen GUI bedient werden kann. Die GUI wird gestartet, indem man das Modul gui.py ausführt.

### Beschreibung des Soll-Zustands
Um die App nicht nur lokal nutzen zu können, sollen die bereits vorhandenen Funktionen über eine REST-API aufgerufen werden können. Die GUI soll lokal weiterhin funktionieren.

Ist das erreicht, sollen weitere Funktionen implementiert werden, um Shorts mit Kategorien zu versehen und sie in Playlists zu organisieren.

### technische Rahmenbedingungen
- Die API soll mit [FastAPI](https://fastapi.tiangolo.com/) implementiert werden.
- Einhaltung der [BestPractices für Namenskonventionen](https://dev.to/msnmongare/best-practices-for-naming-api-endpoints-2n5o)
- Möglichst hohe Testabdeckung
