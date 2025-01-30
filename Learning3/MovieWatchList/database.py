import sqlite3
import datetime
import os

CREATE_TABLE_1 = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_date REAL
    );"""
CREATE_TABLE_2 = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
    );"""
CREATE_TABLE_3 = """CREATE TABLE IF NOT EXISTS watchlist (
    watchlist_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY (watchlist_username) REFERENCES users(username),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
    );"""

SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SEARCH_FOR_MOVIE = "SELECT * FROM movies WHERE title LIKE ?;"
INSERT_MOVIES = "INSERT INTO movies (title, release_date) VALUES (?, ?);"
DELETE_FROM_MOVIES_LIST = "DELETE FROM movies WHERE title = ?;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_date > ?;"
SELECT_USER_WATCHED_MOVIES = """SELECT movies.* FROM movies
JOIN watchlist ON movies.id = watchlist.movie_id
JOIN users ON users.username = watchlist.watchlist_username
WHERE users.username = ? ORDER BY movies.id;"""
INSERT_WATCHED_MOVIE = "INSERT INTO watchlist (watchlist_username, movie_id) VALUES (?, ?);"
DELETE_FROM_USER_LIST = "DELETE FROM watchlist WHERE watchlist_username = ? AND movie_id = ?;"
ADD_NEW_USER = "INSERT INTO users (username) VALUES (?);"
DELETE_USER = "DELETE FROM users WHERE username = ?;"
SHOW_USERS = "SELECT * FROM users;"
CREATE_INDEX = "CREATE INDEX IF NOT EXISTS idx_movies_released ON movies(release_date);"

connection = sqlite3.connect(
    os.path.join(os.getcwd()+os.path.normcase("/Learning3/MovieWatchList/watchlist.db")))

def create_tables():
    with connection:
        connection.execute(CREATE_TABLE_1)
        connection.execute(CREATE_TABLE_2)
        connection.execute(CREATE_TABLE_3)
        connection.execute(CREATE_INDEX)
    
def close_connection():
    connection.close()
    
def delete_from_user_list(user_name : str, title : str):
    with connection:
        connection.execute(DELETE_FROM_USER_LIST, (user_name, title))

def add_new_movie(movie : str, date : str):
    with connection:
        connection.execute(INSERT_MOVIES, (movie, date))

def view_upcoming_movies():
    with connection:
        time_now = datetime.datetime.today().timestamp()
        cursor = connection.execute(SELECT_UPCOMING_MOVIES, (time_now, ))
        return cursor.fetchall()

def view_all_movies():
    with connection:
        cursor = connection.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def search_for_movie(search_keyword : str):
    with connection:
        cursor = connection.execute(SEARCH_FOR_MOVIE, (f"%{search_keyword}%", ))
        return cursor.fetchall()

def add_watched_movie(viewer : str, movie_id : str):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (viewer, movie_id))

def view_watched_movies(viewer : str):
    with connection:
        cursor = connection.execute(SELECT_USER_WATCHED_MOVIES, (viewer, ))
        return cursor.fetchall()

def show_users():
    with connection:
        cursor = connection.execute(SHOW_USERS)
        return cursor.fetchall()

def add_user(new_user : str):
    with connection:
        connection.execute(ADD_NEW_USER, (new_user, ))

def delete_user(delete_user : str):
    with connection:
        connection.execute(DELETE_USER, (delete_user, ))
        
if __name__ == '__main__':
    create_tables()