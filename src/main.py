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


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Taste profile: an upbeat, high-energy listener.
    # Targets are numeric (0-1) so songs can be scored by closeness, not just exact matches.
    user_prefs = {
        "genre": "pop",           # label: exact-match bonus
        "mood": "happy",          # label: exact-match bonus
        "energy": 0.80,           # high, but not maxed out, so near-neighbors still score well
        "valence": 0.75,          # positive/bright sound
        "likes_acoustic": False,  # prefers produced/electronic over acoustic (target acousticness ~0.2)
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print()
    print(format_recommendations(user_prefs, recommendations))


if __name__ == "__main__":
    main()
