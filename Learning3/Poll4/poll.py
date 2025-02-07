import database
from typing import List
from options import Options
from connection_pool import ConnectionPool


class Poll():
    """A class for poll object with DataBase class database interactions
    """

    def __init__(self, title: str, poll_maker: str, _id: int = None):
        self.id = _id
        self.title = title
        self.poll_maker = poll_maker

    def __repr__(self):
        return f"Poll({self.title!r}, {self.poll_maker!r}, {self.id!r})"

    def save(self):
        with ConnectionPool.auto_connect() as database_connection:
            new_poll_id = database.create_poll(database_connection=database_connection,
                                               title=self.title, owner=self.poll_maker)
            self.id = new_poll_id

    def add_option(self, option_text: str):
        with ConnectionPool.auto_connect() as database_connection:
            Options(option_text, self.id).save(
                database_connection=database_connection)

    @property
    def get_options(self) -> List[Options]:
        with ConnectionPool.auto_connect() as database_connection:
            options = database.get_poll_options(database_connection=database_connection,
                                                poll_id=self.id)
            return [Options(option[1], option[2], option[0]) for option in options]

    @classmethod
    def get_poll(cls, poll_id: int):
        with ConnectionPool.auto_connect() as database_connection:
            poll = database.get_poll(database_connection=database_connection,
                                     poll_id=poll_id)
            return cls(poll[1], poll[2], poll[0])

    @classmethod
    def get_all_polls(cls) -> List["Poll"]:
        with ConnectionPool.auto_connect() as database_connection:
            polls = database.get_all_polls(database_connection)
            return [cls(title=poll[1], poll_maker=poll[2], _id=poll[0]) for poll in polls]

    @classmethod
    def get_latest_poll(cls, database_connection: object) -> "Poll":
        with ConnectionPool.auto_connect() as database_connection:
            poll = database.get_latest_poll(
                database_connection=database_connection)
            return cls(title=poll[1], poll_maker=poll[2], _id=poll[0])
