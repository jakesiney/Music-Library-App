from lib.track_repository import TrackRepository
from lib.track import Track

"""
When I call all on songs it returns all the songs in the db.
"""


def test_all_tracks(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = TrackRepository(db_connection)
    assert repository.all() == [
        Track(1, "A Track", 1, 1),
        Track(2, "Another Track", 2, 2),
        Track(3, "A Third Track", 3, 3),
        Track(4, "A Fourth Track", 4, 4)
    ]


"""
When I create a track it returns all songs.
"""


def test_create_track(db_connection):
    db_connection.seed("seeds/music_app.sql")
    repository = TrackRepository(db_connection)
    track = Track(None, 'New Track', 3, 3)
    repository.create(Track)
    assert repository.all() == [
        Track(1, "A Track", 1, 1),
        Track(2, "Another Track", 2, 2),
        Track(3, "A Third Track", 3, 3),
        Track(4, "A Fourth Track", 4, 4),
        Track(5, "New Track", 3, 3)
    ]
