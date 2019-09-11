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

def import_movies():
    """ Load movie csv files movies class """
    import csv
    with open('movies.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0: # Header row
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            else:
                line_count += 1

                """*** Add the imported data to the Movie class ***"""
                # Seperating the year and title
                year = (row[1])[-5:-1]
                title = (row[1])[0:-6]
                id = (row[0])
                
                # ***Do some string processing to import into the Movie class ***
                Movies(row[0], year, title, row[2])
                
        print('Movies, Processed {} lines.'.format(line_count))





if __name__ == "__main__":
    LIKED_RATING = "4"  # Movies rated this score and above are considered liked
    movies = []     # Stores all instances of movies
    ratings = []    # Stores all instances of ratings
    users = []      # Stores all instances of users

    # Import csv as objects
    import_movies()
    import_ratings(LIKED_RATING)

    similarity_index(CURRENT_USER, users[5])
    # Checking
    print("\nLiked:\n", users[0].return_liked())
    print("\nDisliked:\n", users[0].return_disliked())

    # Set the current user and number of recommendations
    current_user_id = '1'
    num_of_recommendations = 5

    # Store current user instance
    CURRENT_USER = set_current_user(current_user_id)
    
