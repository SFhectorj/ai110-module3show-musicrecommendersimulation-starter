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

### What each `Song` uses

- `genre` and `mood` (labels)
- `energy`, `valence`, `acousticness` (numbers from 0 to 1)
- `tempo_bpm` and `danceability` are stored but barely used, because they mostly repeat energy.

### What `UserProfile` stores

- `favorite_genre`
- `favorite_mood`
- `target_energy`
- `likes_acoustic`

### How a song gets a score

1. Compare the song to the user's profile, one feature at a time.
2. Energy: the closer to the target, the more points (`1 - |difference|`).
3. Mood and genre: a bonus if they match exactly.
4. Acousticness: it fits better if the song's level matches what the user likes.
5. Add the points with weights (starting guess):

```
score = 0.35 energy + 0.25 mood + 0.20 genre + 0.12 valence + 0.08 acousticness
```

Valence needs a `target_valence` field on `UserProfile`, which doesn't exist yet.

### How songs get chosen

1. Score every song in the list.
2. Sort from highest to lowest score.
3. Return the top `k` songs, each with a short reason, such as "matches your mood and has similar energy".

```
UserProfile + all Songs -> score each song -> sort high to low -> top k
```

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

Output of `python -m src.main` for the default pop/happy profile:

```
Loaded songs: 19

========================================================================
                          TOP RECOMMENDATIONS
Profile: genre=pop, mood=happy, energy=0.80, valence=0.75, likes_acoustic=False
========================================================================

#1  Sunrise City  by Neon Echo
    Score: 0.98 / 1.00   [pop, happy]
    Why:
      - energy 0.82 vs. target 0.80 (+0.34)
      - mood match: happy (+0.25)
      - genre match: pop (+0.20)
      - valence 0.84 vs. target 0.75 (+0.11)
      - acousticness 0.18 vs. target 0.20 (+0.08)
------------------------------------------------------------------------

#2  Rooftop Lights  by Indigo Parade
    Score: 0.77 / 1.00   [indie pop, happy]
    Why:
      - energy 0.76 vs. target 0.80 (+0.34)
      - mood match: happy (+0.25)
      - genre mismatch: indie pop (+0.00)
      - valence 0.81 vs. target 0.75 (+0.11)
      - acousticness 0.35 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#3  Gym Hero  by Max Pulse
    Score: 0.69 / 1.00   [pop, intense]
    Why:
      - energy 0.93 vs. target 0.80 (+0.30)
      - mood mismatch: intense (+0.00)
      - genre match: pop (+0.20)
      - valence 0.77 vs. target 0.75 (+0.12)
      - acousticness 0.05 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#4  Concrete Crown  by Rhyme Atlas
    Score: 0.52 / 1.00   [hip hop, confident]
    Why:
      - energy 0.78 vs. target 0.80 (+0.34)
      - mood mismatch: confident (+0.00)
      - genre mismatch: hip hop (+0.00)
      - valence 0.62 vs. target 0.75 (+0.10)
      - acousticness 0.08 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#5  Fiesta Sol  by Los Marea
    Score: 0.50 / 1.00   [latin, euphoric]
    Why:
      - energy 0.88 vs. target 0.80 (+0.32)
      - mood mismatch: euphoric (+0.00)
      - genre mismatch: latin (+0.00)
      - valence 0.92 vs. target 0.75 (+0.10)
      - acousticness 0.20 vs. target 0.20 (+0.08)
------------------------------------------------------------------------
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



