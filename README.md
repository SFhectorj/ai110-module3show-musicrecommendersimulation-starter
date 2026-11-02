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




---

## Sample Recommendations (Profile Evaluation)

Profiles are defined in `src/main.py`; run all of them with `python3 -m src.main`. Standard profiles first, then adversarial edge cases that try to trick the scoring logic.

### Standard: High-Energy Pop

```text
========================================================================
                          TOP RECOMMENDATIONS                           
Profile: genre=pop, mood=happy, energy=0.85, valence=0.80, likes_acoustic=False
========================================================================

#1  Sunrise City  by Neon Echo
    Score: 0.98 / 1.00   [pop, happy]
    Why:
      - energy 0.82 vs. target 0.85 (+0.34)
      - mood match: happy (+0.25)
      - genre match: pop (+0.20)
      - valence 0.84 vs. target 0.80 (+0.12)
      - acousticness 0.18 vs. target 0.20 (+0.08)
------------------------------------------------------------------------

#2  Rooftop Lights  by Indigo Parade
    Score: 0.76 / 1.00   [indie pop, happy]
    Why:
      - energy 0.76 vs. target 0.85 (+0.32)
      - mood match: happy (+0.25)
      - genre mismatch: indie pop (+0.00)
      - valence 0.81 vs. target 0.80 (+0.12)
      - acousticness 0.35 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#3  Gym Hero  by Max Pulse
    Score: 0.71 / 1.00   [pop, intense]
    Why:
      - energy 0.93 vs. target 0.85 (+0.32)
      - mood mismatch: intense (+0.00)
      - genre match: pop (+0.20)
      - valence 0.77 vs. target 0.80 (+0.12)
      - acousticness 0.05 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#4  Fiesta Sol  by Los Marea
    Score: 0.53 / 1.00   [latin, euphoric]
    Why:
      - energy 0.88 vs. target 0.85 (+0.34)
      - mood mismatch: euphoric (+0.00)
      - genre mismatch: latin (+0.00)
      - valence 0.92 vs. target 0.80 (+0.11)
      - acousticness 0.20 vs. target 0.20 (+0.08)
------------------------------------------------------------------------

#5  Pulse Garden  by Kilo Bloom
    Score: 0.51 / 1.00   [edm, energetic]
    Why:
      - energy 0.94 vs. target 0.85 (+0.32)
      - mood mismatch: energetic (+0.00)
      - genre mismatch: edm (+0.00)
      - valence 0.80 vs. target 0.80 (+0.12)
      - acousticness 0.04 vs. target 0.20 (+0.07)
------------------------------------------------------------------------
```

### Standard: Chill Lofi

```text
========================================================================
                          TOP RECOMMENDATIONS                           
Profile: genre=lofi, mood=chill, energy=0.35, valence=0.58, likes_acoustic=True
========================================================================

#1  Library Rain  by Paper Lanterns
    Score: 0.99 / 1.00   [lofi, chill]
    Why:
      - energy 0.35 vs. target 0.35 (+0.35)
      - mood match: chill (+0.25)
      - genre match: lofi (+0.20)
      - valence 0.60 vs. target 0.58 (+0.12)
      - acousticness 0.86 vs. target 0.80 (+0.08)
------------------------------------------------------------------------

#2  Midnight Coding  by LoRoom
    Score: 0.97 / 1.00   [lofi, chill]
    Why:
      - energy 0.42 vs. target 0.35 (+0.33)
      - mood match: chill (+0.25)
      - genre match: lofi (+0.20)
      - valence 0.56 vs. target 0.58 (+0.12)
      - acousticness 0.71 vs. target 0.80 (+0.07)
------------------------------------------------------------------------

#3  Spacewalk Thoughts  by Orbit Bloom
    Score: 0.76 / 1.00   [ambient, chill]
    Why:
      - energy 0.28 vs. target 0.35 (+0.33)
      - mood match: chill (+0.25)
      - genre mismatch: ambient (+0.00)
      - valence 0.65 vs. target 0.58 (+0.11)
      - acousticness 0.92 vs. target 0.80 (+0.07)
------------------------------------------------------------------------

#4  Focus Flow  by LoRoom
    Score: 0.73 / 1.00   [lofi, focused]
    Why:
      - energy 0.40 vs. target 0.35 (+0.33)
      - mood mismatch: focused (+0.00)
      - genre match: lofi (+0.20)
      - valence 0.59 vs. target 0.58 (+0.12)
      - acousticness 0.78 vs. target 0.80 (+0.08)
------------------------------------------------------------------------

#5  Coffee Shop Stories  by Slow Stereo
    Score: 0.52 / 1.00   [jazz, relaxed]
    Why:
      - energy 0.37 vs. target 0.35 (+0.34)
      - mood mismatch: relaxed (+0.00)
      - genre mismatch: jazz (+0.00)
      - valence 0.71 vs. target 0.58 (+0.10)
      - acousticness 0.89 vs. target 0.80 (+0.07)
------------------------------------------------------------------------
```

