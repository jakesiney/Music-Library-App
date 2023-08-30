from lib.artist import Artist
from lib.artist_repository import ArtistRepository


def test_get_all_artists(db_connection):
    repo = ArtistRepository(db_connection)
    assert repo.all() == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz")
    ]


def test_find_artist_by_id(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = ArtistRepository(db_connection)
    assert repository.find_artist(1) == Artist(1, "Pixies", "Rock")


def test_delete_an_artist(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = ArtistRepository(db_connection)
    repository.delete_artist(1)
    assert repository.all() == [
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz")
    ]
