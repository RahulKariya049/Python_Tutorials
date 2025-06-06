# You have a list of movie records, each as a dictionary:

Data = [
    {"title": "Inception", "year": 2010, "genres": ["Action", "Sci-Fi"], "rating": 8.8},
    {"title": "The Matrix", "year": 1999, "genres": ["Action", "Sci-Fi"], "rating": 8.7},
    {"title": "Interstellar", "year": 2014, "genres": ["Adventure", "Drama", "Sci-Fi"], "rating": 8.6},
    {"title": "The Godfather", "year": 1972, "genres": ["Crime", "Drama"], "rating": 9.2},
    {"title": "Pulp Fiction", "year": 1994, "genres": ["Crime", "Drama"], "rating": 8.9},
    {"title": "The Dark Knight", "year": 2008, "genres": ["Action", "Crime", "Drama"], "rating": 9.0},
]

# Tasks (try to do each in one line using comprehensions where possible):

# Create a list of movie titles released after 2000.
# Create a set of all unique genres across all movies.
# Create a dictionary that maps each movie title to its rating.
# Create a generator that yields movie titles which have a rating above 9.0.

# Flatten the genres into a list (not set) of all genres from all movies (with duplicates).
# Create a dictionary mapping each genre to the number of movies in that genre.

movies = [dict['title'] for dict in Data if dict['year'] > 2000]
print(movies)

unique_genres = {item for dic in Data for item in dic.get('genres')}
print(unique_genres)

movie_rating = { dic.get('title') : dic.get('rating') for dic in Data }  
print(movie_rating)

generator = (dic.get('title') for dic in Data if dic.get('rating') > 9.0)
print(list(generator))

genres = [genre for dic in Data for genre in dic.get('genres')]
print(genres)


# Counter Function
from collections import Counter

data = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana']
counted = Counter(data)
print(counted)

genre_movie = dict(Counter([genre for dic in Data for genre in dic.get('genres')]))
print(genre_movie)
