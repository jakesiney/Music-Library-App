from lib.artist import Artist

"""
When creating an artist object, should return nothing.
"""


def test_create_artist_object():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"


def test_equal_artist():
    artist_1 = Artist(1, "Test", "Genre")
    artist_2 = Artist(1, "Test", "Genre")
    assert artist_1 == artist_2
