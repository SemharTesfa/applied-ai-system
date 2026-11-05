# 🎵 Music Recommender Simulation

## Project Summary

This project is a content-based music recommendation system developed using Python. It analyzes a dataset of 20 songs and recommends music based on a user's preferences for genre, mood, energy, valence, and tempo.

The system calculates a weighted similarity score for each song, ranks the songs from highest to lowest score, and displays the top recommendations with explanations.

The project demonstrates how recommendation systems use data, algorithms, and user preferences to generate personalized suggestions. It also explores how changing feature weights can affect recommendations and introduce bias.

I used **ChatGPT and Claude** as AI coding assistants during the development process to help understand the assignment, design the algorithm, develop implementation prompts, analyze results, and evaluate the recommendation system.

---

## 1. Project Objectives

The main objectives of this project are to:

- Build a content-based music recommendation system.
- Load and process music data from a CSV file.
- Represent user preferences using Python dictionaries.
- Calculate weighted similarity scores.
- Rank songs based on their relevance to a user.
- Explain why each song was recommended.
- Test the recommender with different user profiles.
- Investigate algorithmic bias and limitations.
- Evaluate how changing feature weights affects recommendations.
- Practice using AI coding assistants responsibly.

---

## 2. How the System Works

### Recommendation Algorithm

The recommender uses **content-based filtering**.

Content-based filtering recommends items by comparing their characteristics with the user's preferences.

For example, if a user prefers happy pop music with high energy and a tempo around 130 BPM, the system searches for songs with similar characteristics.

### Algorithm Recipe

1. Load the song dataset from `data/songs.csv`.
2. Read the user's preferred genre, mood, energy, valence, and tempo.
3. Compare each song's characteristics with the user's preferences.
4. Calculate a weighted similarity score.
5. Rank all songs from highest to lowest score.
6. Return the top five songs for evaluation or the top three for the original demonstration.
7. Explain which features contributed to each recommendation.

### Recommendation Data Flow

**Input:** User preferences for genre, mood, energy, valence, and tempo.

**Dataset:** The system reads 20 songs from `songs.csv`.

**Processing:** Each song is compared with the user's preferences using weighted similarity calculations.

**Ranking:** Songs are sorted from highest to lowest similarity score.

**Output:** The recommender displays the top-ranked songs, their scores, and explanations.

---

## 3. Song Dataset

The dataset contains **20 fictional songs**, expanded from the original 10-song starter dataset.

Each song includes the following features:

| Feature | Description |
|---|---|
| `id` | Unique song identifier |
| `title` | Song title |
| `artist` | Artist name |
| `genre` | Music genre |
| `mood` | Emotional style |
| `energy` | Energy level between 0 and 1 |
| `tempo_bpm` | Tempo in beats per minute |
| `valence` | Musical positivity between 0 and 1 |
| `danceability` | Danceability between 0 and 1 |
| `acousticness` | Acousticness between 0 and 1 |

The dataset represents multiple musical styles, including pop, lofi, rock, jazz, ambient, synthwave, blues, metal, and electronic music.

The current algorithm uses genre, mood, energy, valence, and tempo. Danceability and acousticness are available but are not included in the scoring calculation.

---

## 4. User Profiles

The recommender represents a listener's preferences using a Python dictionary.

Example:

```python
user_profile = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.80,
    "target_valence": 0.85,
    "target_tempo_bpm": 120
}
```

Each user profile contains five preferences that are compared with the song dataset.

For Phase 4, I tested four different user profiles.

| Profile | Genre | Mood | Energy | Valence | Tempo |
|---|---|---|---|---|---|
| High-Energy Pop | pop | happy | 0.90 | 0.85 | 130 BPM |
| Chill Lofi | lofi | chill | 0.35 | 0.60 | 75 BPM |
| Intense Rock | rock | intense | 0.95 | 0.45 | 155 BPM |
| Sad but Energetic | blues | sad | 0.90 | 0.20 | 145 BPM |

The fourth profile is an adversarial test because it combines a sad mood with high energy and fast tempo. This helps reveal potential weaknesses in the scoring algorithm.

