# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

**The big idea:** the recommender gives every song in the catalog a "how well does this fit you?" grade from 0 to 1, then lists the highest-graded songs first. It never learns or guesses. It just compares each song to what you told it you like, one trait at a time, and adds up the points.

**What it knows about you:** your favorite genre, your favorite mood, how energetic you want the music to feel, how bright and positive you want it to sound, and whether you like acoustic (more "unplugged") music.

**What it knows about each song:** its genre, its mood, and three 0-to-1 measures: energy (calm to intense), valence (sad or dark to cheerful), and acousticness (electronic to unplugged). Tempo and danceability are in the data but not used, because they mostly repeat what energy already says.

**How the points work:** each trait is worth a share of the final grade, and the shares add up to 1.

| Trait | Share of the grade | How it earns points |
|---|---|---|
| Energy | 35% | The closer the song's energy is to what you want, the more of the share it gets. |
| Mood | 25% | All or nothing: full points if the mood is exactly your favorite, zero otherwise. |
| Genre | 20% | All or nothing, the same way. |
| Valence (positivity) | 12% | The closer to the brightness you want, the more it gets. |
| Acousticness | 8% | The closer to what you like (mostly acoustic or mostly not), the more it gets. |

For example, if you want energy 0.80 and a song has 0.82, it is very close, so it gets nearly the whole energy share. If its genre is not your favorite, it gets nothing from the genre share. Add up all five and you have the song's grade.

**Picking the winners:** every song is graded, the list is sorted from highest to lowest, and the top five are shown. Each one comes with a short list of reasons that shows exactly how many points each trait added, including the traits that added nothing, so you can see why a song ranked where it did.

**Choices worth knowing about:**

- Energy counts the most because it is the clearest sign of whether a song suits the moment (workout versus studying). Mood and genre are all-or-nothing bonuses, so a song that matches both will usually beat a song that is only close on energy.
- Genre matching is strict. "Indie pop" does not count as "pop", so a very similar song can lose the genre points.
- The weights are starting guesses, not proven values. Changing them changes the rankings, and that is a good thing to experiment with.
- The starter code only had empty placeholders, so everything above (loading the songs, scoring, ranking and the explanations) is new.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users  


**Weakness found in experiments:** The system trusts exact-match labels too much, so users with conflicting or unusual preferences get confident but poor results. Genre and mood together are worth 45% of the score, but the 19-song catalog has only one song for most genres and moods, and nothing that is both sad and high-energy. For the "high energy + sad" profile, the single blues/sad song won at 0.81, while the rest of the top 5 were angry or intense songs scoring only about 0.4, matched on energy alone. When I doubled the energy weight, a euphoric latin song entered that user's top 5, the opposite of what they asked for. The output never signals that the match is weak, so the user can't tell the recommendations are filler.  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

### Profiles tested

Three realistic listeners and five "trick" listeners (full output is in the README):

| Profile | What it asks for |
|---|---|
| High-Energy Pop | pop, happy, very energetic, bright, not acoustic |
| Chill Lofi | lofi, chill, quiet and mellow, acoustic |
| Deep Intense Rock | rock, intense, very energetic, darker, not acoustic |
| Conflicting (sad + high energy) | blues, sad, very energetic, dark, acoustic |
| Unknown genre and mood | "k-pop" and "dreamy", which are not in the catalog |
| Out-of-range numbers | energy 1.8 and valence -0.5, which are impossible values |
| Dead-center | jazz, relaxed, 0.5 on everything |
| Metal + chill | metal fan who wants quiet, chill, acoustic music |

I looked for two things: do the top 5 match what the profile asked for, and does the score explanation add up to something a person would agree with?

### Profile-by-profile comparisons

**Pop vs. Lofi.** Pop gets Sunrise City, Rooftop Lights and Gym Hero: loud, bright and electronic. Lofi gets Library Rain, Midnight Coding and Spacewalk Thoughts: quiet and acoustic. The two lists share no songs. This makes sense because the profiles sit at opposite ends of energy (0.85 vs. 0.35) and acousticness, so the system is clearly reacting to what we change.

