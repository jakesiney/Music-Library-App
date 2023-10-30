from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When I call all on albums
returns all the albums in the db.
"""


def test_all_albums(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "An Album", 2023, 1),
        Album(2, "Another Album", 1999, 2),
        Album(3, "A Third Album", 2000, 3),
        Album(4, "A Fourth Album", 2001, 4)
    ]


"""
Creating an album in the db returns all albums.
"""


def test_create_album(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'New Album', 2023, 3)
    repository.create(album)
    assert repository.all() == [
        Album(1, "An Album", 2023, 1),
        Album(2, "Another Album", 1999, 2),
        Album(3, "A Third Album", 2000, 3),
        Album(4, "A Fourth Album", 2001, 4),
        Album(5, "New Album", 2023, 3)
    ]


"""
Testing finding an album by id
"""


def test_find_album_by_id(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find_album(1) == Album(1, "An Album", 2023, 1)


def test_find_album_by_id_two(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find_album(2) == Album(2, "Another Album", 1999, 2)


"""
Testing delete an album
"""


def test_delete_an_album(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = AlbumRepository(db_connection)
    repository.delete_album(1)
    assert repository.all() == [
        Album(2, "Another Album", 1999, 2),
        Album(3, "A Third Album", 2000, 3),
        Album(4, "A Fourth Album", 2001, 4)
    ]


"""
Testing get albums by artist id
"""


def test_get_albums_by_artist_id(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = AlbumRepository(db_connection)
    assert repository.get_albums_by_artist_id(1) == [
        Album(1, "An Album", 2023, 1)
    ]
