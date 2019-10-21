##
# movie_reccomendation.py
# Created: 29.08.19
# Last edit: 06.09.19
# A program that reccommends movies based on an algorithm and other 'users'

from tkinter import *
import tkinter as tk
movie_title = []
user_rating = []
new_user = []


class GUI:
    """ dont know """
    def __init__(self, parent):
        self.new_user = int(ratings[-1].user_id) + 1
        User(self.new_user)
        self.CURRENT_USER = set_current_user(self.new_user)
        self.parent = parent
        # Control buttons
        self.button_search = Button(root, text="Search for a movie", command=self.movie_search).grid(row=0, column=0)
        

    def movie_search(self):
        """ Search the name of a student and print all the students info """
        self.movie_entrybox = Entry(root)
        self.movie_entrybox.grid(row=1, column=0)

        self.search_submit_button = Button(root, text="Submit", command=self.submit_search)
        self.search_submit_button.grid(row=2, column=0)

    def submit_search(self):
        """ """
        self.results = Listbox(root)
        self.results.grid(row=3, column=0)
        for movie in movies:
            if self.movie_entrybox.get().lower() in movie.title.lower():
                self.results.insert(END, movie.title)
                





    def getting_reccomenendeations(self):
        
        self.movie_listbox = Listbox(root)
        self.movie_listbox.grid(row=3, column=1)
        self.movie_listbox.insert(END, "The Toker")

