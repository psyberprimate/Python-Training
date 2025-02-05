



class DataBase():
    """A class for containing the static methods for PostgresSQL database interactions.
    Functions take database connection instance as first argument from Connection() class
    """
    #class attributes
    CREATE_TABLE_1 = """CREATE TABLE IF NOT EXISTS polls (
        id SERIAL PRIMARY KEY,
        title TEXT,
        poll_author TEXT
        );"""
    CREATE_TABLE_2 = """CREATE TABLE IF NOT EXISTS options (
        id SERIAL PRIMARY KEY, option TEXT, poll_id INTEGER,
        FOREIGN KEY(poll_id) REFERENCES polls (id)
        );"""
    CREATE_TABLE_3 = """CREATE TABLE IF NOT EXISTS votes (
        voter_name TEXT,
        option_id INTEGER,
        FOREIGN KEY (option_id) REFERENCES options (id)
        );"""
    SELECT_EVERY_POLL = "SELECT * FROM polls;"
    SELECT_POLL = "SELECT * FROM polls WHERE polls.id = %s;"
    SELECT_POLL_WHERE = "SELECT * FROM options WHERE poll_id = %s;"
    CREATE_POLL_RETURN_ID = "INSERT INTO polls (title, poll_author) VALUES (%s, %s) RETURNING id;"
    GET_LATEST_POLL =   """SELECT * FROM polls
    WHERE polls.id = (
        SELECT id FROM polls ORDER BY id DESC LIMIT 1
        );
    """
    INSERT_OPTION_RETURN_ID = "INSERT INTO options (option, poll_id) VALUES (%s, %s) RETURNING id;"
    INSERT_VOTE = "INSERT INTO votes (voter_name, option_id) VALUES (%s, %s);"
    SELECT_OPTION = "SELECT * FROM options WHERE id = %s;"
    SELECT_VOTES_FOR_OPTION = "SELECT * FROM votes WHERE option_id = %s;"

    @staticmethod
    def create_tables(database_connection : object):
        cursor = database_connection.connection.cursor()
        cursor.execute(DataBase.CREATE_TABLE_1)
        cursor.execute(DataBase.CREATE_TABLE_2)
        cursor.execute(DataBase.CREATE_TABLE_3)
        database_connection.connection.commit()
        cursor.close()
    
    
    @staticmethod
    def create_poll(database_connection : object, title : str, owner : str):
        cursor = database_connection.connection.cursor()
        cursor.execute(DataBase.CREATE_POLL_RETURN_ID, (title, owner))
        database_connection.connection.commit()
        poll_id = cursor.fetchone()[0]
        return poll_id
    
    @staticmethod
    def get_polls(database_connection : object):
        cursor = database_connection.connection.cursor()
        cursor.execute(DataBase.SELECT_EVERY_POLL)
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query
    
    @staticmethod
    def get_poll(database_connection : object, poll_id : int):
        cursor = database_connection.connection.cursor()
        cursor.execute(DataBase.SELECT_POLL, (poll_id, ))
        returned_query = cursor.fetchone()
        cursor.close()
        return returned_query
    
    @staticmethod
    def get_latest_poll(database_connection : object) -> list:
        cursor = database_connection.connection.cursor()
        cursor = cursor.execute(DataBase.GET_LATEST_POLL)
        returned_query = cursor.fetchone()
        cursor.close()
        return returned_query
    
    @staticmethod
    def get_poll_options(database_connection : object, poll_id : int) -> list[tuple]:
        cursor = database_connection.connection.cursor()
        cursor.execute(DataBase.SELECT_POLL_WHERE, (poll_id, ))
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query
    
    @staticmethod
    def get_random_poll_vote(database_connection : object, id : int):
        cursor = database_connection.connection.cursor()
        cursor.execute(DataBase.SELECT_RANDOM_WINNER, (id, ))
        returned_query = cursor.fetchone()
        cursor.close()
        return returned_query
    
    @staticmethod
    def get_votes_for_option(database_connection : object, option_id : int):
        cursor = database_connection.connection.cursor()
        cursor.execute(DataBase.SELECT_VOTES_FOR_OPTION, (option_id, ))
        return cursor.fetchall()
    
    @staticmethod
    def add_poll_vote(database_connection : object, voter_name : str, option_id):
        cursor = database_connection.connection.cursor()
        cursor.execute(DataBase.INSERT_VOTE, (voter_name, option_id))
        database_connection.connection.commit()
        cursor.close()
        
    @staticmethod
    def add_option(database_connection : object, option_text : str, poll_id : int):
        cursor = database_connection.connection.cursor()
        cursor.execute(DataBase.INSERT_OPTION_RETURN_ID, (option_text, poll_id))
        option_id = cursor.fetchone()[0]
        database_connection.connection.commit()
        cursor.close()
        return option_id
    
    @staticmethod
    def get_poll_option(database_connection : object, poll_id : int):
        cursor = database_connection.connection.cursor()
        cursor.execute(DataBase.SELECT_OPTION, (poll_id, ))
        returned_query = cursor.fetchone()
        cursor.close()
        return returned_query