# Movie Recommendation System  

This is a javascript program that recommends movies to users based on their similarity to other users. The script reads a JSON file containing user movie and category preferences and suggests three movies that a user hasn't watched yet, based on their most similar matches.  

## How It Works  

1. The script reads a JSON file, `movies.json`, with the following structure:  

```json
[
 {
  "name":"John",
  "categories":["Sci/Fi","Comedy"],
  "movies":["Matrix Reloaded","Inception","Minority Report","Superbad"]
 },
 {
  "name":"Jason",
  "categories":["Comedy","Drama"],
  "movies":["The Room","Lars and the Real Girl","Minority Report","Zardoz"]
 }
]
```

2. It calculates the **Jaccard Similarity** between each pair of users, for both their movie preferences and category preferences.
3. The sum of both is claculated as the user simularity 
4. For each user it finds the three most similar other users in the set 
5. For each user it suggests three movies that were most liked among the user's neighbors which the user did not already select

## Installation & Usage  

### Prerequisites  

- NodeJS or similar javascript runtime
- A JSON file with user preferences
- Install dependencies with `npm i`

### Running the Script   

- Start the NodeJS REPL, or similar system
- Require the movies.js module with
```javascript
const movies = require('./movies.js');
```
- Execute the run function
```javascript
movies.run()
```

### Output

```
Internet Bot:
    The Lord of the Rings: The Return of the King
    The Dark Knight
    The Departed
Jason:
    Matrix Reloaded
    Inception
    Avatar
John:
    Avatar
    Inception
    Minority Report
```
