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
        # Album(3, "New Album", 2023, 2)
    ]


"""
Creating an album in the db returns all albums.
"""


def test_create_album(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = AlbumRepository(db_connection)
    repository.create(Album(None, 'New Album', 2023, 3))

    assert repository.all() == [
        Album(1, "An Album", 2023, 1),
        Album(2, "Another Album", 1999, 2),
        Album(3, "New Album", 2023, 3)
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
