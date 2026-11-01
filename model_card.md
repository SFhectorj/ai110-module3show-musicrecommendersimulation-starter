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

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

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
