##
# movie_reccomendation.py
# Created: 29.08.19
# Last edit: 06.09.19
# A program that reccommends movies based on an algorithm and other 'users'



class Movies:
    """ Movie class, genres is stored as a list """
    def __init__(self, id, title, year, genres):
        self.id = id
        self.title = title
        self.year = year
        self.genres = genres
        movies.append(self)


class Ratings:
    """ Ratings class joining the user and movie classes with a rating """
    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        ratings.append(self)


class User:
    """
    User class holds the id and a list of all movies liked and disliked
    The liked and disliked lists are initialised on creation of a new user
    Methods to add to liked and disliked lists
    Methods to return the liked and disliked lists as sets
    """

    def __init__(self, id):
        self.id = id
        self.liked = set()
        self.disliked = set()
        users.append(self)

    def add_liked(self, movie_id):
        self.liked.add(movie_id)

    def return_liked(self):
        return self.liked

    def add_disliked(self, movie_id):
        self.disliked.add(movie_id)

    def return_disliked(self):
        return self.disliked
