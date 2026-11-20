# Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

VibeFinder recommends songs from a small catalog for users who choose a genre, mood, target energy, and acoustic preference. It is designed for classroom demonstration and preference experiments, not for real listener profiling or product decisions.

---

## 3. How the Model Works

The recommender compares each song with a user's taste profile. It gives 2 points for the same genre and 1 point for the same mood. It gives up to 1.5 points when song energy is close to the target energy, and 0.5 points when acousticness agrees with the user's preference. The highest-scoring songs are returned first.

---

## 4. Data

The dataset has 18 songs loaded from `data/songs.csv`. It includes 10 starter songs and 8 added songs across pop, lofi, rock, jazz, ambient, synthwave, indie pop, country, folk, reggae, blues, electronic, metal, classical, and disco. Each song includes genre, mood, and numeric values for energy, tempo, valence, danceability, and acousticness.

The catalog is small and does not cover every genre or mood. It also lacks listening history, popularity, and user ratings.

---

## 5. Strengths

The system works clearly for profiles with genre, mood, and energy values represented in the catalog. It gave reasonable leaders for the Pop, Lofi, and Rock profiles. Sunrise City felt appropriate for Happy Pop, Library Rain and Midnight Coding fit Chill Lofi, and Storm Runner fit Deep Intense Rock.

---

## 6. Limitations and Bias

The +2.0 genre bonus can create a filter bubble and give cross-genre songs lower scores. The catalog overrepresents lofi and pop, so users interested in less common genres have fewer good matches. Exact mood labels miss related moods, and the 0.50 acousticness cutoff is a simple approximation. The energy calculation also rewards close values but does not distinguish every size of mismatch beyond a difference of 1.0.

---

## 7. Evaluation

I tested High-Energy Pop, Chill Lofi, Deep Intense Rock, and a conflicting blues/sad/high-energy profile. Pop and Rock both favored high-energy songs, but Pop also rewarded the pop genre and Rock rewarded intense mood matches. Chill Lofi favored low-energy, acoustic songs instead.

Gym Hero appeared for Happy Pop because it is a pop song with high energy, even though its mood is intense. The sad edge profile had no exact sad mood match, so its blues genre match kept Velvet Smoke first. A weight experiment halved genre and doubled energy; this changed the lower-ranked order but did not clearly improve accuracy.

---

## 8. Future Work

- Use related genre and mood groups instead of exact labels.
- Add tempo, valence, and danceability to the scoring rule.
- Add diversity and listening-history features to reduce repetitive recommendations.

---

## 9. Personal Reflection

The biggest learning moment was seeing how a few score rules can make a result feel personal while still hiding bias. AI tools helped generate and organize repetitive work, but I double-checked formulas, imports, CSV values, and ranking results. I was surprised that simple matching rules could feel convincing, and next I would test larger, more varied data with better mood and diversity features.
