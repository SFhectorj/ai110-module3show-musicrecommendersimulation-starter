import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

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
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs from a CSV file into dicts, converting id to int and numeric features to float."""
    int_fields = ("id",)
    float_fields = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for key in int_fields:
                row[key] = int(row[key])
            for key in float_fields:
                row[key] = float(row[key])
            songs.append(row)
    return songs

# Starting-guess weights from README.md ("How a song gets a score"); they sum to 1.0.
WEIGHTS = {
    "energy": 0.35,
    "mood": 0.25,
    "genre": 0.20,
    "valence": 0.12,
    "acousticness": 0.08,
}

# likes_acoustic is a bool, so it maps to a target acousticness level.
ACOUSTIC_TARGET_LIKED = 0.8
ACOUSTIC_TARGET_DISLIKED = 0.2

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a song's weighted match score (0-1) and a list of reasons showing each feature's points."""
    # score = 0.35 energy + 0.25 mood + 0.20 genre + 0.12 valence + 0.08 acousticness
    # Every component adds a reason with the points it contributed, so the
    # reasons always sum to the score.
    score = 0.0
    reasons: List[str] = []

    # Energy: closer to the target earns more points (1 - |difference|).
    energy_pts = WEIGHTS["energy"] * (1 - abs(song["energy"] - user_prefs["energy"]))
    score += energy_pts
    reasons.append(
        f"energy {song['energy']:.2f} vs. target {user_prefs['energy']:.2f} (+{energy_pts:.2f})"
    )

    # Mood and genre: bonus only on an exact match.
    if song["mood"] == user_prefs["mood"]:
        score += WEIGHTS["mood"]
        reasons.append(f"mood match: {song['mood']} (+{WEIGHTS['mood']:.2f})")
    else:
        reasons.append(f"mood mismatch: {song['mood']} (+0.00)")
    if song["genre"] == user_prefs["genre"]:
        score += WEIGHTS["genre"]
        reasons.append(f"genre match: {song['genre']} (+{WEIGHTS['genre']:.2f})")
    else:
        reasons.append(f"genre mismatch: {song['genre']} (+0.00)")

    # Valence: closer to the target earns more points.
    valence_pts = WEIGHTS["valence"] * (1 - abs(song["valence"] - user_prefs["valence"]))
    score += valence_pts
    reasons.append(
        f"valence {song['valence']:.2f} vs. target {user_prefs['valence']:.2f} (+{valence_pts:.2f})"
    )

    # Acousticness: fits better when the song's level matches what the user likes.
    acoustic_target = ACOUSTIC_TARGET_LIKED if user_prefs["likes_acoustic"] else ACOUSTIC_TARGET_DISLIKED
    acoustic_pts = WEIGHTS["acousticness"] * (1 - abs(song["acousticness"] - acoustic_target))
    score += acoustic_pts
    reasons.append(
        f"acousticness {song['acousticness']:.2f} vs. target {acoustic_target:.2f} (+{acoustic_pts:.2f})"
    )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song with score_song and return the top k as (song, score, explanation) tuples."""
    # Judge every song in the catalog with score_song...
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, "; ".join(reasons)))

    # ...then sort the whole list from highest to lowest score and keep the top k.
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
