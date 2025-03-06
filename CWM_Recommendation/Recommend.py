import csv
import os
import argparse

# Set up argparse to accept command-line arguments
parser = argparse.ArgumentParser(description="Movie Recommendation System")
parser.add_argument("filename", help="CSV file name (with extension)")

# Parse the arguments
args = parser.parse_args()

# Get the filename from the command-line argument
file_path = args.filename.strip()

# Check if the file exists
if not os.path.isfile(file_path):
    print("Error: File not found. Please check the file name and try again.")
    exit()

# Load CSV into dictionary
directory = {}

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row.get("Name?", "").strip()
        movies = [movie.strip() for movie in row.get("Please Check All the Movies You've Liked!", "").split(";") if movie.strip()]

        if name and movies:
            directory[name] = set(movies)

# Check if data is empty
if not directory:
    print("Error: No valid data found in the CSV file.")
    exit()

# Similarity function using Jaccard Index
def howsimilar(lista, listb):
    set_a, set_b = set(lista), set(listb)
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union != 0 else 0

# Finding the most similar person and recommending movies not already watched
for person, movies in directory.items():
    best_match = None
    highest_score = 0
    recommended_movies = []

    for other_person, other_movies in directory.items():
        if person != other_person:
            score = howsimilar(movies, other_movies)
            if score > highest_score:
                highest_score = score
                best_match = other_person
                # Get the common movies between the two people
                recommended_movies = list(other_movies - movies)  # Only recommend movies that the person hasn't watched

    # Recommend the best match and movies the person hasn't watched yet
    if best_match and recommended_movies:
        # Get two movies, or as many as possible if fewer than 2 non-watched common movies
        top_movies = recommended_movies[:2]
        print(f"Recommendation for {person}: Most similar to {best_match} with score {highest_score:.2f}.")
        print(f"Recommended Movies: {', '.join(top_movies)}\n")

