from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the highest-scoring songs for a user profile."""
        if k <= 0:
            return []

        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        scored_songs = []

        for song in self.songs:
            song_dict = {
                "id": song.id,
                "title": song.title,
                "artist": song.artist,
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
                "tempo_bpm": song.tempo_bpm,
                "valence": song.valence,
                "danceability": song.danceability,
                "acousticness": song.acousticness,
            }
            score, _ = score_song(user_prefs, song_dict)
            scored_songs.append((song, score))

        ranked_songs = sorted(
            scored_songs,
            key=lambda item: (-item[1], item[0].id),
        )
        return [song for song, _ in ranked_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain the score that a song received for a user profile."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        song_dict = {
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "tempo_bpm": song.tempo_bpm,
            "valence": song.valence,
            "danceability": song.danceability,
            "acousticness": song.acousticness,
        }
        _, reasons = score_song(user_prefs, song_dict)
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    songs: List[Dict] = []

    with open(csv_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against a user profile and return matching reasons."""
    score = 0.0
    reasons: List[str] = []

    favorite_genre = user_prefs.get(
        "favorite_genre", user_prefs.get("genre", "")
    )
    favorite_mood = user_prefs.get(
        "favorite_mood", user_prefs.get("mood", "")
    )
    target_energy = float(
        user_prefs.get("target_energy", user_prefs.get("energy", 0.0))
    )

    song_genre = str(song.get("genre", ""))
    if favorite_genre and song_genre.lower() == str(favorite_genre).lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    song_mood = str(song.get("mood", ""))
    if favorite_mood and song_mood.lower() == str(favorite_mood).lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    song_energy = float(song["energy"])
    energy_match = max(0.0, 1.0 - abs(song_energy - target_energy))
    energy_points = 1.5 * energy_match
    score += energy_points
    reasons.append(
        f"energy similarity ({energy_points:+.2f})"
    )

    likes_acoustic = bool(user_prefs.get("likes_acoustic", False))
    acousticness = float(song["acousticness"])
    acoustic_match = (
        likes_acoustic and acousticness >= 0.50
    ) or (
        not likes_acoustic and acousticness < 0.50
    )
    if acoustic_match:
        score += 0.5
        reasons.append("acoustic preference (+0.5)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score and rank songs, returning the top k with explanations."""
    if k <= 0:
        return []

    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(
        scored_songs,
        key=lambda recommendation: (
            -recommendation[1],
            int(recommendation[0].get("id", 0)),
        ),
    )
    return ranked_songs[:k]
