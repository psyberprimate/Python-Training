import database
import pytz
import datetime
from connection_pool import ConnectionPool


class Options():

    def __init__(self, option_text: str, poll_id: int, _id: int = None):
        self.id = _id
        self.text = option_text
        self.poll_id = poll_id

    def __repr__(self) -> str:
        return f"Option({self.text!r}, {self.poll_id!r}, {self.id!r})"

    def save(self):
        with ConnectionPool.auto_connect() as database_connection:
            new_option_id = database.add_option(database_connection=database_connection,
                                                option_text=self.text,
                                                poll_id=self.poll_id)
            self.id = new_option_id

    @classmethod
    def get_option(cls, option_id: int) -> "Options":
        with ConnectionPool.auto_connect() as database_connection:
            option = database.get_poll_option(database_connection, option_id)
            print("[x] inside options class method")
            return cls(option[1], option[2], option[0])

    def vote(self, voter_name: str):
        with ConnectionPool.auto_connect() as database_connection:
            utc_datetime = datetime.datetime.now(tz=pytz.utc)
            timestamp = utc_datetime.timestamp()
            database.add_poll_vote(database_connection=database_connection,
                                   voter_name=voter_name,
                                   option_id=self.id,
                                   vote_timestamp=timestamp)

    @property
    def get_votes(self):
        with ConnectionPool.auto_connect() as database_connection:
            votes = database.get_votes_for_option(database_connection=database_connection,
                                                  option_id=self.id)
            return votes
