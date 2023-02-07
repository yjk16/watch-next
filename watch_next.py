# This program will take in the description of a movie, then using spacy,
# compare this description with the descriptions of other movies in a list and return the title of the closest match.

# Had help from my friend Silas with things including error handling.
# Used lots of websites to get through this including geeksforgeeks.org.

import spacy
from movie import Movie
nlp = spacy.load('en_core_web_md')


def watch_next(watched_movie_description):
    """
    Take in the description of a movie, compare it to a list of other descriptions and return the closest match.

    :param watched_movie_description: description of the movie to be compared to

    :return: the title of the closest match
    """

    list_of_movies = []

    f = open("movies.txt", "r")
    for lines in f.readlines():
        line = lines.strip().split(":")

        # Creating movie objects
        movie_object = Movie(line[0], line[1], 'none')
        description = movie_object.description

        # Creating a list of the objects
        list_of_movies.append(movie_object)

        # Using nlp for the watched movie description and creating a variable name for this
        nlp_watched_movie = nlp(watched_movie_description)

        # Comparing the descriptions of the movies in the list to the description of the watched movie
        similarity = nlp(description).similarity(nlp_watched_movie)

        # Changing the values of similarity for the objects
        movie_object.similarity = f"{similarity}"

        from operator import attrgetter

        # Finding the max for the similarities
        max_similarity = max(list_of_movies, key=attrgetter('similarity'))

    f.close()

    # Returning the title of the movie object with the max similarity
    return max_similarity.title


planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
              "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in " \
              "peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a " \
              "gladiator."

print(f"The title of the movie which best matches the description of your watched movie is: {watch_next(planet_hulk)}")
