from lib.track import Track


class TrackRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from tracks')
        tracks = []
        for row in rows:
            item = Track(row["id"], row["title"],
                         row["artist_id"], row["album_id"])
            tracks.append(item)
        return tracks

    def create(self, track):
        rows = self._connection.execute('INSERT INTO tracks (title, artist_id, album_id) VALUES (%s, %s, %s) RETURNING id', [
            track.title, track.artist_id, track.album_id])
        track.id = rows[0]['id']
        return None

    def find_track(self, id):
        rows = self._connection.execute(
            'SELECT * from tracks WHERE id = %s', [id])
        row = rows[0]
        return Track(row["id"], row["title"], row["artist_id"], row["album_id"])

    def delete_track(self, song_id):
        self._connection.execute(
            'DELETE FROM tracks WHERE id = %s', [song_id])
        return None

    def find_track_by_artist(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from tracks WHERE artist_id = %s', [artist_id])
        tracks = []
        for row in rows:
            item = Track(row["id"], row["title"],
                         row["artist_id"], row["album_id"])
            tracks.append(item)
        return tracks

    def find_tracks_by_album(self, album_id):
        rows = self._connection.execute(
            'SELECT * from tracks WHERE album_id = %s', [album_id])
        tracks = []
        for row in rows:
            item = Track(row["id"], row["title"],
                         row["artist_id"], row["album_id"])
            tracks.append(item)
        return tracks

    def find_tracks_by_artist_and_album(self, artist_id, album_id):
        rows = self._connection.execute(
            'SELECT * from tracks WHERE artist_id = %s AND album_id = %s', [artist_id, album_id])
        tracks = []
        for row in rows:
            item = Track(row["id"], row["title"],
                         row["artist_id"], row["album_id"])
            tracks.append(item)
        return tracks