### Standard: Deep Intense Rock

```text
========================================================================
                          TOP RECOMMENDATIONS                           
Profile: genre=rock, mood=intense, energy=0.92, valence=0.40, likes_acoustic=False
========================================================================

#1  Storm Runner  by Voltline
    Score: 0.98 / 1.00   [rock, intense]
    Why:
      - energy 0.91 vs. target 0.92 (+0.35)
      - mood match: intense (+0.25)
      - genre match: rock (+0.20)
      - valence 0.48 vs. target 0.40 (+0.11)
      - acousticness 0.10 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#2  Gym Hero  by Max Pulse
    Score: 0.74 / 1.00   [pop, intense]
    Why:
      - energy 0.93 vs. target 0.92 (+0.35)
      - mood match: intense (+0.25)
      - genre mismatch: pop (+0.00)
      - valence 0.77 vs. target 0.40 (+0.08)
      - acousticness 0.05 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#3  Cathedral of Static  by Iron Veil
    Score: 0.50 / 1.00   [metal, angry]
    Why:
      - energy 0.97 vs. target 0.92 (+0.33)
      - mood mismatch: angry (+0.00)
      - genre mismatch: metal (+0.00)
      - valence 0.25 vs. target 0.40 (+0.10)
      - acousticness 0.03 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#4  Pulse Garden  by Kilo Bloom
    Score: 0.48 / 1.00   [edm, energetic]
    Why:
      - energy 0.94 vs. target 0.92 (+0.34)
      - mood mismatch: energetic (+0.00)
      - genre mismatch: edm (+0.00)
      - valence 0.80 vs. target 0.40 (+0.07)
      - acousticness 0.04 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#5  Night Drive Loop  by Neon Echo
    Score: 0.48 / 1.00   [synthwave, moody]
    Why:
      - energy 0.75 vs. target 0.92 (+0.29)
      - mood mismatch: moody (+0.00)
      - genre mismatch: synthwave (+0.00)
      - valence 0.49 vs. target 0.40 (+0.11)
      - acousticness 0.22 vs. target 0.20 (+0.08)
------------------------------------------------------------------------
```

### Adversarial: Conflicting: high energy + sad

