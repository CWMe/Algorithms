# Movie Recommendation System  

This is a Python script that recommends movies to users based on their similarity to other users. The script reads a CSV file containing user movie preferences and suggests two movies that a user hasn't watched yet, based on their most similar match.  

## Challenge Statement  

Given a CSV file where each row represents a person and the movies they like, the goal is to:  
1. Find the most similar person for each user based on shared movie preferences (using Jaccard Similarity).  
2. Recommend **two movies** that the user **has not watched yet** but are liked by their most similar match.  

## How It Works  

1. The script reads a CSV file with the following structure:  

   | Name?  | Please Check All the Movies You've Liked! |  
   |--------|------------------------------------------|  
   | John   | Movie1; Movie2; Movie3                  |  
   | Alice  | Movie2; Movie3; Movie4                  |  
   | Bob    | Movie1; Movie3; Movie5                  |  

2. It calculates the **Jaccard Similarity** between each pair of users.  
3. It finds the **best match** for each user (highest similarity score).  
4. It suggests up to **two movies** that the user **hasn't seen yet** but are liked by their best match.  

## Installation & Usage  

### Prerequisites  

- Python 3  
- A CSV file with user preferences  

### Running the Script  

1. Save your CSV file in the same directory as the script.  
2. Run the script using:  

```bash
python3 Recommendation.py your_file.csv
```

Run this following command 


The output looks like this:
```

Recommendation for Internet Bot: Most similar to Paulo with score 0.44.
Recommended Movies: The Lord of the Rings: The Return of the King, Avatar

Recommendation for Milu: Most similar to Shijit Dasgupta with score 0.43.
Recommended Movies: The 40 Year Old Virgin, Superbad

Recommendation for John: Most similar to Alex with score 0.50.
Recommended Movies: Avatar, Inception

Recommendation for Alex: Most similar to John with score 0.50.
Recommended Movies: Matrix Reloaded

Recommendation for Paulo: Most similar to A H with score 0.54.
Recommended Movies: The 40 Year Old Virgin, The Room

Recommendation for A H: Most similar to Paulo with score 0.54.
Recommended Movies: Avatar

Recommendation for Jason: Most similar to Alex with score 0.29.
Recommended Movies: Avatar, Mean Girls

Recommendation for Vale: Most similar to Alex with score 0.44.
Recommended Movies: Mean Girls, Inception

Recommendation for Fabio: Most similar to Pavel with score 0.60.
Recommended Movies: The 40 Year Old Virgin, The Dark Knight

Recommendation for Shijit Dasgupta: Most similar to Milu with score 0.43.
Recommended Movies: Avatar

Recommendation for Calvin: Most similar to Nick with score 0.40.
Recommended Movies: Matrix Reloaded, Avatar

Recommendation for Bob: Most similar to John with score 0.50.
Recommended Movies: Movie5

```
