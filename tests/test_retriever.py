
import pytest

from src.retriever import SongRetriever
from src.recommender import recommend_songs


# Sample dataset used for testing
@pytest.fixture
def sample_songs():
    return [
        {
            "id": 1,
            "title": "Rock Song",
            "artist": "Artist A",
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95,
            "valence": 0.40,
            "tempo_bpm": 150,
            "danceability": 0.65,
            "acousticness": 0.10,
        },
        {
            "id": 2,
            "title": "Pop Song",
            "artist": "Artist B",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.70,
            "valence": 0.80,
            "tempo_bpm": 120,
            "danceability": 0.85,
            "acousticness": 0.20,
        },
        {
            "id": 3,
            "title": "Lofi Song",
            "artist": "Artist C",
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.30,
            "valence": 0.60,
            "tempo_bpm": 75,
            "danceability": 0.50,
            "acousticness": 0.90,
        },
    ]


# Test 1: Matching genre songs are prioritized
def test_retriever_matches_genre(sample_songs):
    retriever = SongRetriever(sample_songs)

    results = retriever.retrieve(
        {"genre": "rock"},
        max_candidates=3
    )

    assert len(results) == 3
    assert results[0]["genre"] == "rock"
    assert len({song["id"] for song in results}) == 3


# Test 2: Matching mood songs are prioritized
def test_retriever_matches_mood(sample_songs):
    retriever = SongRetriever(sample_songs)

    results = retriever.retrieve(
        {"mood": "chill"},
        max_candidates=3
    )

    assert len(results) == 3
    assert results[0]["mood"] == "chill"


# Test 3: Fallback works when there are no matches
def test_retriever_fallback(sample_songs):
    retriever = SongRetriever(sample_songs)

    results = retriever.retrieve(
        {"genre": "jazz"},
        max_candidates=3
    )

    assert len(results) == 3
    assert results == sample_songs


# Test 4: Invalid candidate count is rejected
def test_invalid_max_candidates(sample_songs):
    retriever = SongRetriever(sample_songs)

    with pytest.raises(ValueError):
        retriever.retrieve(
            {"genre": "rock"},
            max_candidates=0
        )


# Test 5: Retrieval integrates with recommendation scoring
def test_retrieval_integrated_with_recommendations(sample_songs):
    preferences = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.95,
        "valence": 0.40,
        "tempo_bpm": 150,
    }

    results = recommend_songs(
        preferences,
        sample_songs,
        k=3
    )

    assert len(results) == 3

    # Highest-scoring song should match user preferences
    assert results[0][0]["title"] == "Rock Song"

    # Scores should be between 0 and 1
    assert all(
        0 <= score <= 1
        for _, score, _ in results
    )

    # Results should be ranked from highest to lowest
    scores = [score for _, score, _ in results]

    assert scores == sorted(scores, reverse=True)

    # Each recommendation should include an explanation
    assert all(
        isinstance(explanation, str) and explanation
        for _, _, explanation in results
    )