---

## 5. Scoring Algorithm

### Original Feature Weights

| Feature | Weight |
|---|---|
| Genre | 30% |
| Mood | 25% |
| Energy | 20% |
| Valence | 15% |
| Tempo | 10% |
| **Total** | **100%** |

### Scoring Rules

**Genre similarity:** A song receives 0.30 points when its genre matches the user's preferred genre.

**Mood similarity:** A song receives 0.25 points when its mood matches the user's preferred mood.

**Energy similarity:** The system calculates how close the song's energy is to the user's target.

```python
energy_similarity = 1 - abs(song_energy - target_energy)
```

**Valence similarity:** The system compares the song's positivity level with the user's preference.

```python
valence_similarity = 1 - abs(song_valence - target_valence)
```

**Tempo similarity:** The system calculates the difference between the song's tempo and the user's target tempo.

```python
tempo_similarity = max(
    0,
    1 - abs(song_tempo - target_tempo) / 100
)
```

The feature contributions are multiplied by their respective weights and added together.

The final score ranges from 0 to 1.

A higher score indicates a closer match to the user's stated preferences. It does not represent the probability that the user will enjoy the song.

### Ranking Rule

After calculating scores, the recommender sorts songs from highest to lowest score and returns the requested number of recommendations.

The system also generates explanations showing how genre, mood, energy, valence, and tempo contribute to each score.

---

## 6. Getting Started

### Requirements

- Python 3.10 or later
- VS Code or another Python development environment
- Project dependencies listed in `requirements.txt`

### Setup

**Step 1: Create a virtual environment**

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For macOS or Linux:

```bash
source .venv/bin/activate
```

**Step 2: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 3: Run the recommender**

```bash
python -m src.main
```

**Step 4: Run automated tests**

```bash
python -m pytest
```

The project currently uses a command-line interface. A graphical interface may be added in a future version.

---

## 7. Original Recommendation Results

The original recommender was tested with the following default user preferences:

- Genre: pop
- Mood: happy
- Energy: 0.80
- Valence: 0.85
- Tempo: 120 BPM

### Top Three Recommendations

| Rank | Song | Artist | Score |
|---|---|---|---|
| 1 | Sunrise City | Neon Echo | 0.99 |
| 2 | Gym Hero | Max Pulse | 0.70 |
| 3 | Rooftop Lights | Indigo Parade | 0.68 |

### Verified Terminal Output

```text
Loaded songs: 20
User profile: genre=pop, mood=happy, energy=0.80, valence=0.85, tempo=120 BPM

Top 3 recommendations:

1. Sunrise City by Neon Echo - Score: 0.99
   Reasons:
   - genre match: pop (+0.30)
   - mood match: happy (+0.25)
   - energy 0.82 vs target 0.80 (+0.20)
   - valence 0.84 vs target 0.85 (+0.15)
   - tempo 118 BPM vs target 120 (+0.10)

2. Gym Hero by Max Pulse - Score: 0.70
   Reasons:
   - genre match: pop (+0.30)
   - energy 0.93 vs target 0.80 (+0.17)
   - valence 0.77 vs target 0.85 (+0.14)
   - tempo 132 BPM vs target 120 (+0.09)

3. Rooftop Lights by Indigo Parade - Score: 0.68
   Reasons:
   - mood match: happy (+0.25)
   - energy 0.76 vs target 0.80 (+0.19)
   - valence 0.81 vs target 0.85 (+0.14)
   - tempo 124 BPM vs target 120 (+0.10)
```

Sunrise City ranked first because it matched both the user's preferred genre and mood while closely matching the numerical features.

---

## 8. Phase 4: Evaluation with Diverse User Profiles

I tested four user profiles to examine how the recommendation system responds to different musical preferences.

For each profile, the recommender generated five ranked songs.

### Experiment A: Original Algorithm

The original algorithm used the weights 30% genre, 25% mood, 20% energy, 15% valence, and 10% tempo.

#### Chill Lofi