```text
========================================================================
                          TOP RECOMMENDATIONS                           
Profile: genre=blues, mood=sad, energy=0.90, valence=0.20, likes_acoustic=True
========================================================================

#1  Porch Light Blues  by Delta Marlow
    Score: 0.81 / 1.00   [blues, sad]
    Why:
      - energy 0.40 vs. target 0.90 (+0.17)
      - mood match: sad (+0.25)
      - genre match: blues (+0.20)
      - valence 0.28 vs. target 0.20 (+0.11)
      - acousticness 0.74 vs. target 0.80 (+0.08)
------------------------------------------------------------------------

#2  Cathedral of Static  by Iron Veil
    Score: 0.46 / 1.00   [metal, angry]
    Why:
      - energy 0.97 vs. target 0.90 (+0.33)
      - mood mismatch: angry (+0.00)
      - genre mismatch: metal (+0.00)
      - valence 0.25 vs. target 0.20 (+0.11)
      - acousticness 0.03 vs. target 0.80 (+0.02)
------------------------------------------------------------------------

#3  Storm Runner  by Voltline
    Score: 0.46 / 1.00   [rock, intense]
    Why:
      - energy 0.91 vs. target 0.90 (+0.35)
      - mood mismatch: intense (+0.00)
      - genre mismatch: rock (+0.00)
      - valence 0.48 vs. target 0.20 (+0.09)
      - acousticness 0.10 vs. target 0.80 (+0.02)
------------------------------------------------------------------------

#4  Night Drive Loop  by Neon Echo
    Score: 0.42 / 1.00   [synthwave, moody]
    Why:
      - energy 0.75 vs. target 0.90 (+0.30)
      - mood mismatch: moody (+0.00)
      - genre mismatch: synthwave (+0.00)
      - valence 0.49 vs. target 0.20 (+0.09)
      - acousticness 0.22 vs. target 0.80 (+0.03)
------------------------------------------------------------------------

#5  Gym Hero  by Max Pulse
    Score: 0.41 / 1.00   [pop, intense]
    Why:
      - energy 0.93 vs. target 0.90 (+0.34)
      - mood mismatch: intense (+0.00)
      - genre mismatch: pop (+0.00)
      - valence 0.77 vs. target 0.20 (+0.05)
      - acousticness 0.05 vs. target 0.80 (+0.02)
------------------------------------------------------------------------
```

**Observation:** Tricked it only partly: the single blues/sad song wins on label bonuses (0.81), but #2-#5 are angry/intense songs matched on energy alone. Nothing is both sad and high-energy in the catalog, so the system cannot tell the user that.

### Adversarial: Unknown genre and mood

```text
========================================================================
                          TOP RECOMMENDATIONS                           
Profile: genre=k-pop, mood=dreamy, energy=0.60, valence=0.60, likes_acoustic=False
========================================================================

#1  Velvet Hours  by Sable June
    Score: 0.50 / 1.00   [r&b, romantic]
    Why:
      - energy 0.52 vs. target 0.60 (+0.32)
      - mood mismatch: romantic (+0.00)
      - genre mismatch: r&b (+0.00)
      - valence 0.68 vs. target 0.60 (+0.11)
      - acousticness 0.30 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#2  Island Drift  by Salt & Palm
    Score: 0.49 / 1.00   [reggae, laid-back]
    Why:
      - energy 0.55 vs. target 0.60 (+0.33)
      - mood mismatch: laid-back (+0.00)
      - genre mismatch: reggae (+0.00)
      - valence 0.78 vs. target 0.60 (+0.10)
      - acousticness 0.45 vs. target 0.20 (+0.06)
------------------------------------------------------------------------

#3  Night Drive Loop  by Neon Echo
    Score: 0.48 / 1.00   [synthwave, moody]
    Why:
      - energy 0.75 vs. target 0.60 (+0.30)
      - mood mismatch: moody (+0.00)
      - genre mismatch: synthwave (+0.00)
      - valence 0.49 vs. target 0.60 (+0.11)
      - acousticness 0.22 vs. target 0.20 (+0.08)
------------------------------------------------------------------------

#4  Concrete Crown  by Rhyme Atlas
    Score: 0.47 / 1.00   [hip hop, confident]
    Why:
      - energy 0.78 vs. target 0.60 (+0.29)
      - mood mismatch: confident (+0.00)
      - genre mismatch: hip hop (+0.00)
      - valence 0.62 vs. target 0.60 (+0.12)
      - acousticness 0.08 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#5  Rooftop Lights  by Indigo Parade
    Score: 0.46 / 1.00   [indie pop, happy]
    Why:
      - energy 0.76 vs. target 0.60 (+0.29)
      - mood mismatch: happy (+0.00)
      - genre mismatch: indie pop (+0.00)
      - valence 0.81 vs. target 0.60 (+0.09)
      - acousticness 0.35 vs. target 0.20 (+0.07)
------------------------------------------------------------------------
```

**Observation:** Neither label exists in the catalog, so the 0.45 of label weight is dead and ranking falls to energy/valence closeness. Results are plausible but arbitrary, and the output never says the labels were unrecognized.

### Adversarial: Out-of-range values (energy 1.8, valence -0.5)

