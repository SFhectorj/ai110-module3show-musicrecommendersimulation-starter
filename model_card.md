# 🎧 Model Card: VibeFinder 1.0

## 1. Model Name  

**VibeFinder 1.0**

A small, rule-based music recommender. It matches songs to a listener's "vibe."

---

## 2. Intended Use  

**Goal:** Suggest the 5 songs from a small catalog that best fit a listener's taste.

**What it predicts:** a "fit" score from 0 to 1 for every song. The highest scores are shown first.

**Intended use:**

- Classroom learning. It shows how a recommender turns data into a ranked list.
- Small experiments, like changing the weights to see what happens.

**Assumptions about the user:**

- They can say their favorite genre and mood.
- They can give a target for energy and positivity.
- They know if they like acoustic music.

**Not intended for:**

- Real music apps or real users.
- Anything that needs fair or well-tested results. The catalog is tiny.
- Guessing a person's taste from their history. It only uses what they type in.
- Decisions about artists, such as who gets exposure or pay.

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

- **Size:** 19 songs in `data/songs.csv`. I did not add or remove any. This is the starter data.
- **Columns:** title, artist, genre, mood, energy, tempo, valence, danceability, acousticness.
- **Used in scoring:** genre, mood, energy, valence and acousticness. Tempo and danceability are ignored.
- **Genres:** 16 kinds. Lofi has 3 songs and pop has 2. Every other genre has 1.
- **Moods:** 15 kinds. Chill has 3 songs and happy and intense have 2 each. Every other mood has 1.
- **Energy gap:** 10 songs are at 0.55 or below, and 9 are at 0.75 or above. Nothing sits between 0.56 and 0.74.
- **Missing:** lyrics, language, artist popularity, release year, and any listening history. It has no world music beyond a few genres.

---

## 5. Strengths  

- It works well when the user's labels and numbers agree. Examples are High-Energy Pop, Chill Lofi and Deep Intense Rock.
- Different tastes give very different lists. Lofi and Rock share no songs.
- The top pick was what I expected each time: Sunrise City, Library Rain and Storm Runner.
- Every score comes with reasons, so it is easy to see why a song ranked where it did.
- Mood and genre act as a good tiebreaker when two songs have similar energy.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users  


**Weakness found in experiments:** The system trusts exact-match labels too much, so users with conflicting or unusual preferences get confident but poor results. Genre and mood together are worth 45% of the score, but the 19-song catalog has only one song for most genres and moods, and nothing that is both sad and high-energy. For the "high energy + sad" profile, the single blues/sad song won at 0.81, while the rest of the top 5 were angry or intense songs scoring only about 0.4, matched on energy alone. When I doubled the energy weight, a euphoric latin song entered that user's top 5, the opposite of what they asked for. The output never signals that the match is weak, so the user can't tell the recommendations are filler.  

**Other patterns I saw:**

- Genre and mood must match exactly. "Indie pop" gets no credit for "pop."
- Lofi and chill have 3 songs each. Most other tastes have 1. Lofi fans get more choice.
- The catalog has a hole in the middle of the energy range. Mid-energy listeners get weaker matches.
- Mellow, acoustic songs show up in more lists than loud ones. Spacewalk Thoughts appeared in about 2.7 times as many top-5 lists as Pulse Garden in my 7,200-profile sweep.
- Gym Hero shows up for many people. It is close enough on many traits to beat songs that are exact on only one.
- Bad input, such as energy 1.8, is not rejected. The system just returns low scores.
- There is no variety rule. A pop fan can get several pop songs in a row.

---

## 7. Evaluation  

**Summary:** I tested 8 profiles. Three were normal: High-Energy Pop, Chill Lofi and Deep Intense Rock. Five were tricky: conflicting taste, unknown labels, impossible numbers, all-middle values, and metal plus chill. I also ran one experiment that doubled energy and halved genre. Then I compared the lists for each pair of profiles.

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

1. **Add more songs.** Fill the energy gap and add more genres and moods. Aim for at least a few songs per label.
2. **Give partial credit.** "Indie pop" should count a little for "pop." "Melancholy" should count a little for "sad."
3. **Mix up the top 5.** Limit the list to two songs per genre so it is not all the same.
4. **Warn on weak matches.** If the best score is low, say so. Reject impossible values such as energy 1.8.
5. **Make acousticness a number.** Right now it is only "likes it" or "doesn't."

---

## 9. Personal Reflection  

- **What I learned:** A recommender is just math on labels and numbers. The weights decide what "a good match" means.
- **How AI Helped:** I used AI mainly to help give me ideas for the scoring and ranking code. I also used it for testing profiles and edge cases. After reviewing the AI comparison notes I caught two errors, which seemed like the AI just guessed or assumed an output which I corrected against the actual output.
- **What surprised me:** One song, Gym Hero, kept showing up for different people. A song that is close on everything can beat a song that is exact on one thing.
- **How it changed my view:** The data matters as much as the code. A small catalog gives biased results, even with a fair formula.
- **Real apps:** Big apps likely face the same problem on a larger scale. Songs and tastes with less data get less attention.
