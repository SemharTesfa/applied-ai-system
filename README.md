
# Applied AI Music Recommendation System

## Project Overview

This project extends a Module 3 Music Recommender Simulation
into an end-to-end, retrieval-enhanced recommendation system.

The application recommends songs based on user preferences,
including genre, mood, energy, valence, and tempo.

It uses a deterministic scoring algorithm rather than a
trained machine learning model.

The enhanced system includes:
- Input validation and guardrails
- Song retrieval
- Weighted recommendation scoring
- Recommendation explanations
- Logging and error handling
- Automated reliability tests
- Evaluation documentation

## Original Project

The original Module 3 project was a Python-based music
recommendation simulation.

It loaded a local CSV dataset, compared song attributes
with user preferences, calculated weighted similarity
scores, and ranked recommendations.

The final project adds retrieval, validation, logging,
automated testing, and reliability evaluation.

## System Architecture

User Preferences
    |
    v
Input Validation
    |
    v
Song Retrieval
    |
    v
Weighted Scoring
    |
    v
Ranking and Explanations
    |
    v
Recommendation Results
    |
    v
Logging and Evaluation

Architecture diagram source:
`diagrams/architecture.mmd`

## Technology Stack

- Python 3
- Pytest
- CSV dataset
- Python logging
- Git and GitHub
- VS Code

## Project Structure

```text
applied-ai-system/
├── assets/
├── data/
│   └── songs.csv
├── diagrams/
│   └── architecture.mmd
├── logs/
│   └── test_results.txt
├── src/
│   ├── main.py
│   ├── recommender.py
│   ├── retriever.py
│   └── validator.py
├── tests/
│   ├── test_recommender.py
│   ├── test_retriever.py
│   └── test_validator.py
├── evaluation_results.md
├── model_card.md
├── ai_interactions.md
├── README.md
└── requirements.txt
```

The application also uses `src/logger.py` to configure
execution logging.

## Installation

Clone the repository:

```powershell
git clone https://github.com/SemharTesfa/applied-ai-system.git
cd applied-ai-system
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Running the Application

Run the command-line demonstration:

```powershell
python -m src.main
```

The application loads the song dataset and generates
recommendations for predefined user profiles.

## Example Recommendation Profiles

### Example 1: High-Energy Pop

Input preferences:

```python
{
    "genre": "pop",
    "mood": "happy",
    "energy": 0.90,
    "valence": 0.85,
    "tempo_bpm": 130
}
```

Previously observed top recommendation:
Sunrise City

### Example 2: Chill Lofi

Input preferences:

```python
{
    "genre": "lofi",
    "mood": "chill",
    "energy": 0.35,
    "valence": 0.60,
    "tempo_bpm": 75
}
```

Previously observed top recommendation:
Library Rain

### Example 3: Intense Rock

Input preferences:

```python
{
    "genre": "rock",
    "mood": "intense",
    "energy": 0.95,
    "valence": 0.45,
    "tempo_bpm": 155
}
```

Previously observed top recommendation:
Storm Runner

Note: These examples were observed before the latest
retrieval update. Run the application to confirm current
ranking results.

## Recommendation Method

The system uses weighted similarity scoring.

Features include:
- Genre matching
- Mood matching
- Energy similarity
- Valence similarity
- Tempo similarity

Songs are scored and sorted in descending order.

The system also produces explanations describing
the features contributing to each recommendation.

## Input Validation

The validator checks:
- Empty preferences
- Invalid genre and mood values
- Energy outside the allowed range
- Valence outside the allowed range
- Invalid tempo
- Invalid recommendation count

Invalid inputs raise ValueError exceptions.

## Reliability Testing

Run all automated tests:

```powershell
python -m pytest tests -v
```

Save test evidence:

```powershell
python -m pytest tests -v *> logs\test_results.txt
```

The project includes tests for recommendation behavior,
retrieval, validation, and integration.

The final passing test count should be recorded from
the actual pytest output.

See `evaluation_results.md` for the evaluation findings.

## Logging

The application records:
- Recommendation requests
- Candidate retrieval counts
- Number of results generated
- Input validation warnings

Logs are written to:

`logs/recommendations.log`

## Limitations

- Small dataset of 20 songs
- No trained machine learning model
- No collaborative filtering
- Limited genre and mood diversity
- No learning from user feedback
- Recommendation quality has not been validated through
  a formal user study

## Design Tradeoffs

A deterministic scoring algorithm was selected because
it is transparent, easy to test, and produces explainable
results.

A local CSV dataset was selected to keep the application
reproducible without requiring external API access.

The command-line interface was retained to prioritize
system reliability and evaluation over UI development.

## Future Improvements

1. Expand the dataset.
2. Add user feedback and personalized ranking.
3. Introduce embedding-based semantic retrieval.
4. Evaluate ranking quality using relevance judgments.
5. Add monitoring for recommendation performance.

## AI Collaboration

AI assistance was used to support system design,
implementation, debugging, and documentation.

Generated suggestions were reviewed and tested rather
than accepted without verification.

See `ai_interactions.md` for the detailed interaction log.

## Conclusion

The final project demonstrates how a basic recommendation
simulation can be extended into a more reliable and
explainable application through retrieval, validation,
logging, testing, and documented evaluation.
