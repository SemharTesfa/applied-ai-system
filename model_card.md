# 🎧 Model Card: VibeMatch 1.0

## 1. Model Name

**VibeMatch 1.0 — Content-Based Music Recommender**

VibeMatch is a simple Python program that recommends songs based on a user's music preferences.

## 2. Goal / Task

The goal is to recommend songs that match what a user likes.

The system compares each song with the user's preferred genre, mood, energy, valence, and tempo.

It gives every song a similarity score, ranks the songs, and recommends the best matches.

The score measures how closely a song matches the user's preferences. It does not predict whether the user will definitely enjoy the song.

## 3. Data Used

The project uses a CSV dataset containing **20 fictional songs**.

Each song includes:

- Song ID, title, and artist
- Genre and mood
- Energy and valence
- Tempo in BPM
- Danceability and acousticness

The scoring algorithm uses five features: genre, mood, energy, valence, and tempo.

The dataset is small and does not include real user ratings or listening history. It also does not represent every genre, language, or musical style.

## 4. Algorithm Summary

VibeMatch uses **content-based filtering**.

It compares song features with the user's preferences and calculates a weighted similarity score.

The original scoring weights are:

| Feature | Weight |
|---|---:|
| Genre | 30% |
| Mood | 25% |
| Energy | 20% |
| Valence | 15% |
| Tempo | 10% |
| **Total** | **100%** |

Genre and mood receive points for exact matches.

Energy, valence, and tempo receive more points when their values are closer to the user's preferences.

The system adds the weighted scores and ranks songs from highest to lowest.

The original demonstration recommends three songs. During evaluation, I generated five recommendations for each user profile.

## 5. Observed Behavior / Biases

I discovered that feature weights strongly affect the recommendations.

For example, the Sad but Energetic profile preferred blues, sad music, high energy, and fast tempo.

Under the original algorithm, **Crossroads at Midnight** ranked first with a score of 0.57. It matched the blues genre, but its energy and tempo were much lower than the user's targets.

After increasing the energy weight, **Storm Runner** ranked first with a score of 0.57. Its energy and tempo were closer to the user's preferences, but it did not match the requested genre or mood.

This showed me that a recommendation can be strong in one area but weak in another.

Other limitations include the small dataset, exact genre and mood matching, missing listening history, and the risk of repeatedly recommending similar songs.

## 6. Evaluation Process

I tested the recommender with four user profiles.

| Profile | Genre | Mood | Energy | Valence | Tempo |
|---|---|---|---:|---:|---:|
| High-Energy Pop | pop | happy | 0.90 | 0.85 | 130 BPM |
| Chill Lofi | lofi | chill | 0.35 | 0.60 | 75 BPM |
| Intense Rock | rock | intense | 0.95 | 0.45 | 155 BPM |
| Sad but Energetic | blues | sad | 0.90 | 0.20 | 145 BPM |

I generated five recommendations for each profile and reviewed their scores and explanations.

### Weight-Shift Experiment

I temporarily changed the scoring weights to test how they affect the results.

| Feature | Original | Experimental |
|---|---:|---:|
| Genre | 30% | 15% |
| Mood | 25% | 25% |
| Energy | 20% | 40% |
| Valence | 15% | 15% |
| Tempo | 10% | 10% |

The experimental weights totaled 105%, so I divided the final weighted scores by 1.05.

### Results

| Profile | Top Song (Experimental) | Score |
|---|---|---:|
| High-Energy Pop | Sunrise City | 0.96 |
| Chill Lofi | Library Rain | 1.00 |
| Intense Rock | Storm Runner | 0.98 |
| Sad but Energetic | Storm Runner | 0.57 |

The biggest change was in the Sad but Energetic profile.

Crossroads at Midnight dropped from first to fourth place. Storm Runner moved from third to first.

I also compared the profiles to see how different preferences changed the recommendations. Chill Lofi favored slower, lower-energy songs, while Intense Rock favored faster, higher-energy songs.

One surprising result was that Intense Rock and Sad but Energetic both ranked Storm Runner first under the experimental weights, even though their genre and mood preferences were different.

### Automated Testing

I ran:

```bash
python -m src.main
python -m pytest
```

The program loaded 20 songs and generated recommendations for all four profiles.

**Test results: 2 passed, 0 failed.**

The tests confirmed that the existing automated checks passed. They did not measure actual listener satisfaction.

## 7. Intended Use and Non-Intended Use

### Intended Use

VibeMatch is designed for:

- Learning how recommendation algorithms work.
- Practicing Python programming and CSV data processing.
- Testing different user preferences.
- Understanding weighted scoring and ranking.
- Studying how algorithm choices affect recommendations.

### Non-Intended Use

VibeMatch should not be used as:

- A commercial music recommendation system.
- A reliable prediction of someone's musical taste.
- A system that claims to understand a person's emotions.
- A replacement for recommendation systems trained on large, real-world datasets.

It is an educational simulation, not a trained machine-learning model.

## 8. Ideas for Improvement

If I continued developing this project, I would focus on three improvements:

1. **Build a Streamlit interface.** Users could select their preferences and view recommendations in a browser.
2. **Expand the dataset and add feedback.** More songs and user likes or dislikes could improve personalization.
3. **Make feature weights adjustable.** Users could decide whether genre, mood, energy, valence, or tempo matters most.

## 9. Personal Reflection

My biggest learning moment was the weight-shift experiment. I learned that changing a few numbers in the scoring algorithm can change which songs are recommended. For the Sad but Energetic profile, the top recommendation changed from Crossroads at Midnight to Storm Runner. This helped me understand that the developer's choices directly affect the results.

I used **ChatGPT and Claude** to help with the project. These tools helped me understand the assignment, work through Python implementation ideas, plan experiments, and explain the results. I still needed to double-check the code and recommendations by running the program in VS Code. I also ran automated tests to confirm that the implementation passed the existing checks.

I was surprised that a simple weighted scoring algorithm could produce recommendations that seemed personalized. The system does not learn from real users, but comparing song features with preferences can still produce useful rankings.

If I extended this project, I would build an interactive interface, expand the song dataset, and allow users to adjust the scoring weights. I would also collect feedback to see whether users actually enjoy the recommended songs.

This project helped me understand that building an AI-related system involves more than writing code. It also requires testing, evaluating limitations, documenting decisions, and checking whether the results make sense.