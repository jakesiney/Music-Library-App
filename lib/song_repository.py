from lib.song import Song


class Songs:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from songs')
        songs = []
        for row in rows:
            item = Song(row["id"], row["title"],
                        row["artist_id"], row["album_id"])
            songs.append(item)
        return songs

    def create(self, song):
        rows = self._connection.execute('INSERT INTO songs (title, artist_id, album_id) VALUES (%s, %s, %s) RETURNING id', [
            song.title, song.artist_id, song.album_id])
        song.id = rows[0]['id']
        return None

    def find_song(self, id):
        rows = self._connection.execute(
            'SELECT * from songs WHERE id = %s', [id])
        row = rows[0]
        return Song(row["id"], row["title"], row["artist_id"], row["album_id"])

    def delete_song(self, song_id):
        self._connection.execute(
            'DELETE FROM songs WHERE id = %s', [song_id])
        return None

    def find_songs_by_artist(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from songs WHERE artist_id = %s', [artist_id])
        songs = []
        for row in rows:
            item = Song(row["id"], row["title"],
                        row["artist_id"], row["album_id"])
            songs.append(item)
        return songs

    def find_songs_by_album(self, album_id):
        rows = self._connection.execute(
            'SELECT * from songs WHERE album_id = %s', [album_id])
        songs = []
        for row in rows:
            item = Song(row["id"], row["title"],
                        row["artist_id"], row["album_id"])
            songs.append(item)
        return songs

    def find_songs_by_artist_and_album(self, artist_id, album_id):
        rows = self._connection.execute(
            'SELECT * from songs WHERE artist_id = %s AND album_id = %s', [artist_id, album_id])
        songs = []
        for row in rows:
            item = Song(row["id"], row["title"],
                        row["artist_id"], row["album_id"])
            songs.append(item)
        return songs
