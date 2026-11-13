
import math


def validate_preferences(user_prefs):
    """
    Validate user preferences before generating
    music recommendations.

    Returns validated preferences or raises ValueError.
    """
    if not isinstance(user_prefs, dict):
        raise ValueError("User preferences must be a dictionary.")

    if not user_prefs:
        raise ValueError("User preferences cannot be empty.")

    for key in ("genre", "mood"):
        if key in user_prefs:
            value = user_prefs[key]
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{key} must be a non-empty string.")

    for key in ("energy", "valence"):
        if key in user_prefs:
            value = user_prefs[key]

            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or not 0 <= value <= 1
            ):
                raise ValueError(
                    f"{key} must be a number between 0 and 1."
                )

    if "tempo_bpm" in user_prefs:
        tempo = user_prefs["tempo_bpm"]

        if (
            isinstance(tempo, bool)
            or not isinstance(tempo, (int, float))
            or not math.isfinite(tempo)
            or tempo <= 0
        ):
            raise ValueError(
                "tempo_bpm must be a positive number."
            )

    return user_prefs
