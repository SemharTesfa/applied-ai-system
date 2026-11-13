
---

# Applied AI System — Final Project Reflection

## 1. How I Used AI Assistance

I used ChatGPT as a development assistant to extend my
original Music Recommender Simulation into a more reliable,
retrieval-enhanced recommendation system.

AI assistance supported:
- System architecture planning
- Python code development
- Input validation
- Song retrieval
- Logging and error handling
- Automated test development
- Debugging
- Documentation

I reviewed the suggested changes and tested the code
using Python and pytest.

## 2. AI Suggestion I Accepted

One useful suggestion was adding input validation before
processing recommendation requests.

The validator checks that:
- User preferences are valid.
- Energy and valence are within acceptable ranges.
- Tempo is positive.
- Recommendation count is valid.

This prevents invalid input from reaching the scoring
algorithm and improves application reliability.

I also accepted the suggestion to introduce application
logging so recommendation activity could be inspected.

## 3. AI Suggestion I Revised

The initial song retrieval implementation returned only
songs matching the requested genre or mood.

During testing, I observed that some profiles received
fewer recommendations than requested.

For example, the Sad but Energetic profile returned only
one recommendation.

I revised the retrieval approach so matching songs are
prioritized while additional songs can be included.

This improved recommendation coverage.

## 4. Debugging and Testing Experience

After changing the retrieval logic, I ran:

python -m pytest tests -v

The test results showed:

14 passed, 3 failed

The failing tests were:
- test_retriever_matches_genre
- test_retriever_matches_mood
- test_retrieval_integrated_with_recommendations

The failures occurred because the tests expected the
original strict filtering behavior.

I updated the tests to verify the revised retrieval
requirements, including candidate coverage and ranking.

The final test result should be recorded after running
the complete updated test suite.

## 5. Human Decisions

I made several implementation decisions:

- Retained the Python command-line interface.
- Used the existing 20-song CSV dataset.
- Continued using explainable weighted scoring.
- Added reliability features without introducing
  unnecessary external dependencies.
- Prioritized working functionality and testing
  over building a new graphical interface.

## 6. What I Learned

This project demonstrated that implementing an algorithm
is only one part of building a reliable AI-related system.

Input validation, retrieval behavior, logging, testing,
and documentation are also important.

I learned that changing application requirements may
require updating automated tests.

I also learned that AI-generated suggestions must be
evaluated against actual application behavior.

## 7. Limitations of AI Assistance

AI assistance accelerated development, but suggested
code was not automatically correct for every requirement.

The initial retrieval design limited recommendation
coverage, and its revision required changes to the
existing tests.

I used application outputs, logs, and pytest results
to identify and address these issues.

## 8. Final Reflection

The project evolved from a basic music recommendation
simulation into a structured, explainable recommendation
application.

The most important improvements were input validation,
retrieval, execution logging, and automated testing.

Future work could include a larger dataset, semantic
retrieval, user feedback, and more comprehensive
recommendation quality evaluation.
