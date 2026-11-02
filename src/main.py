"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs  # python -m src.main
except ImportError:
    from recommender import load_songs, recommend_songs  # python src/main.py

WIDTH = 72


def format_recommendations(user_prefs: dict, recommendations: list) -> str:
    """Builds a readable terminal layout: rank, title, artist, score, then one line per reason."""
    lines = [
        "=" * WIDTH,
        "TOP RECOMMENDATIONS".center(WIDTH),
        (
            f"Profile: genre={user_prefs['genre']}, mood={user_prefs['mood']}, "
            f"energy={user_prefs['energy']:.2f}, valence={user_prefs['valence']:.2f}, "
            f"likes_acoustic={user_prefs['likes_acoustic']}"
        ).center(WIDTH),
        "=" * WIDTH,
    ]
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        lines.append("")
        lines.append(f"#{rank}  {song['title']}  by {song['artist']}")
        lines.append(f"    Score: {score:.2f} / 1.00   [{song['genre']}, {song['mood']}]")
        lines.append("    Why:")
        for reason in explanation.split("; "):
            lines.append(f"      - {reason}")
        lines.append("-" * WIDTH)
    return "\n".join(lines)


# Three realistic taste profiles.
STANDARD_PROFILES = {
    "High-Energy Pop": {
        "genre": "pop", "mood": "happy", "energy": 0.85, "valence": 0.80, "likes_acoustic": False,
    },
    "Chill Lofi": {
        "genre": "lofi", "mood": "chill", "energy": 0.35, "valence": 0.58, "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "genre": "rock", "mood": "intense", "energy": 0.92, "valence": 0.40, "likes_acoustic": False,
    },
}

# Adversarial / edge-case profiles meant to trick or stress the scoring logic.
ADVERSARIAL_PROFILES = {
    "Conflicting: high energy + sad": {
        "genre": "blues", "mood": "sad", "energy": 0.90, "valence": 0.20, "likes_acoustic": True,
    },
    "Unknown genre and mood": {
        "genre": "k-pop", "mood": "dreamy", "energy": 0.60, "valence": 0.60, "likes_acoustic": False,
    },
    "Out-of-range values (energy 1.8, valence -0.5)": {
        "genre": "pop", "mood": "happy", "energy": 1.8, "valence": -0.5, "likes_acoustic": False,
    },
    "Dead-center middle (0.5 everywhere)": {
        "genre": "jazz", "mood": "relaxed", "energy": 0.5, "valence": 0.5, "likes_acoustic": True,
    },
    "Mood/genre clash: metal + chill": {
        "genre": "metal", "mood": "chill", "energy": 0.30, "valence": 0.60, "likes_acoustic": True,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for group, profiles in (("STANDARD", STANDARD_PROFILES), ("ADVERSARIAL", ADVERSARIAL_PROFILES)):
        for name, user_prefs in profiles.items():
            recommendations = recommend_songs(user_prefs, songs, k=5)
            print()
            print(f"##### {group}: {name} #####")
            print(format_recommendations(user_prefs, recommendations))


if __name__ == "__main__":
    main()