```text
Profile: Chill Lofi
Preferences: genre=lofi, mood=chill, energy=0.35, valence=0.60, tempo=75 BPM

1. Library Rain - Paper Lanterns
   Score: 1.00

2. Midnight Coding - LoRoom
   Score: 0.98

3. Focus Flow - LoRoom
   Score: 0.73

4. Spacewalk Thoughts - Orbit Bloom
   Score: 0.66

5. Coffee Shop Stories - Slow Stereo
   Score: 0.41
```

Library Rain ranked first because it matched both genre and mood and had nearly identical numerical features.

#### Intense Rock

```text
Profile: Intense Rock
Preferences: genre=rock, mood=intense, energy=0.95, valence=0.45, tempo=155 BPM

1. Storm Runner - Voltline
   Score: 0.98

2. Gym Hero - Max Pulse
   Score: 0.62

3. Iron Requiem - Black Cathedral
   Score: 0.40

4. Night Drive Loop - Neon Echo
   Score: 0.36

5. Neon Pulse Festival - Hyperion Drop
   Score: 0.35
```

Storm Runner ranked first because it matched the rock genre, intense mood, high energy, and fast tempo.

#### Sad but Energetic

```text
Profile: Sad but Energetic
Preferences: genre=blues, mood=sad, energy=0.90, valence=0.20, tempo=145 BPM

1. Crossroads at Midnight - Delta Smoke
   Score: 0.57

2. Iron Requiem - Black Cathedral
   Score: 0.41

3. Storm Runner - Voltline
   Score: 0.40

4. Gym Hero - Max Pulse
   Score: 0.35

5. Night Drive Loop - Neon Echo
   Score: 0.34
```

This profile revealed a weakness in the algorithm.

Crossroads at Midnight ranked first because it matched the preferred blues genre. However, its energy was only 0.48 compared with the user's target of 0.90, and its tempo was 72 BPM compared with the target of 145 BPM.

This showed that the genre weight could overpower differences in numerical preferences.

---

## 9. Weight-Shift Experiment

### Experiment Goal

The goal was to determine whether increasing the importance of energy and reducing the importance of genre would change the rankings.

### Original vs. Experimental Weights

| Feature | Original | Experimental |
|---|---|---|
| Genre | 30% | 15% |
| Mood | 25% | 25% |
| Energy | 20% | 40% |
| Valence | 15% | 15% |
| Tempo | 10% | 10% |
| **Total** | **100%** | **105%** |

Because the experimental weights total 105%, the experimental scores were normalized by dividing by 1.05.

### Experimental Results

The following results were produced by the modified scoring algorithm.

#### High-Energy Pop

```text
Profile: High-Energy Pop
Preferences: genre=pop, mood=happy, energy=0.90, valence=0.85, tempo=130 BPM

1. Sunrise City - Neon Echo
   Score: 0.96

2. Rooftop Lights - Indigo Parade
   Score: 0.79

3. Gym Hero - Max Pulse
   Score: 0.74

4. Neon Pulse Festival - Hyperion Drop
   Score: 0.59

5. Fuego en la Noche - Luna Caliente
   Score: 0.57
```

#### Chill Lofi

```text
Profile: Chill Lofi
Preferences: genre=lofi, mood=chill, energy=0.35, valence=0.60, tempo=75 BPM

1. Library Rain - Paper Lanterns
   Score: 1.00

2. Midnight Coding - LoRoom
   Score: 0.96

3. Spacewalk Thoughts - Orbit Bloom
   Score: 0.81

4. Focus Flow - LoRoom
   Score: 0.74

5. Coffee Shop Stories - Slow Stereo
   Score: 0.58
```

#### Intense Rock

```text
Profile: Intense Rock
Preferences: genre=rock, mood=intense, energy=0.95, valence=0.45, tempo=155 BPM

1. Storm Runner - Voltline
   Score: 0.98

2. Gym Hero - Max Pulse
   Score: 0.78

3. Iron Requiem - Black Cathedral
   Score: 0.57

4. Neon Pulse Festival - Hyperion Drop
   Score: 0.53

5. Night Drive Loop - Neon Echo
   Score: 0.49
```

