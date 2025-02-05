from database import DataBase



class Options():
    
    def __init__(self, option_text : str, poll_id : int, _id : int = None):
        self.id = _id
        self.text = option_text
        self.poll_id = poll_id
        
    def __repr__(self) -> str:
        return f"Option({self.text!r}, {self.poll_id!r}, {self.id!r})"
    
    def save(self, database_connection : object):
        new_option_id = DataBase.add_option(database_connection,
                                            self.text,
                                            self.poll_id)
        self.id = new_option_id
    
    @classmethod
    def get_option(cls, database_connection : object, option_id : int) -> "Options":
        option = DataBase.get_poll_option(database_connection, option_id)
        return cls(option[1], option[2], option[0])
    
    def vote(self, database_connection : object, voter_name : str):
        DataBase.add_poll_vote(database_connection=database_connection,
                                      voter_name=voter_name,
                                      option_id=self.id)
        
    def get_votes(self, database_connection : object):
        votes = DataBase.get_votes_for_option(database_connection=database_connection,
                                              option_id=self.id)
        return votes
    
    @property
    def get_random_winner(self):
        return 
        