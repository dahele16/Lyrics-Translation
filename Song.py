class Song:
    def __init__(self,id, title, artist, lyrics_path, picture_path) :
        self.id = id
        self.title = title
        self.artist = artist
        self.artist = artist
        self.lyrics_path = lyrics_path
        self.picture_path = picture_path


    def __str__(self) :
        return f"title: {self.title} artist: {self.artist} lyrics_path: {self.lyrics_path} picture_path: {self.picture_path}"