from lib.track import Track

"""
When creating a track object, should return nothing.
"""


def test_create_track_object():
    track = Track(1, "Test Track", 1, 1)
    assert track.id == 1
    assert track.title == "Test Track"
    assert track.artist_id == 1
    assert track.album_id == 1
