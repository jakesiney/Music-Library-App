from lib.song import Song

"""
When creating a song object, should return nothing.
"""


def test_create_song_object():
    song = Song(1, "Test Song", 1, 1)
    assert song.id == 1
    assert song.title == "Test Song"
    assert song.artist_id == 1
    assert song.album_id == 1
