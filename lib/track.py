class Track:
    def __init__(self, id, title, artist_id, album_id):
        self.id = id
        self.title = title
        self.artist_id = artist_id
        self.album_id = album_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Track({self.id}, {self.title}, {self.artist_id}, {self.album_id})"
