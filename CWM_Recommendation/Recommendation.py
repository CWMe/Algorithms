import csv
import os

# Ask for file name from the user
file_path = input("Enter the CSV file name (with extension): ").strip()

# Check if file exists
if not os.path.isfile(file_path):
    print("Error: File not found. Please check the file name and try again.")
    exit()

# Load CSV into dictionary
directory = {}

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    # Debug: Print column names to ensure correctness
    print("Detected Columns:", reader.fieldnames)

    for row in reader:
        name = row.get("Name?", "").strip()  # Ensure correct column name and remove spaces
        movies = [movie.strip() for movie in row.get("Please Check All the Movies You've Liked!", "").split(",") if movie.strip()]
        
        if name and movies:  # Only store if valid data exists
            directory[name] = set(movies)

# Debug: Print loaded dictionary
print("\nLoaded Data:")
for name, movies in directory.items():
    print(f"{name}: {movies}")

# Check if data is empty
if not directory:
    print("Error: No valid data found in the CSV file. Please check the file content.")
    exit()

# Similarity function using Jaccard Index
def howsimilar(lista, listb):
    set_a, set_b = set(lista), set(listb)
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    similarity = intersection / union if union != 0 else 0
    return similarity

# Finding the most similar person and recommending a movie
sim_scores = {}
recommendations = []

for person, movies in directory.items():
    best_match = None
    highest_score = 0

    print(f"\nChecking recommendations for: {person}")

    for other_person, other_movies in directory.items():
        if person == other_person:
            continue  # Skip self-comparison

        score = howsimilar(movies, other_movies)

        print(f"  Comparing with {other_person}: Similarity Score = {score:.2f}")

        if score > highest_score:
            highest_score = score
            best_match = other_person

    sim_scores[person] = (best_match, highest_score)

    # Recommend a movie from best_match that person hasn't seen
    if best_match:
        recommended_movies = directory[best_match] - movies
        print(f"  Best Match: {best_match} (Score: {highest_score:.2f})")
        print(f"  Unseen Movies from {best_match}: {recommended_movies}")

        if recommended_movies:
            recommendation = next(iter(recommended_movies))
            recommendations.append(f"Hey {person}, you might like '{recommendation}' based on {best_match}'s taste!")
        else:
            print(f"  No new movies to recommend for {person}. They have already seen all of {best_match}'s movies.")

# Output the recommendations
print("\nMovie Recommendations:")
if recommendations:
    for rec in recommendations:
        print(rec)
else:
    print("No recommendations could be generated. Check if there are enough shared movie preferences.")