**Pop vs. Rock.** Both want loud songs, so they share Gym Hero and Pulse Garden. The difference is at the top: Pop gets the happy Sunrise City, Rock gets the intense Storm Runner. Mood and genre are the tiebreakers when energy is about the same, which is how it should work.

**Lofi vs. Rock.** These are the most opposite profiles and have zero songs in common. Good: if they overlapped, the system would not be listening to energy at all.

**Why does "Gym Hero" keep showing up for Happy Pop fans?** Gym Hero is a pop song, so it gets the full genre bonus. It is also very high-energy (0.93, and the Pop fan wants 0.85) and has a bright sound, so it earns nearly full marks for those too. The only thing it misses is the "happy" mood, because it is labeled "intense," and that costs only a quarter of the score. Think of a shopping list with five items: Gym Hero ticks four of them. The system has no way to know that "intense gym music" and "happy sunny music" feel different to a person, since it only checks whether the mood labels match exactly. The same song also shows up in the Rock list (#2) because its energy and "intense" mood fit that user. It is a general "loud and punchy" song that fits many profiles, which is why it is everywhere.

**Rock vs. Conflicting (sad + high energy).** Both ask for loud music, and both lists include Storm Runner, Cathedral of Static and Gym Hero. But the Conflicting user gets the quiet blues song Porch Light Blues at #1 (0.81) even though they asked for high energy. The "sad" label and the blues genre are worth more points than the energy mismatch costs. This is the biggest surprise: the profile asked for something that doesn't exist in the catalog, and the system quietly picked the single song that matched the labels instead of saying so.

**Lofi vs. Conflicting.** Both like acoustic music, but Lofi gets calm songs and Conflicting gets one calm blues song then loud ones. This shows that energy is the strongest numeric signal; acoustic preference alone cannot pull a loud-music fan toward quiet songs.

**Pop vs. Unknown genre and mood.** Pop's top score is 0.98. The "k-pop/dreamy" user's best is only 0.50 and all five songs are within 0.04 of each other (Velvet Hours, Island Drift, Night Drive Loop and so on). Since neither label exists, nobody gets the bonus, so the order is effectively decided by small differences in energy. The results look plausible but are close to random, and the program doesn't admit that.

**Pop vs. Out-of-range numbers.** Same genre and mood, but the impossible energy of 1.8 means no song can match well: the top score drops from 0.98 to 0.49. The ranking is still reasonable (high-energy pop songs first), which is a good sign, but the system should have rejected the bad input instead of scoring it.

**Lofi vs. Dead-center.** Both end up with mellow, mid-to-low-energy songs because the catalog is full of them (10 of 19 songs are under 0.56 energy). Dead-center's #1, Coffee Shop Stories (jazz, relaxed), wins on the label bonuses, and Midnight Coding and Focus Flow (both on Lofi's list too) fill #3 and #4. An "average" listener is pushed toward calm music because the catalog has no songs in the middle (nothing between 0.56 and 0.74 energy).

**Rock vs. Metal + chill.** Rock wants loud, intense songs. Metal + chill asks for metal, but also for quiet, chill, acoustic music, so it gets Library Rain and Spacewalk Thoughts and never sees Cathedral of Static, the only metal song. They asked for "metal" and "chill" at once, and chill (mood 0.25 plus low energy) outweighs metal (genre 0.20). That could be correct for someone who wants quiet music tonight, but a real metal fan would feel ignored.

**Lofi vs. Metal + chill.** The top 3 are almost the same songs (Library Rain, Spacewalk Thoughts, Midnight Coding). The "metal" preference had no visible effect, so the genre label is the weakest signal in the score.

### What surprised me

1. A song that matches the *label* beats a song that matches the *numbers*: the sad user at high energy got a quiet blues song first.
2. The three realistic profiles worked well and gave sensible, different lists, but the system does not tell the user when it is guessing (unknown labels, impossible numbers).
3. One song (Gym Hero) fits many different tastes, because the scoring rewards "close enough on everything" over "exactly right on one thing".
4. Doubling the weight on energy (see the README experiment) barely changed realistic profiles but pulled a euphoric song into the "sad" user's list, which showed me how easily the weights can push results the wrong way.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
