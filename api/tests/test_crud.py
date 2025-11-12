# Diese Datei beinhaltet Unit-Tests für die Funktionen (Units) in 
# der Datei ../crud.py.

from api.crud import create_short, read_short, read_short_random, delete_short
from api.database import get_connection, create_example_database
import pytest


@pytest.fixture
def create_fresh_database():
    con = get_connection()
    create_example_database(con)


def test_create_short__neuer_short_bekommt_id(create_fresh_database):
    # Arrange
    url = "https://www.youtube.com/shorts/Ny5vjwA-3hU"
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
    assert url[0] == 'https://youtube.com/shorts/dxqjrVuDLEo?si=mwWakcrMmgBA8vVe'


def test_read_short_random__short_wird_ausgegeben(create_fresh_database):
    ## Ein Test auf Zufälligkeit ist schwierig, da der Test
    ## Zufällig fehlschlagen könnte.
    
    # Act
    url = read_short_random()
    # Assert
    assert type(url[0]) is str


def test_delete_short__short_wird_entfernt(create_fresh_database):
    # Arrange
    id = 1
    # Act
    success: bool = delete_short(id)
    # Assert
    assert success == True