class Movies:
    """ Movie class, genres is stored as a list """
    def __init__(self, id, year, title, genres):
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
    with open('lessMovies.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0: # Header row
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

def import_ratings(LIKED_RATING):
    """ Load ratings csv files to ratings and user classes """
    id_list = []
    import csv
    with open('lessRatings.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        # Count the rows and discount the header
        for row in csv_reader:
            if line_count == 0: # Header row
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
                    if row[2] >= LIKED_RATING:
                        users[int(row[0])-1].add_liked(row[1])
                    else:
                        users[int(row[0])-1].add_disliked(row[1])


def similarity_index(CURRENT_USER, user):
    """
    Return the similarity index of two users Between —1.0 and 1.0.
    Originally known as "coefficient de communaute" By Paul Jaccard
    """
    U1 = CURRENT_USER
    U2 = user

    L1 = U1.return_liked()
    D1 = U1.return_disliked()
 
    L2 = U2.return_liked()
    D2 = U2.return_disliked()
    
    similarity = (len(L1&L2) + len(D1&D2) - len(L1&D2) - len(L2&D1)) / len(L1|L2|D1|D2)

    return similarity

def user_movies(user):
    """ Return the liked and disliked movie SETS for the given user """
    # Return movies rated by a given user
    movies_rated = (user.return_liked())|(user.return_disliked())
    return movies_rated
    
def return_user_liked(movie):
    """ Return the set of all users who liked a movie """
    # Create an empty set
    users_liked = set()
    # For each user
    for user in users:
        # If the movie is in the users set of liked movies
        if movie in user.return_liked():
            # Add the user to the set
            users_liked.add(user)
    # Return the set
    return users_liked

def return_user_disliked(movie):
    """ Return the set of all users who liked a movie """
    users_disliked = set()
    for user in users:
        if movie in user.return_disliked():
            users_disliked.add(user)
    
    return users_disliked

def find_similar_users(CURRENT_USER):
    """
    Given a user, compute a list of other users who are similar
    Store the list in a database (in this case a dictionary), along with their similarity indicies
    Return the list of similar user in order of most to least similar
    """
    similar_users_set = set()
    similar_user_instances = []
    similar_users_ratio = {}

    rated_movies = user_movies(CURRENT_USER)
    for movie in rated_movies:
        similar_users_set.update(return_user_liked(movie)|return_user_disliked(movie))
    
    for similar_user in similar_users_set:
        if similar_user.id != CURRENT_USER.id:
            similarity = similarity_index(CURRENT_USER, similar_user)
            similar_users_ratio[similar_user] = similarity
        
    # Order users in terms of most similar
    for user, similarity in sorted(similar_users_ratio.items(), key=lambda x:x[1], reverse=True):
        similar_user_instances.append(user)

    return similar_user_instances


def possibility_index(CURRENT_USER, movie):
    """
    Given a user and a movie (obviously the user should not have rated this movie yet)
    Find all users who have rated the movie
    Compute the similarity index of each user and use if to
    Generate the possibility of a user liking a given movie
    """

    ## Finding the sum of the similarity indicies of all users who have LIKED a movie
    liked_sum = 0  # Variable to store the sum of all the similarity indicies of all users who have liked a given movie
    for user in return_user_liked(movie):
        if user != CURRENT_USER:
            liked_sum += similarity_index(CURRENT_USER, user)

    ## Finding the sum of the similarity indicies of all users who have DISLIKED a movie
    disliked_sum = 0
    for user in return_user_disliked(movie):
        if user != CURRENT_USER:
            disliked_sum += similarity_index(CURRENT_USER, user)

    try:
        possibility_index = (liked_sum - disliked_sum) / (len(return_user_liked(movie)) + len(return_user_disliked(movie)))
    except ZeroDivisionError:
        possibility_index = 0
    return possibility_index

def return_unrated(CURRENT_USER):
    """ Return a list of all unrated movie ids a given user has not rated """
    # Create a list to store all movie ids of unrated movies
    unrated_movie_ids = []
    for user in find_similar_users(CURRENT_USER):
        unrated_movies = user_movies(user).difference(user_movies(CURRENT_USER))
        for movie in unrated_movies:
            if movie not in unrated_movie_ids:
                unrated_movie_ids.append(movie)

    return unrated_movie_ids        
        
def unrated_movie_possibilities(CURRENT_USER):
    """ Store all items the given user has not rated with the possibility index and return the dictionary """
    # Create an empty dictionary to store all reccommended movies with their id and their possibility index
    recommended_movies = {}
    unrated_movie_ids = return_unrated(CURRENT_USER)
    for unrated_movie in unrated_movie_ids:
        recommended_movies[unrated_movie] = possibility_index(CURRENT_USER, unrated_movie)

    # Return the dictionary of reccommended movies
    return recommended_movies

def generate_recommendations(CURRENT_USER, num_recommendations):
    """ Generating movie recommendations """
    recommended_movies = unrated_movie_possibilities(CURRENT_USER)  # Rate all recommended

    counter = 0
    # Recommend the top five recommended movies using a dictionary sorted on values
    highest_possibility = -1
    for movie in movies:
        if possibility_index(CURRENT_USER, movie.id) > highest_possibility:
            highest_possibility = possibility_index(CURRENT_USER, movie.id)
    
    print("******\nMovies\n******")
    for i, j in sorted(recommended_movies.items(), key=lambda x:x[1], reverse=True):
        if counter < num_recommendations:
            for movie in movies:
                if movie.id == i:
                    print(movie.title, movie.year, "\n{}%".format(round(possibility_index(CURRENT_USER, movie.id) / highest_possibility * 100, 1)), "\n")
                    counter += 1
    
if __name__ == "__main__":
    LIKED_RATING = "4"  # Movies rated this score and above are considered liked
    movies = []     # Stores all instances of movies
    ratings = []    # Stores all instances of ratings
    users = []      # Stores all instances of users

    # Import csv as objects
    import_movies()
    import_ratings(LIKED_RATING)

    # Store current user instance
    current_user_id = '2'
    CURRENT_USER = set_current_user(current_user_id)

    # Generate recommended movies
    generate_recommendations(CURRENT_USER, 6)


#GUI
root = tk.Tk()
root.title("Movie Ratings")
root.geometry("800x400+500+200")
gui_1 = GUI(root)
root.mainloop()