```text
========================================================================
                          TOP RECOMMENDATIONS                           
Profile: genre=pop, mood=happy, energy=1.80, valence=-0.50, likes_acoustic=False
========================================================================

#1  Sunrise City  by Neon Echo
    Score: 0.49 / 1.00   [pop, happy]
    Why:
      - energy 0.82 vs. target 1.80 (+0.01)
      - mood match: happy (+0.25)
      - genre match: pop (+0.20)
      - valence 0.84 vs. target -0.50 (+-0.04)
      - acousticness 0.18 vs. target 0.20 (+0.08)
------------------------------------------------------------------------

#2  Gym Hero  by Max Pulse
    Score: 0.28 / 1.00   [pop, intense]
    Why:
      - energy 0.93 vs. target 1.80 (+0.05)
      - mood mismatch: intense (+0.00)
      - genre match: pop (+0.20)
      - valence 0.77 vs. target -0.50 (+-0.03)
      - acousticness 0.05 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#3  Rooftop Lights  by Indigo Parade
    Score: 0.27 / 1.00   [indie pop, happy]
    Why:
      - energy 0.76 vs. target 1.80 (+-0.01)
      - mood match: happy (+0.25)
      - genre mismatch: indie pop (+0.00)
      - valence 0.81 vs. target -0.50 (+-0.04)
      - acousticness 0.35 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#4  Cathedral of Static  by Iron Veil
    Score: 0.16 / 1.00   [metal, angry]
    Why:
      - energy 0.97 vs. target 1.80 (+0.06)
      - mood mismatch: angry (+0.00)
      - genre mismatch: metal (+0.00)
      - valence 0.25 vs. target -0.50 (+0.03)
      - acousticness 0.03 vs. target 0.20 (+0.07)
------------------------------------------------------------------------

#5  Storm Runner  by Voltline
    Score: 0.11 / 1.00   [rock, intense]
    Why:
      - energy 0.91 vs. target 1.80 (+0.04)
      - mood mismatch: intense (+0.00)
      - genre mismatch: rock (+0.00)
      - valence 0.48 vs. target -0.50 (+0.00)
      - acousticness 0.10 vs. target 0.20 (+0.07)
------------------------------------------------------------------------
```

**Observation:** No input validation: scores collapse (top is 0.49, last is 0.11) and the 'closest' songs are just the highest-energy ones. It still returns results instead of rejecting the profile.

### Adversarial: Dead-center middle (0.5 everywhere)

```text
========================================================================
                          TOP RECOMMENDATIONS                           
Profile: genre=jazz, mood=relaxed, energy=0.50, valence=0.50, likes_acoustic=True
========================================================================

#1  Coffee Shop Stories  by Slow Stereo
    Score: 0.92 / 1.00   [jazz, relaxed]
    Why:
      - energy 0.37 vs. target 0.50 (+0.30)
      - mood match: relaxed (+0.25)
      - genre match: jazz (+0.20)
      - valence 0.71 vs. target 0.50 (+0.09)
      - acousticness 0.89 vs. target 0.80 (+0.07)
------------------------------------------------------------------------

#2  Dust Road Lullaby  by Hollow Pines
    Score: 0.52 / 1.00   [country, nostalgic]
    Why:
      - energy 0.45 vs. target 0.50 (+0.33)
      - mood mismatch: nostalgic (+0.00)
      - genre mismatch: country (+0.00)
      - valence 0.58 vs. target 0.50 (+0.11)
      - acousticness 0.81 vs. target 0.80 (+0.08)
------------------------------------------------------------------------

#3  Midnight Coding  by LoRoom
    Score: 0.51 / 1.00   [lofi, chill]
    Why:
      - energy 0.42 vs. target 0.50 (+0.32)
      - mood mismatch: chill (+0.00)
      - genre mismatch: lofi (+0.00)
      - valence 0.56 vs. target 0.50 (+0.11)
      - acousticness 0.71 vs. target 0.80 (+0.07)
------------------------------------------------------------------------

#4  Focus Flow  by LoRoom
    Score: 0.50 / 1.00   [lofi, focused]
    Why:
      - energy 0.40 vs. target 0.50 (+0.32)
      - mood mismatch: focused (+0.00)
      - genre mismatch: lofi (+0.00)
      - valence 0.59 vs. target 0.50 (+0.11)
      - acousticness 0.78 vs. target 0.80 (+0.08)
------------------------------------------------------------------------

#5  Porch Light Blues  by Delta Marlow
    Score: 0.48 / 1.00   [blues, sad]
    Why:
      - energy 0.40 vs. target 0.50 (+0.32)
      - mood mismatch: sad (+0.00)
      - genre mismatch: blues (+0.00)
      - valence 0.28 vs. target 0.50 (+0.09)
      - acousticness 0.74 vs. target 0.80 (+0.08)
------------------------------------------------------------------------
```