#### Sad but Energetic

```text
Profile: Sad but Energetic
Preferences: genre=blues, mood=sad, energy=0.90, valence=0.20, tempo=145 BPM

1. Storm Runner - Voltline
   Score: 0.57

2. Iron Requiem - Black Cathedral
   Score: 0.57

3. Gym Hero - Max Pulse
   Score: 0.51

4. Crossroads at Midnight - Delta Smoke
   Score: 0.51

5. Neon Pulse Festival - Hyperion Drop
   Score: 0.49
```

### Comparison of Results

The largest change occurred with the Sad but Energetic profile.

| Song | Original Rank | Experimental Rank |
|---|---|---|
| Crossroads at Midnight | 1 | 4 |
| Storm Runner | 3 | 1 |
| Iron Requiem | 2 | 2 |
| Gym Hero | 4 | 3 |

Under the original algorithm, Crossroads at Midnight ranked first because of its blues genre match.

After increasing the energy weight, Storm Runner ranked first because its energy of 0.91 was close to the user's target of 0.90 and its tempo was also close to the requested value.

However, Storm Runner did not match the requested blues genre or sad mood.

**Conclusion:** Increasing the energy weight improved numerical matching for this profile but did not necessarily improve overall musical relevance.

---

## 10. Comparison Between User Profiles

### High-Energy Pop vs. Chill Lofi

High-Energy Pop ranked Sunrise City first, while Chill Lofi ranked Library Rain first.

The profiles have different genre, mood, energy, and tempo preferences, so different recommendations are expected.

### High-Energy Pop vs. Intense Rock

High-Energy Pop ranked Sunrise City first, while Intense Rock ranked Storm Runner first.

Although both users prefer high-energy music, they have different genre, mood, valence, and tempo preferences.

### High-Energy Pop vs. Sad but Energetic

The experimental algorithm ranked Sunrise City first for High-Energy Pop and Storm Runner first for Sad but Energetic.

The difference reflects their distinct preference combinations, although neither result alone establishes real-world listener satisfaction.

### Chill Lofi vs. Intense Rock

Chill Lofi favored low-energy, slower songs such as Library Rain and Midnight Coding.

Intense Rock favored high-energy, faster songs such as Storm Runner and Gym Hero.

This demonstrates that the recommender responds to numerical differences in energy and tempo.

### Chill Lofi vs. Sad but Energetic

Chill Lofi ranked Library Rain first, while Sad but Energetic ranked Storm Runner first under the experimental algorithm.

The energy weight strongly influenced the different rankings.

### Intense Rock vs. Sad but Energetic

Under the experimental algorithm, Storm Runner ranked first for both profiles.

This revealed an important limitation: users with different genre and mood preferences can receive the same top recommendation when their numerical preferences are similar and energy is heavily weighted.

---

## 11. Strengths

The recommendation system has several strengths:

- It provides personalized rankings based on user preferences.
- It uses numerical similarity rather than always favoring higher values.
- It explains why each song was recommended.
- It supports multiple user profiles.
- It allows feature weights to be adjusted and evaluated.
- It produces understandable results for clearly defined preferences.
- It is simple enough to inspect, test, and improve.

---

## 12. Limitations and Risks

### Small Dataset

The catalog contains only 20 songs. This limits the variety of available recommendations.

### Genre and Mood Bias

The original algorithm gives genre and mood a combined weight of 55%. This can favor categorical matches even when energy and tempo differ significantly.

### Energy Bias

The experimental algorithm gives energy greater importance. This can cause songs with matching energy levels to rank highly even when their genres and moods differ.

### Filter Bubbles

The system may repeatedly recommend songs similar to the user's existing preferences, limiting exposure to unfamiliar genres and artists.

### No User Feedback

The recommender does not learn from likes, dislikes, skips, or listening history.

### Limited Musical Features

The algorithm does not currently consider lyrics, language, cultural context, danceability, or acousticness.

