import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dicts with numeric fields converted."""
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["id"] = int(row["id"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            for key in ("energy", "valence", "danceability", "acousticness"):
                row[key] = float(row[key])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song 0-1 against user prefs and return (score, human-readable reasons)."""
    # EXPERIMENT: weight shift (original: genre 0.30, energy 0.20, divisor 1.00).
    # Each contribution is divided by NORMALIZER so explanations sum to the score.
    NORMALIZER = 1.05
    score = 0.0
    reasons: List[str] = []

    for key, weight in (("genre", 0.15), ("mood", 0.25)):
        if key in user_prefs and song[key] == user_prefs[key]:
            points = weight / NORMALIZER
            score += points
            reasons.append(f"{key} match: {song[key]} (+{points:.2f})")

    for key, weight in (("energy", 0.40), ("valence", 0.15)):
        if key in user_prefs:
            points = weight * (1 - abs(song[key] - user_prefs[key])) / NORMALIZER
            score += points
            reasons.append(
                f"{key} {song[key]:.2f} vs target {user_prefs[key]:.2f} (+{points:.2f})"
            )

    if "tempo_bpm" in user_prefs:
        points = 0.10 * max(0, 1 - abs(song["tempo_bpm"] - user_prefs["tempo_bpm"]) / 100) / NORMALIZER
        score += points
        reasons.append(
            f"tempo {song['tempo_bpm']} BPM vs target {user_prefs['tempo_bpm']} (+{points:.2f})"
        )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, rank by score (highest first), and return the top k as (song, score, explanation)."""
    results: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        results.append((song, score, "; ".join(reasons)))

    return sorted(results, key=lambda item: item[1], reverse=True)[:k]
