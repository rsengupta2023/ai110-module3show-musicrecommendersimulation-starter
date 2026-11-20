# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world music recommenders estimate how likely a listener is to enjoy a song from patterns in listening history, similarity to other users and songs, and the song's metadata or audio features. Our simulation will be simpler and will prioritize transparent, content-based matching: it will compare each song directly with an explicit taste profile and rank the closest matches.

**Object features**

- `Song`: `id`, `title`, `artist`, `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`.
- `UserProfile`: `favorite_genre`, `favorite_mood`, `target_energy`, and `likes_acoustic`.

**Scoring rule**

Each `Song` will receive a weighted total score from several feature matches. Categorical features use exact-match contributions: `genre` and `mood` each earn a fixed bonus only when they equal the user's favorites.

For the numerical `energy` feature, the score rewards closeness rather than a universally high or low value. Both values are on the normalized `0.0–1.0` scale, so:

`energy_match = 1 - |song.energy - user.target_energy|`

This produces `1.0` for an exact match and a score that decreases in proportion to the absolute difference. If the feature ever uses a range wider than `0.0–1.0`, the formula will instead divide the difference by that range: `1 - |song_value - target_value| / value_range`.

The intended overall formula is:

`total_score = (genre_weight × genre_match) + (mood_weight × mood_match) + (energy_weight × energy_match) + (acoustic_weight × acoustic_match)`

Here, each match is either `1.0` or `0.0`, except `energy_match`, which is continuous between `0.0` and `1.0`. `acoustic_match` will reflect `likes_acoustic` when implemented: a user who likes acoustic songs will favor higher `acousticness`, while a user who does not will favor lower values. This plan leaves the weights tunable and defers implementation of the acoustic formula until a clear preference range is defined.

The recommender will score every song, sort by descending `total_score`, and return the top `k` songs. The other numerical fields (`tempo_bpm`, `valence`, and `danceability`) are retained for a richer future profile and for explaining catalog data, but are not required in the first scoring rule.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


