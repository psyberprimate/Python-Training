from contextlib import contextmanager
import psycopg2

# class attributes
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
        vote_timestamp INTEGER,
        FOREIGN KEY (option_id) REFERENCES options (id)
        );"""
SELECT_EVERY_POLL = "SELECT * FROM polls;"
SELECT_POLL = "SELECT * FROM polls WHERE polls.id = %s;"
SELECT_POLL_WHERE = "SELECT * FROM options WHERE poll_id = %s;"
CREATE_POLL_RETURN_ID = "INSERT INTO polls (title, poll_author) VALUES (%s, %s) RETURNING id;"
GET_LATEST_POLL = """SELECT * FROM polls
    WHERE polls.id = (
        SELECT id FROM polls ORDER BY id DESC LIMIT 1
        );
    """
INSERT_OPTION_RETURN_ID = "INSERT INTO options (option, poll_id) VALUES (%s, %s) RETURNING id;"
INSERT_VOTE = "INSERT INTO votes (voter_name, option_id, vote_timestamp) VALUES (%s, %s, %s);"
SELECT_OPTION = "SELECT * FROM options WHERE id = %s;"
SELECT_VOTES_FOR_OPTION = "SELECT * FROM votes WHERE option_id = %s;"
SELECT_POLLS = "SELECT * FROM polls;"
SELECT_OPTIONS_IN_POLL = """
SELECT options.text, SUM(votes.option_id) FROM options
JOIN polls ON options.poll_id = polls.id
JOIN votes ON options.id = votes.option_id
WHERE polls.id = %s
GROUP BY options.text"""


@contextmanager
def get_cursor(database_connection):
    with database_connection:
        with database_connection.cursor() as cursor:
            yield cursor


def create_tables(database_connection):
    with get_cursor(database_connection) as cursor:
        cursor.execute(CREATE_TABLE_1)
        cursor.execute(CREATE_TABLE_2)
        cursor.execute(CREATE_TABLE_3)


def create_poll(database_connection, title: str, owner: str):
    with get_cursor(database_connection) as cursor:
        cursor.execute(CREATE_POLL_RETURN_ID, (title, owner))
        poll_id = cursor.fetchone()[0]
        return poll_id


def get_all_polls(database_connection):
    with get_cursor(database_connection) as cursor:
        cursor.execute(SELECT_EVERY_POLL)
        return cursor.fetchall()


def get_poll(database_connection, poll_id: int):
    with get_cursor(database_connection) as cursor:
        cursor.execute(SELECT_POLL, (poll_id, ))
        return cursor.fetchone()


def get_latest_poll(database_connection) -> list:
    with get_cursor(database_connection) as cursor:
        cursor = cursor.execute(GET_LATEST_POLL)
        return cursor.fetchone()


def get_poll_options(database_connection, poll_id: int) -> list[tuple]:
    with get_cursor(database_connection) as cursor:
        cursor.execute(SELECT_POLL_WHERE, (poll_id, ))
        return cursor.fetchall()


def get_votes_for_option(database_connection, option_id: int):
    with get_cursor(database_connection) as cursor:
        cursor.execute(SELECT_VOTES_FOR_OPTION, (option_id, ))
        return cursor.fetchall()


def add_poll_vote(database_connection, voter_name: str,
                  option_id: int, vote_timestamp: int):
    with get_cursor(database_connection) as cursor:
        cursor.execute(INSERT_VOTE, (voter_name, option_id, vote_timestamp))


def add_option(database_connection, option_text: str, poll_id: int):
    with get_cursor(database_connection) as cursor:
        cursor.execute(INSERT_OPTION_RETURN_ID,
                       (option_text, poll_id))
        return cursor.fetchone()[0]


def get_poll_option(database_connection, poll_id: int):
    with get_cursor(database_connection) as cursor:
        cursor.execute(SELECT_OPTION, (poll_id, ))
        return cursor.fetchone()
