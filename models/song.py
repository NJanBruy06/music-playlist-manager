import uuid

class Song:
    def __init__(self, title, artist, duration, genre="Unknown", year=2024):
        self.song_id = str(uuid.uuid4())
        self.title    = title
        self.artist   = artist
        self.duration = duration
        self.genre    = genre
        self.year     = year

    def duration_str(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes}:{seconds:02d}"

    def __repr__(self):
        return (f"Song(title='{self.title}', artist='{self.artist}', "
                f"duration='{self.duration_str()}', genre='{self.genre}', "
                f"year={self.year})")

    def __eq__(self, other):
        if not isinstance(other, Song):
            return False
        return self.song_id == other.song_id

    def __str__(self):
        return f"{self.title} — {self.artist} [{self.duration_str()}]"
