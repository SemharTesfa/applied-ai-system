
import logging
from pathlib import Path


def setup_logger():
    """Configure logging for the recommendation system."""

    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    logger = logging.getLogger("music_recommender")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(
            log_directory / "recommendations.log",
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


logger = setup_logger()
