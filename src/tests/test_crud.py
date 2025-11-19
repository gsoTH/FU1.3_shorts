# Diese Datei beinhaltet Unit-Tests für die Funktionen (Units) in 
# der Datei ../crud.py.

from src.crud import * #create_short, read_short, read_short_random, delete_short
import src.database as database
import pytest


@pytest.fixture
def create_fresh_database():
    con = database.get_connection()
    database.create_example_database(con)


def test_create_short__neuer_short_bekommt_id(create_fresh_database):
    # Arrange
    url = "https://youtube.com/shorts/0zfuSBmU4_s"
    # Act
    id = create_short(url)
    # Assert
    assert id == 5
 

def test_read_short__short_kann_abgerufen_werden(create_fresh_database):
    # Arrange
    id = 1
    # Act
    url = read_short(id)
    # Assert
    assert url == 'https://youtube.com/shorts/dxqjrVuDLEo?si=mwWakcrMmgBA8vVe'


def test_read_all__gibt_liste_an_shorts_aus(create_fresh_database):
    #Arrange
    #Act
    url:list[str] = read_all()
    #Assert
    assert isinstance(url,list)
    assert len(url) > 0


def test_read_short_random__short_wird_ausgegeben(create_fresh_database):
    # Act
    erste_url:str = read_short_random()
    #zweite_url:str = read_short_random()
    # Assert
    assert type(erste_url) is str
    #assert erste_url != zweite_url     # könnte zufällig fehlschlagen


def test_delete_short__short_wird_entfernt(create_fresh_database):
    # Arrange
    id = 1
    # Act
    success: bool = delete_short(id)
    # Assert
    assert success == True
