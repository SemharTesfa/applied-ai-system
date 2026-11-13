
# Reliability Evaluation Report

## Project
Applied AI Music Recommendation System

## Evaluation Objective
Evaluate whether the system can retrieve, score, rank, and
explain music recommendations while rejecting invalid inputs.

## System Architecture
1. User preferences
2. Input validation
3. Song retrieval
4. Recommendation scoring
5. Ranking and explanations
6. Logging and error handling

## Dataset
- Source: Local CSV dataset
- Total songs: 20
- Features: genre, mood, energy, tempo, valence,
  danceability, and acousticness

## Functional Evaluation

| Test Profile | Candidates Retrieved | Results Returned | Status |
|---|---:|---:|---|
| High-Energy Pop | 3 | 3 | Completed |
| Chill Lofi | 4 | 4 | Completed |
| Intense Rock | 2 | 2 | Completed |
| Sad but Energetic | 1 | 1 | Completed |

Source: Application log from November 13, 2026.

## Input Validation

The system includes validation for:
- Empty user preferences
- Invalid genre or mood values
- Energy outside the 0–1 range
- Valence outside the 0–1 range
- Invalid tempo values
- Invalid recommendation count
- Empty song datasets

Invalid preferences raise ValueError exceptions.

## Automated Testing

Tests cover:
- Original recommender functionality
- Song retrieval
- Input validation
- Integration between retrieval and recommendation

Test command:
python -m pytest tests -v

Test evidence:
logs/test_results.txt

Final test count and pass/fail results:
Pending confirmation from saved pytest output.

## Reliability Findings

### Finding 1: Retrieval reduces the candidate pool
The retriever selects songs matching the user's genre or mood.

### Finding 2: Some profiles receive fewer recommendations
The Sad but Energetic profile returned only one song.

This is a limitation because the retriever currently does not
expand the candidate pool when too few songs match.

### Finding 3: Logging provides execution visibility
The system records recommendation requests, candidate counts,
result counts, and input validation warnings.

## Limitations
- Small dataset of 20 songs
- Rule-based scoring rather than a trained ML model
- Limited genre and mood coverage
- No collaborative filtering or user feedback learning
- Retrieval may return fewer than the requested number of songs

## Future Improvements
1. Add retrieval fallback when fewer than k candidates match.
2. Expand the music dataset.
3. Introduce user feedback to improve ranking.
4. Add more automated edge-case tests.
5. Evaluate recommendation relevance using human ratings.

## Conclusion
The observed application runs successfully generated recommendations
for four test profiles, and logging captured candidate and result
counts. Automated test results must be confirmed separately before
claiming that all tests passed.
