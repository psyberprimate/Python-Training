import datetime
import os

class WatchList():
    """A class for containing the functions for PostgresSQL database interactions
    """
    #class attributes
    CREATE_TABLE_1 = """CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
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
    SEARCH_FOR_MOVIE = "SELECT * FROM movies WHERE title LIKE %s;"
    INSERT_MOVIES = "INSERT INTO movies (title, release_date) VALUES (%s, %s);"
    DELETE_FROM_MOVIES_LIST = "DELETE FROM movies WHERE title = %s;"
    SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_date > %s;"
    SELECT_USER_WATCHED_MOVIES = """SELECT movies.* FROM movies
    JOIN watchlist ON movies.id = watchlist.movie_id
    JOIN users ON users.username = watchlist.watchlist_username
    WHERE users.username = %s ORDER BY movies.id;"""
    INSERT_WATCHED_MOVIE = "INSERT INTO watchlist (watchlist_username, movie_id) VALUES (%s, %s);"
    DELETE_FROM_USER_LIST = "DELETE FROM watchlist WHERE watchlist_username = %s AND movie_id = %s;"
    ADD_NEW_USER = "INSERT INTO users (username) VALUES (%s);"
    DELETE_USER = "DELETE FROM users WHERE username = %s;"
    SHOW_USERS = "SELECT * FROM users;"
    CREATE_INDEX = "CREATE INDEX IF NOT EXISTS idx_movies_released ON movies(release_date);"
    
    def __init__(self, connection_instance):
        self.connection = connection_instance.connection

    def create_tables(self):
        #    I do not know if with is always better to use than so for practice...
                
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         cursor.execute(WatchList.CREATE_TABLE_1)
        #         cursor.execute(WatchList.CREATE_TABLE_2)
        #         cursor.execute(WatchList.CREATE_TABLE_3)
        #         cursor.execute(WatchList.CREATE_INDEX)
        
        cursor = self.connection.cursor()
        cursor.execute(WatchList.CREATE_TABLE_1)
        cursor.execute(WatchList.CREATE_TABLE_2)
        cursor.execute(WatchList.CREATE_TABLE_3)
        self.connection.commit()
        cursor.close()
        
    def delete_from_user_list(self, user_name : str, title : str):
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         cursor.execute(WatchList.DELETE_FROM_USER_LIST, (user_name, title))
        cursor = self.connection.cursor()
        cursor.execute(WatchList.DELETE_FROM_USER_LIST, (user_name, title))
        self.connection.commit()
        cursor.close()

    def add_new_movie(self, movie : str, date : str):
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         cursor.execute(WatchList.INSERT_MOVIES, (movie, date))
        cursor = self.connection.cursor()
        cursor.execute(WatchList.INSERT_MOVIES, (movie, date))
        self.connection.commit()
        cursor.close()

    def view_upcoming_movies(self):
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         time_now = datetime.datetime.today().timestamp()
        #         cursor.execute(WatchList.SELECT_UPCOMING_MOVIES, (time_now, ))
        #         return cursor.fetchall()
        cursor = self.connection.cursor()
        time_now = datetime.datetime.today().timestamp()
        cursor.execute(WatchList.SELECT_UPCOMING_MOVIES, (time_now, ))
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query

    def view_all_movies(self, ):
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         cursor.execute(WatchList.SELECT_ALL_MOVIES)
        #         return cursor.fetchall()
        cursor = self.connection.cursor()
        cursor.execute(WatchList.SELECT_ALL_MOVIES)
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query

    def search_for_movie(self, search_keyword : str):
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         cursor.execute(WatchList.SEARCH_FOR_MOVIE, (f"%{search_keyword}%", ))
        #         return cursor.fetchall()
        cursor = self.connection.cursor()
        cursor.execute(WatchList.SEARCH_FOR_MOVIE, (f"%{search_keyword}%", ))
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query

    def add_watched_movie(self, viewer : str, movie_id : str):
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         cursor.execute(WatchList.INSERT_WATCHED_MOVIE, (viewer, movie_id))
        cursor = self.connection.cursor()
        cursor.execute(WatchList.INSERT_WATCHED_MOVIE, (viewer, movie_id))
        self.connection.commit()
        cursor.close()

    def view_watched_movies(self, viewer : str):
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         cursor.execute(WatchList.SELECT_USER_WATCHED_MOVIES, (viewer, ))
        #         return cursor.fetchall()
        cursor = self.connection.cursor()
        cursor.execute(WatchList.SELECT_USER_WATCHED_MOVIES, (viewer, ))
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query

    def show_users(self):
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         cursor.execute(WatchList.SHOW_USERS)
        #         return cursor.fetchall()
        cursor = self.connection.cursor()
        cursor.execute(WatchList.SHOW_USERS)
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query

    def add_user(self, new_user : str):
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         cursor.execute(WatchList.ADD_NEW_USER, (new_user, ))
        cursor = self.connection.cursor()
        cursor.execute(WatchList.ADD_NEW_USER, (new_user, ))
        self.connection.commit()
        cursor.close()
        

    def delete_user(self, delete_user : str):
        # with self.connection:
        #     with self.connection.cursor() as cursor:
        #         cursor.execute(WatchList.DELETE_USER, (delete_user, ))
        cursor = self.connection.cursor()
        cursor.execute(WatchList.DELETE_USER, (delete_user, ))
        self.connection.commit()
        cursor.close()
        
if __name__ == '__main__':
    WatchList.create_tables()