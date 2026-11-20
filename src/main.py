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

    # The profile favors upbeat pop without requiring the same genre or mood for every
    # recommendation. A moderate energy target also leaves room for adjacent styles.
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.68,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nUser Profile:")
    print(
        f"  Genre: {user_prefs['genre']} | Mood: {user_prefs['mood']} "
        f"| Energy: {user_prefs['energy']:.2f} "
        f"| Likes acoustic: {user_prefs['likes_acoustic']}"
    )
    print("\nTop 5 Recommendations:")

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")


if __name__ == "__main__":
    main()
