

class Poll():
    """A class for containing the functions for PostgresSQL database interactions.
    Where __init__ need to have class passed to it with self.connection with database
    connection.
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
    SELECT_POLL_WHERE = """SELECT * FROM polls
    JOIN options ON polls.id = options.poll_id
    WHERE polls.id = %s;
    """
    GET_POLL_RESULTS = """
    SELECT
        options.id,
        options.option,
        COUNT(votes.option_id) AS vote_count,
        COUNT(votes.option_id) / SUM(COUNT(votes.option_id)) OVER() * 100.0 AS vote_percentage
    FROM options
    LEFT JOIN votes ON options.id = votes.option_id
    WHERE options.poll_id = %s
    GROUP BY options.id;
    """
    CREATE_POLL_RETURN_ID = "INSERT INTO polls (title, poll_author) VALUES (%s, %s) RETURNING id;"
    GET_LATEST_POLL =   """SELECT * FROM polls
    JOIN option ON polls.id = options.poll_id
    WHERE polls.id = (SELECT id FROM polls ORDER BY id DESC LIMIT 1);
    """
    SELECT_RANDOM_WINNER = """SELECT * FROM public.polls
    JOIN public.options ON polls.id = options.poll_id
    JOIN public.votes ON options.id = votes.option_id
    WHERE public.polls.id = %s
    ORDER BY RANDOM() LIMIT 1"""
    INSERT_OPTION = "INSERT INTO options (option, poll_id) VALUES (%s, %s);"
    INSERT_VOTE = "INSERT INTO votes (voter_name, option_id) VALUES (%s, %s)"

    
    def __init__(self, connection_instance):
        #database connection
        self.connection = connection_instance.connection

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute(Poll.CREATE_TABLE_1)
        cursor.execute(Poll.CREATE_TABLE_2)
        cursor.execute(Poll.CREATE_TABLE_3)
        self.connection.commit()
        cursor.close()
        
    def get_polls(self):
        cursor = self.connection.cursor()
        cursor.execute(Poll.SELECT_EVERY_POLL)
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query
    
    def get_latest_poll(self):
        cursor = self.connection.cursor()
        cursor = cursor.execute(Poll.GET_LATEST_POLL)
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query
    
    def get_poll_details(self, poll_id : int):
        cursor = self.connection.cursor()
        cursor.execute(Poll.SELECT_POLL_WHERE, (poll_id, ))
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query
    
    def get_poll_and_vote_results(self, poll_id : int):
        cursor = self.connection.cursor()
        cursor.execute(Poll.GET_POLL_RESULTS, (poll_id, ))
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query
    
    def get_random_poll_vote(self, id : int):
        cursor = self.connection.cursor()
        cursor.execute(Poll.SELECT_RANDOM_WINNER, (id, ))
        returned_query = cursor.fetchall()
        cursor.close()
        return returned_query
    
    def create_poll(self, title : str, owner : str, options : list):
        cursor = self.connection.cursor()
        cursor.execute(Poll.CREATE_POLL_RETURN_ID, (title, owner))
        self.connection.commit()
        poll_id = cursor.fetchone()[0]
        option_values = [(option, poll_id) for option in options]
        for values in option_values:
            cursor.execute(Poll.INSERT_OPTION, values)
        self.connection.commit()
        cursor.close()
    
    def add_poll_vote(self, voter_name : str, option_id):
        cursor = self.connection.cursor()
        cursor.execute(Poll.INSERT_VOTE, (voter_name, option_id))
        self.connection.commit()
        cursor.close()