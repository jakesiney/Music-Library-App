from lib.album import Album


def test_album_object():
    album = Album(1, "Title", 2023, 1)
    assert album.id == 1
    assert album.title == 'Title'
    assert album.release_year == 2023
    assert album.artist_id == 1


def test_equal():
    album_1 = Album(1, "Test", 2000, 2)
    album_2 = Album(1, "Test", 2000, 2)
    assert album_1 == album_2
