
from typing import Dict, List


class SongRetriever:
    def __init__(self, songs: List[Dict]):
        self.songs = songs

    def retrieve(
        self,
        user_prefs: Dict,
        max_candidates: int = 10
    ) -> List[Dict]:

        if isinstance(max_candidates, bool) or not isinstance(max_candidates, int) or max_candidates <= 0:
            raise ValueError("max_candidates must be positive")

        genre = user_prefs.get("genre")
        mood = user_prefs.get("mood")

        matching_songs = []
        other_songs = []

        for song in self.songs:
            if (
                (genre and song["genre"] == genre)
                or (mood and song["mood"] == mood)
            ):
                matching_songs.append(song)
            else:
                other_songs.append(song)

        # Prioritize matching songs, then fill with others.
        candidates = matching_songs + other_songs

        return candidates[:max_candidates]
