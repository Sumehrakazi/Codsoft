import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Sample movie data
movies = [
    "The Matrix (Action, Sci-Fi)",
    "The Godfather (Crime, Drama)",
    "Inception (Action, Adventure, Sci-Fi)",
    "The Dark Knight (Action, Drama)",
    "Pulp Fiction (Crime, Drama)",
    "Interstellar (Adventure, Drama, Sci-Fi)",
    "Gladiator (Action, Adventure, Drama)"
]

# User's favorite movie
favorite_movie = "Inception (Action, Adventure, Sci-Fi)"

# Step 1: Create a CountVectorizer to convert text data into vectors
vectorizer = CountVectorizer().fit_transform(movies)
vectors = vectorizer.toarray()

# Step 2: Calculate the cosine similarity between all movie vectors
cosine_sim = cosine_similarity(vectors)

# Find the index of the user's favorite movie
fav_movie_index = movies.index(favorite_movie)

# Step 3: Get similarity scores for the favorite movie
similarity_scores = list(enumerate(cosine_sim[fav_movie_index]))

# Step 4: Sort movies by similarity scores (excluding the favorite movie)
similar_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]

# Step 5: Recommend top 3 similar movies
print("Because you liked:", favorite_movie)
print("You might also like:")
for i, score in similar_movies[:3]:
    print(f"- {movies[i]} (similarity: {score:.2f})")