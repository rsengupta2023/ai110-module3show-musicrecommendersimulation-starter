"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        (
            "High-Energy Pop",
            {"genre": "pop", "mood": "happy", "energy": 0.68, "likes_acoustic": False},
        ),
        (
            "Chill Lofi",
            {"genre": "lofi", "mood": "chill", "energy": 0.38, "likes_acoustic": True},
        ),
        (
            "Deep Intense Rock",
            {"genre": "rock", "mood": "intense", "energy": 0.90, "likes_acoustic": False},
        ),
        (
            "Conflicting Sad/Energetic Edge Case",
            {"genre": "blues", "mood": "sad", "energy": 0.90, "likes_acoustic": True},
        ),
    ]

    for name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{name}")
        print(
            f"  Genre: {user_prefs['genre']} | Mood: {user_prefs['mood']} "
            f"| Energy: {user_prefs['energy']:.2f} "
            f"| Likes acoustic: {user_prefs['likes_acoustic']}"
        )
        print("  Top 5 Recommendations:")

        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"  {rank}. {song['title']} by {song['artist']}")
            print(f"     Score: {score:.2f}")
            print(f"     Reasons: {explanation}")


if __name__ == "__main__":
    main()
