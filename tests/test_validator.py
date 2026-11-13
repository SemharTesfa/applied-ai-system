
import pytest

from src.validator import validate_preferences
from src.recommender import recommend_songs


def test_valid_preferences():
    prefs = {"genre": "rock", "energy": 0.9}
    assert validate_preferences(prefs) == prefs


def test_invalid_energy():
    with pytest.raises(ValueError):
        validate_preferences({"energy": 1.5})


def test_negative_energy():
    with pytest.raises(ValueError):
        validate_preferences({"energy": -0.2})


def test_invalid_valence():
    with pytest.raises(ValueError):
        validate_preferences({"valence": 2.0})


def test_negative_tempo():
    with pytest.raises(ValueError):
        validate_preferences({"tempo_bpm": -100})


def test_empty_preferences():
    with pytest.raises(ValueError):
        validate_preferences({})


def test_invalid_genre():
    with pytest.raises(ValueError):
        validate_preferences({"genre": ""})


def test_empty_dataset():
    results = recommend_songs(
        {"genre": "rock", "energy": 0.9},
        [],
        k=5
    )
    assert results == []


def test_invalid_recommendation_count():
    with pytest.raises(ValueError):
        recommend_songs({"genre": "rock"}, [], k=0)


def test_invalid_input_rejected_by_recommender():
    with pytest.raises(ValueError):
        recommend_songs({"energy": 1.5}, [], k=5)