### Exact-Match Categories

Genre and mood are treated as exact categories. Related genres and similar moods do not receive partial credit.

### No Real-World Accuracy Measurement

The automated tests verify software behavior, but the project does not measure actual listener satisfaction or recommendation accuracy using real user feedback.

---

## 13. AI Tools and Development Process

I used **ChatGPT and Claude** to support the development and evaluation of this project.

### ChatGPT

ChatGPT helped me:

- Understand content-based recommendation systems.
- Identify useful song features and user preferences.
- Design the weighted scoring algorithm.
- Develop implementation prompts for the Python functions.
- Understand numerical similarity calculations.
- Plan the ranking and explanation logic.
- Create diverse and adversarial user profiles.
- Analyze recommendation results.
- Design the weight-shift experiment.
- Identify potential bias and limitations.
- Prepare project documentation and reflection.

### Claude

I also used Claude as an AI coding assistant during the project.

Claude was part of my AI-assisted development workflow alongside ChatGPT. I reviewed the project behavior by running the Python application and automated tests locally in VS Code.

### Human Verification

I verified the recommender by:

1. Running `python -m src.main`.
2. Confirming that 20 songs were loaded.
3. Reviewing the ranked recommendations.
4. Testing multiple user profiles.
5. Running a temporary weight-shift experiment.
6. Comparing original and experimental rankings.
7. Running `python -m pytest`.

The project passed both available automated tests during the recorded runs.

AI assistance helped with development, but the recommendations and experimental conclusions were checked against actual terminal results.

---

## 14. Testing

The project was tested in a Python 3.10 environment on Windows.

### Commands

```bash
python -m src.main
python -m pytest
```

### Verified Test Results

```text
collected 2 items

tests\test_recommender.py .. [100%]

2 passed in 0.08s
```

The final experimental run successfully:

- Loaded 20 songs.
- Evaluated four user profiles.
- Generated five recommendations for each profile.
- Produced similarity scores and explanations.
- Passed both automated tests.

The original algorithm also passed both automated tests before the experiment.

---

## 15. Future Improvements

I would like to improve the recommender by:

1. Building a Streamlit web interface.
2. Allowing users to select their favorite genre and mood interactively.
3. Adding sliders for energy, valence, and tempo.
4. Supporting adjustable feature weights.
5. Expanding the dataset to include more genres, artists, and languages.
6. Adding danceability and acousticness to the scoring algorithm.
7. Incorporating user feedback and listening history.
8. Introducing diversity-aware recommendations.
9. Testing with more adversarial user profiles.
10. Comparing the recommender with other recommendation approaches.

---

## 16. Personal Reflection

Through this project, I learned how a recommendation system transforms song features and user preferences into numerical similarity scores. I practiced loading CSV data, designing weighted algorithms, comparing numerical values, ranking songs, and generating explanations. I also learned how to use ChatGPT and Claude as development assistants while verifying the results through actual Python execution and automated testing.

The most interesting part of the project was discovering how changing feature weights affected the recommendations. The Sad but Energetic profile demonstrated that a song could rank first because of its genre even when its energy and tempo did not closely match the user's preferences. After increasing the energy weight, a different song ranked first. This helped me understand that recommendation algorithms reflect design choices and assumptions rather than objective musical taste.

This project changed how I think about music recommendation applications. I now understand that recommendations depend on the data, selected features, scoring weights, and user preferences. A high score does not necessarily mean a user will enjoy a song. In the future, I would like to develop a more interactive recommendation system that incorporates user feedback and encourages music discovery.

---

## 17. Model Documentation

Additional details about the system's intended use, strengths, limitations, bias, evaluation, and future improvements are available in the [Model Card](model_card.md).

---

## Project Status

**Core recommender:** Implemented and tested.

**Dataset:** 20 songs.

**Recommendation method:** Content-based filtering.

**Evaluation:** Four user profiles and one weight-shift experiment.

**Automated tests:** 2 passed, 0 failed.

**Interface:** Python command-line application.

**Future enhancement:** Interactive Streamlit web interface.