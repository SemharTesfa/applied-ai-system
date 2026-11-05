"""
Command line runner for the Music Recommender Simulation.

Evaluates the recommender against four user profiles and prints the top
five results for each one in plain text that can be pasted into Markdown
fenced code blocks.
"""

try:
    from .recommender import load_songs, recommend_songs  # python -m src.main
except ImportError:
    from recommender import load_songs, recommend_songs  # python src/main.py


PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.90,
        "valence": 0.85,
        "tempo_bpm": 130,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "valence": 0.60,
        "tempo_bpm": 75,
    },
    "Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.95,
        "valence": 0.45,
        "tempo_bpm": 155,
    },
    "Sad but Energetic": {
        "genre": "blues",
        "mood": "sad",
        "energy": 0.90,
        "valence": 0.20,
        "tempo_bpm": 145,
    },
}

K = 5
WIDTH = 72


def format_profile(prefs: dict) -> str:
    return (
        f"genre={prefs['genre']}, mood={prefs['mood']}, "
        f"energy={prefs['energy']:.2f}, valence={prefs['valence']:.2f}, "
        f"tempo={prefs['tempo_bpm']} BPM"
    )


def print_profile_results(name: str, prefs: dict, songs: list) -> None:
    recommendations = recommend_songs(prefs, songs, k=K)

    print("=" * WIDTH)
    print(f"Profile: {name}")
    print(f"Preferences: {format_profile(prefs)}")
    print("=" * WIDTH)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} - {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Why:")
        for reason in explanation.split("; "):
            print(f"     - {reason}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}\n")

    for name, prefs in PROFILES.items():
        print_profile_results(name, prefs, songs)


if __name__ == "__main__":
    main()
