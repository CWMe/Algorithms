import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
from collections import defaultdict
import math

def common_movies_vector(m1, m2):
    result = []
    for i in range(len(m1)):
        result.append(m1[i] & m2[i])
    return result

def encode(movies, all_movies):
    result = []
    for movie in all_movies:
        if movie in movies:
            result.append(1)
        else:
            result.append(0)
    return result

def decode(mv, all_movies):
    result = []
    for i,n in enumerate(mv):
        if n == 1:
            result.append(all_movies[i])
    return result

def knn_recommendations(movie_list, all_movies, num_neighbors):
    # Create a dictionary to store movie recommendations for each person
    recommendations = defaultdict(list)

    # Calculate the similarity between each pair of users and movies
    similarities = {}
    for user in movie_list:
        similarities[user] = {}
        for other_user in movie_list:
            if user != other_user:
                common_movies = common_movies_vector(movie_list[user],movie_list[other_user])
                similarity = 1 - cosine(np.array([*common_movies]), np.array(movie_list[other_user]))
                similarities[user][other_user] = similarity if not math.isnan(similarity) else 0

    # Find the K nearest neighbors for each user
    neighbors = defaultdict(list)
    for user in movie_list:
        user_similarities = sorted(similarities[user].items(), key=lambda x: x[1], reverse=True)
        knn_users = [(user, similarity) for user, similarity in user_similarities[:num_neighbors]]
        # Get the recommendations from the K nearest neighbors
        for neighbor, similarity in knn_users:
            common_movies = set(decode(movie_list[user], all_movies)) & set(decode(movie_list[neighbor], all_movies))
            recommendations[user].extend(set(decode(movie_list[neighbor], all_movies)) - common_movies)
            neighbors[user].append((neighbor, similarity))

    return {user: (recommendations[user], neighbors[user]) for user in recommendations}

# Example usage:
# movie_list = {
#     'Alice': ['Movie1', 'Movie2', 'Movie3'],
#     'Bob': ['Movie2', 'Movie3', 'Movie4'],
#     'Charlie': ['Movie1', 'Movie2', 'Movie5'],
# }

# Load data from csv, using pandas
movie_list = {}
df = pd.read_csv("CWM_Recommendation_Results.csv")
for row in df.iterrows():
    movie_list[row[1]["Name?"]] = row[1]["Please Check All the Movies You've Liked!"].strip().split(";")

# Create a list of all movies for one hot encoding
all_movies = set()
for k in movie_list:
    all_movies = all_movies | set(movie_list[k])
all_movies = list(all_movies)
all_movies.sort()


num_neighbors = 2
# Encode the movies for processing and use that to do KNN
recommendations = knn_recommendations({k: encode(movie_list[k], all_movies) for k in movie_list}, all_movies, num_neighbors)

# Show results
for name, data in recommendations.items():
    reco, neighbors = data
    neighbor_info = ", ".join(f"{name}({sim:.2f})" for name,sim in neighbors)
    print(f"Recommend {name} watch {reco} based on neighbors {neighbor_info}")