**Observation:** Nothing matches strongly, so the genre (jazz) and mood (relaxed) bonuses decide; the top-5 is a mix of mid-energy songs from unrelated genres.

### Adversarial: Mood/genre clash: metal + chill

```text
========================================================================
                          TOP RECOMMENDATIONS                           
Profile: genre=metal, mood=chill, energy=0.30, valence=0.60, likes_acoustic=True
========================================================================

#1  Library Rain  by Paper Lanterns
    Score: 0.78 / 1.00   [lofi, chill]
    Why:
      - energy 0.35 vs. target 0.30 (+0.33)
      - mood match: chill (+0.25)
      - genre mismatch: lofi (+0.00)
      - valence 0.60 vs. target 0.60 (+0.12)
      - acousticness 0.86 vs. target 0.80 (+0.08)
------------------------------------------------------------------------

#2  Spacewalk Thoughts  by Orbit Bloom
    Score: 0.78 / 1.00   [ambient, chill]
    Why:
      - energy 0.28 vs. target 0.30 (+0.34)
      - mood match: chill (+0.25)
      - genre mismatch: ambient (+0.00)
      - valence 0.65 vs. target 0.60 (+0.11)
      - acousticness 0.92 vs. target 0.80 (+0.07)
------------------------------------------------------------------------

#3  Midnight Coding  by LoRoom
    Score: 0.75 / 1.00   [lofi, chill]
    Why:
      - energy 0.42 vs. target 0.30 (+0.31)
      - mood match: chill (+0.25)
      - genre mismatch: lofi (+0.00)
      - valence 0.56 vs. target 0.60 (+0.12)
      - acousticness 0.71 vs. target 0.80 (+0.07)
------------------------------------------------------------------------

#4  Focus Flow  by LoRoom
    Score: 0.51 / 1.00   [lofi, focused]
    Why:
      - energy 0.40 vs. target 0.30 (+0.31)
      - mood mismatch: focused (+0.00)
      - genre mismatch: lofi (+0.00)
      - valence 0.59 vs. target 0.60 (+0.12)
      - acousticness 0.78 vs. target 0.80 (+0.08)
------------------------------------------------------------------------

#5  Coffee Shop Stories  by Slow Stereo
    Score: 0.51 / 1.00   [jazz, relaxed]
    Why:
      - energy 0.37 vs. target 0.30 (+0.33)
      - mood mismatch: relaxed (+0.00)
      - genre mismatch: jazz (+0.00)
      - valence 0.71 vs. target 0.60 (+0.11)
      - acousticness 0.89 vs. target 0.80 (+0.07)
------------------------------------------------------------------------
```

**Observation:** Mood (0.25) plus low-energy closeness outweighs the 0.20 genre bonus, so metal is ignored entirely. The only metal song (Cathedral of Static) never appears. Mood can override genre.

---

## Experiment: Weight Shift (energy x2, genre x0.5)

**Change:** energy `0.35 -> 0.70`, genre `0.20 -> 0.10`; mood, valence and acousticness unchanged. The weights now sum to 1.30, so scores can exceed 1.00; only the *ranking* is compared. The change was applied temporarily in a throwaway script (`WEIGHTS` in `src/recommender.py` is untouched). Top 5 per profile, baseline vs. shifted:

```text
== High-Energy Pop
  baseline: Sunrise City 0.98, Rooftop Lights 0.76, Gym Hero 0.71, Fiesta Sol 0.53, Pulse Garden 0.51
  shifted : Sunrise City 1.22, Rooftop Lights 1.07, Gym Hero 0.93, Fiesta Sol 0.86, Pulse Garden 0.82
  same order: True
== Chill Lofi
  baseline: Library Rain 0.99, Midnight Coding 0.97, Spacewalk Thoughts 0.76, Focus Flow 0.73, Coffee Shop Stories 0.52
  shifted : Library Rain 1.24, Midnight Coding 1.19, Spacewalk Thoughts 1.08, Focus Flow 0.96, Coffee Shop Stories 0.86
  same order: True
== Deep Intense Rock
  baseline: Storm Runner 0.98, Gym Hero 0.74, Cathedral of Static 0.5, Pulse Garden 0.48, Night Drive Loop 0.48
  shifted : Storm Runner 1.23, Gym Hero 1.09, Cathedral of Static 0.83, Pulse Garden 0.83, Fiesta Sol 0.81
  same order: False
== Conflicting: high energy + sad
  baseline: Porch Light Blues 0.81, Cathedral of Static 0.46, Storm Runner 0.46, Night Drive Loop 0.42, Gym Hero 0.41
  shifted : Porch Light Blues 0.89, Storm Runner 0.8, Cathedral of Static 0.78, Fiesta Sol 0.75, Gym Hero 0.75
  same order: False
== Unknown genre and mood
  baseline: Velvet Hours 0.5, Island Drift 0.49, Night Drive Loop 0.48, Concrete Crown 0.47, Rooftop Lights 0.46
  shifted : Velvet Hours 0.83, Island Drift 0.82, Night Drive Loop 0.78, Concrete Crown 0.76, Rooftop Lights 0.75
  same order: True
== Out-of-range values (energy 1.8, valence -0.5)
  baseline: Sunrise City 0.49, Gym Hero 0.28, Rooftop Lights 0.27, Cathedral of Static 0.16, Storm Runner 0.11
  shifted : Sunrise City 0.4, Rooftop Lights 0.25, Gym Hero 0.23, Cathedral of Static 0.22, Storm Runner 0.15
  same order: False
== Dead-center middle (0.5 everywhere)
  baseline: Coffee Shop Stories 0.92, Dust Road Lullaby 0.52, Midnight Coding 0.51, Focus Flow 0.5, Porch Light Blues 0.48
  shifted : Coffee Shop Stories 1.13, Dust Road Lullaby 0.85, Midnight Coding 0.83, Velvet Hours 0.82, Focus Flow 0.82
  same order: False
== Mood/genre clash: metal + chill
  baseline: Library Rain 0.78, Spacewalk Thoughts 0.78, Midnight Coding 0.75, Focus Flow 0.51, Coffee Shop Stories 0.51
  shifted : Spacewalk Thoughts 1.12, Library Rain 1.11, Midnight Coding 1.05, Coffee Shop Stories 0.83, Focus Flow 0.83
  same order: False
```

**What changed**

- The three realistic profiles were stable. Pop and Lofi kept the identical top 5 in the same order. Rock kept its top 4 and swapped #5 (Night Drive Loop -> Fiesta Sol, a latin/euphoric song that is merely high-energy). Their labels (mood plus genre) still dominate, so the system is not very sensitive to energy for users with clear tastes.
- Edge cases were where it moved. For "high energy + sad," Storm Runner (rock/intense) overtook Cathedral of Static, and Fiesta Sol (latin/euphoric, the opposite of sad) entered the top 5. Extra energy weight pulls the "sad" user toward happy-sounding loud songs, the wrong direction.
- For "metal + chill," Spacewalk Thoughts and Library Rain swapped #1/#2. For "dead-center," Velvet Hours (r&b) entered the top 5 on energy fit alone.
- Out-of-range energy (1.8) got worse: the top score fell from 0.49 to 0.40, since a bigger weight multiplies a bigger error.
- Halving genre mostly shrinks a bonus that rarely decided anything, but it weakens the only signal for rare genres. With a 19-song catalog (one song per most genres) genre barely affects results either way.

**Takeaway:** the baseline is robust where labels agree with the numbers, but heavier energy weight makes results more "vibe-matched" and less faithful to stated mood, which hurts users with conflicting preferences. Doubling energy is not clearly better; I'd keep the original weights.
