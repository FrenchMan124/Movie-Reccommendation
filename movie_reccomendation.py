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

def set_current_user(user_id):
    """ Assign the current user to an instance """
    # Set the current user to do recommendations for
    CURRENT_USER = ""   # Var to store instance of current user
    for user in users:
        if user.id == user_id:  # Change for current user
            CURRENT_USER = user
    return CURRENT_USER

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

def import_ratings(LIKED_RATING):
    """ Load ratings csv files to ratings and user classes """
    id_list = []
    import csv
    with open('ratings.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        new_user_id = "_"

        # Count the rows and discount the header
        for row in csv_reader:
            if line_count == 0: # Header row
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            else:
                line_count += 1

                """*** Add the imported data to the Rating class ***"""
                # Add the imported data to the Rating class
                Ratings(row[0], row[1], row[2])

                """*** Add the imported data to the User class ***"""
                if row[0] in id_list:
                    # Add liked and disliked movies to the user instance
                    if row[2] >= LIKED_RATING:   # If the rating is above the liked rating add it to the user's liked movies set
                        users[int(row[0])-1].add_liked(row[1])
                    else:   # Otherwise add it to the disliked movies set
                        users[int(row[0])-1].add_disliked(row[1])
                
                # If the user ID changes, create new user
                else:
                    User(row[0])
                    id_list.append(row[0])
                                
        print('Ratings, Processed {} lines.'.format(line_count))


def similarity_index(CURRENT_USER, user):
    """
    Return the similarity index of two users Between —1.0 and 1.0.
    Originally known as "coefficient de communaute" By Paul Jaccard
    """
    # This looks very complicated but it is simple, just build it step by step.
    # You will be using the return methods built in the user class

    # Here U1 and U2 are two users and we are comparing L1 and L2, the sets of movies they have both liked.
    # Divide the number of common elements in either set by the number of all the elements in both sets
    # S(U1, U2) = (L1 intersection L2) / (L1 union L2)
    U1 = CURRENT_USER
    U2 = user

    L1 = U1.return_liked
    D1 = U1.return_disliked
 
    L2 = U2.return_liked
    D2 = U2.return_disliked
    
    # If U1 and U2 like similar movies they should disliked similar movies, add the number of common dislikes
    # S(U1, U2) = ((L1 intersection L2) + (D1 intersection D2)) / (L1 union L2 union D1 union D2)
    similarity_index = 
    
    
    # Considering the case where two users are polar opposities in their preference
    # Subtract the number of conflicting likes and dislikes of the two users from the number of their common
    # likes and dislikes
    # S(U1, U2) = ((L1 intersection L2) + (D1 intersection D2)
    #               -(L1 intersection D2) — (L2 intersection D1) )
    #               / (L1 union L2 union D1 union D2)

    # This will return a value in the range of -1.0 and 1.0
    # Two users having identical tastes will have a similarity index of 1.0
    # Two users with conflicting tastes in movies will have a similarity index of -1.0
    # Return this value


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
    













        
