
# Model Card: Applied AI Music Recommendation System

## 1. System Overview

**System Name:** Applied AI Music Recommendation System

**System Type:** Retrieval-enhanced, rule-based recommendation system

**Programming Language:** Python

**Dataset:** Local CSV containing 20 songs

**Interface:** Command-line application

### Purpose

The system recommends songs based on user preferences,
including genre, mood, energy, valence, and tempo.

It extends the original Module 3 Music Recommender Simulation
by adding input validation, retrieval, logging, automated
testing, and reliability evaluation.

The system does not use a trained machine learning model
or a generative language model.

## 2. Intended Use

The system is designed for:
- Educational demonstrations
- Music recommendation experiments
- Learning recommendation algorithms
- Testing input validation and retrieval workflows
- Demonstrating explainable recommendation logic

### Not Intended For

- Production music streaming services
- High-stakes decision-making
- Predicting individual psychological conditions
- Inferring sensitive personal attributes
- Guaranteeing that users will enjoy recommended songs

## 3. Dataset

The dataset contains 20 songs stored in:

`data/songs.csv`

Available features include:
- Song ID
- Title
- Artist
- Genre
- Mood
- Energy
- Tempo
- Valence
- Danceability
- Acousticness

### Dataset Limitations

The dataset is small and has limited genre and mood coverage.

Recommendation results may not represent the full diversity
of music or individual listener preferences.

## 4. Recommendation Method

The system uses a weighted similarity scoring algorithm.

The implemented scoring weights are:

| Feature | Weight |
|---|---:|
| Genre | 15% |
| Mood | 25% |
| Energy | 40% |
| Valence | 15% |
| Tempo | 10% |

The weights are normalized by 1.05.

Matching categorical features contribute fixed points.
Numerical features contribute points based on similarity
to the user's requested values.

Songs are ranked by their calculated scores.

These scores represent rule-based similarity, not
calibrated probabilities or prediction confidence.

## 5. Retrieval

The SongRetriever prioritizes songs matching the user's
preferred genre or mood.

If additional candidates are needed, it includes other
songs from the dataset.

The recommendation function currently requests up to
the entire dataset, so all available songs can be scored.

This improves result coverage but reduces the filtering
benefit of retrieval for the current 20-song dataset.

## 6. Input Validation and Guardrails

The system validates:
- User preferences must be a nonempty dictionary.
- Genre and mood must be nonempty strings when supplied.
- Energy must be between 0 and 1.
- Valence must be between 0 and 1.
- Tempo must be a positive number.
- Recommendation count must be a positive integer.

Invalid inputs raise ValueError exceptions.

The application records validation warnings in its log.

## 7. Reliability Evaluation

### Observed Application Results

Before the retrieval fallback update, logging showed:

| Profile | Candidates | Recommendations |
|---|---:|---:|
| High-Energy Pop | 3 | 3 |
| Chill Lofi | 4 | 4 |
| Intense Rock | 2 | 2 |
| Sad but Energetic | 1 | 1 |

These results revealed that strict retrieval could
return fewer than the requested five recommendations.

### Reliability Improvement

The retrieval algorithm was modified to prioritize
matching songs while allowing additional songs
to fill the candidate pool.

Automated tests were updated to reflect the revised
retrieval behavior.

### Automated Testing

Test command:

`python -m pytest tests -v`

Tests cover:
- Recommendation behavior
- Genre and mood retrieval
- Retrieval fallback
- Invalid candidate counts
- Input validation
- Recommendation integration

The most recently reported test result before updating
the retrieval tests was 14 passed and 3 failed.

The final test outcome must be confirmed using the
latest pytest output.

## 8. Bias and Fairness Considerations

Potential sources of bias include:

### Dataset Representation Bias

Genres and moods with fewer songs have less variety
in the available recommendations.

### Feature Weight Bias

The selected feature weights emphasize energy and mood.
This may disadvantage songs that match other preferences
but differ in energy.

### Limited Personalization

The system does not learn from individual listening
history or feedback.

### Mitigation Strategies

- Expand the dataset across genres and moods.
- Evaluate ranking quality across different profiles.
- Allow users to adjust feature weights.
- Introduce feedback-based ranking in future versions.

## 9. Safety and Misuse Prevention

The system rejects malformed user preferences and
invalid numerical values.

It does not require personal identifying information.

The local dataset and deterministic algorithm reduce
dependencies on external services.

Application logs should not include unnecessary
personal or sensitive information.

## 10. Explainability

Each recommendation includes a text explanation showing
which preferences contributed to the similarity score.

Explanations describe the implemented scoring calculation;
they do not establish that a user will enjoy a song.

## 11. Known Limitations

- Only 20 songs are available.
- No trained machine learning model is used.
- No semantic embedding search is implemented.
- No collaborative filtering is implemented.
- No user feedback learning is available.
- No formal human relevance evaluation has been completed.
- Similarity scores are not probabilities.
- The current retrieval stage processes all songs when
  called from the recommendation function.

## 12. Lessons Learned

### Unexpected Reliability Finding

The original retrieval logic returned only songs matching
genre or mood.

This resulted in fewer recommendations than requested
for some user profiles.

### Engineering Response

The retrieval logic was changed to include additional
candidates after prioritizing matching songs.

Existing tests initially failed because they asserted
the previous retrieval behavior.

The tests were revised to verify the new behavior.

### Design Tradeoff

The revised approach improves recommendation coverage
but may include less relevant songs.

Future work should evaluate the tradeoff between
candidate recall and recommendation relevance.

## 13. AI Collaboration

AI assistance was used to:
- Design the retrieval architecture
- Implement input validation
- Add application logging
- Develop automated tests
- Diagnose test failures
- Prepare project documentation

### Accepted Suggestion

Adding input validation and automated tests improved
the system's ability to reject invalid preferences.

### Revised Suggestion

The initial strict retrieval approach was revised after
observing that some profiles received too few results.

The revised approach prioritizes matching songs and
includes additional candidates when needed.

All AI-generated code should be reviewed and tested
before being treated as reliable.

## 14. Future Improvements

1. Expand the song dataset.
2. Implement semantic retrieval using embeddings.
3. Collect explicit user feedback.
4. Evaluate ranking quality with human judgments.
5. Improve dataset validation.
6. Add more edge-case and integration tests.

## 15. Conclusion

This project demonstrates an explainable recommendation
pipeline with retrieval, input validation, weighted
scoring, logging, and automated reliability testing.

Its primary contribution is improved system engineering
and reliability rather than development of a trained
machine learning model.
