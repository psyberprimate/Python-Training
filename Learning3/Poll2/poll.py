from database import DataBase
from typing import List
from options import Options

class Poll():
    """A class for poll object with DataBase class database interactions
    """    
    
    def __init__(self, title : str, poll_maker : str, _id : int = None):
        self.id = _id
        self.title = title
        self.poll_maker = poll_maker
        
    def __repr__(self):
        return f"Poll({self.title!r}, {self.poll_maker!r}, {self.id!r})"
    
    def save(self, database_connection : object):
        new_poll_id = DataBase.create_poll(database_connection=database_connection,
                                           title=self.title, owner=self.poll_maker)
        self.id = new_poll_id
        
    def add_option(self, database_connection : object, option_text: str):
        Options(option_text, self.id).save(database_connection=database_connection)
    
    def get_options(self, database_connection : object) -> List[Options]:
        options = DataBase.get_poll_options(database_connection=database_connection,
                                            poll_id=self.id)
        return[Options(option[1], options[2], option[0]) for option in options]
    
    @classmethod
    def get_poll(cls, database_connection : object, poll_id : int):
        poll = DataBase.get_poll(database_connection=database_connection,
                                 poll_id=poll_id)
        return cls(poll[1], poll[2], poll[0])
    
    @classmethod
    def get_all_polls(cls, database_connection : object) -> List["Poll"]:
        polls = DataBase.get_polls(database_connection)
        return [cls(title=poll[1], poll_maker=poll[2], _id=poll[0]) for poll in polls]
    
    @classmethod
    def get_latest_poll(cls, database_connection : object) -> "Poll":
        poll = DataBase.get_latest_poll(database_connection=database_connection)
        return cls(title=poll[1], poll_maker=poll[2], _id=poll[0])