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

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

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

The `+2.0` genre and `+1.0` exact mood bonuses can create a filter bubble, repeatedly favoring users whose favorite labels are well represented and causing related or cross-genre songs to rank lower. Because the catalog has only 18 songs and stronger genre coverage for categories such as lofi and pop, users who prefer genres with fewer or no exact matches receive less variety. The energy calculation rewards closeness but clamps every gap score at zero, so it does not distinguish a modest mismatch from a large mismatch after the first unit of distance. Mood matching also ignores related moods, and the `0.50` acousticness cutoff is a rough preference rule that can ignore nuanced tastes.

---

## 7. Evaluation  

We tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a conflicting blues/sad/high-energy case. High-Energy Pop and Chill Lofi confirmed that a matching genre and mood can strongly lead the list; Library Rain and Midnight Coding ranked at the top for Lofi, while Sunrise City led for Pop.

High-Energy Pop and Deep Intense Rock both receive high-energy recommendations, but Gym Hero appears more strongly for Pop because it matches the pop genre, whereas it only matches the intense mood for the Rock profile. This is the main reason Gym Hero can appear for a user who wants Happy Pop: it is a pop song with high energy, even though its mood is intense rather than happy.

Chill Lofi and Deep Intense Rock produced nearly opposite recommendations because their genre, mood, and energy preferences differ. The Lofi profile favored quiet acoustic songs around `0.35–0.42` energy, while Rock favored Storm Runner at `0.91` energy. High-Energy Pop and the conflicting sad/high-energy profile differed because Pop had a direct genre and mood match, while the edge profile had no catalog song labeled `sad`; therefore, the blues genre match in Velvet Smoke outweighed its imperfect mood and energy combination.

The main surprise was that exact mood matching can leave a strong genre or energy result ranked first even when the user's emotional preference is missing. The weight-shift test, which halved genre and doubled energy, kept Sunrise City first but changed the surrounding order, showing that energy primarily affects variety and tie-breaking while genre and mood still establish a clear leader.

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
