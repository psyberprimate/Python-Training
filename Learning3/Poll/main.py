import datetime
from connection import Connection
from poll import Poll
from psycopg2.errors import DivisionByZero

login_file_path = "/Learning3/MovieWatchList2/login.json"

class MenuController():
    """A class for controlling the user menu and
    calling Poll class via Connection class
    """    
    
    MENU_MESSAGE = """\nSelect one of the following options:\n
1) Create a new poll.\n2) List open polls.\n3) Vote on a poll.
4) Show poll votes. \n5) Select a random winner from a poll option.
6) Exit.\nYour choice: """
    NEW_POLL_OPTION = "Enter new option text (or leave empty to stop adding options): "
    
    def __init__(self, login_file_path : str):
        self.connection = Connection(login_file_path=login_file_path)
        self.poll = Poll(connection_instance=self.connection)
        self.MENU_OPTIONS = {
            "1" : self.create_polls,
            "2" : self.show_open_polls,
            "3" : self.vote_for_poll,
            "4" : self.show_votes_for_poll,
            "5" : self.randomize_poll_winner
        }

    @staticmethod
    def print_menu(title : str):
        
        def see_if_rounded(header):
            return round(number=header, ndigits=None) < header or \
                round(number=header, ndigits=None) > header 
        
        header = 40
        header -= len(title)
        odd = see_if_rounded(header/2)
        header = header // 2
        base_str = ""
        if len(title) > 0:
            for _ in range(1, header):
                base_str += "*"
            title = " ".join([base_str, title])
            title = " ".join([title, base_str])
            title += '*' if odd else ''
            
        else:
            title = ''.join(f'*'*header*2)
        print(title)

    @staticmethod
    def _print_poll_selection(_list : list):
        if _list:
            MenuController.print_menu(title="Poll selection: ")
            for option in _list:
                print(f"{option[3]}: {option[4]}")
        else:
            MenuController.print_menu(title="No poll to vote for id")
            
    def create_polls(self):
        MenuController.print_menu(title="Create a poll: ")
        title = input("Enter poll title: ")
        owner = input("Enter poll owner: ")
        options = []
        while (option := input(MenuController.NEW_POLL_OPTION)):
            if option in options:
                break
            else:
                options.append(option)
        self.poll.create_poll(title=title, owner=owner, options=options)
    
    def show_open_polls(self):
        MenuController.print_menu(title="Open polls: ")
        polls = self.poll.get_polls()
        for _id, title, owner in polls:
            print(f"{_id}: {title} (created by {owner})")
    
    def vote_for_poll(self):
        MenuController.print_menu(title="Vote for a poll: ")
        text = "Enter poll would like to vote on: "
        self.show_open_polls()
        try:
            poll_id = int(input(text))
            options_poll = self.poll.get_poll_details(poll_id=poll_id)
            MenuController._print_poll_selection(options_poll)
            option_id = int(input("Enter option you would like to vote for: "))
        except ValueError as error:
            MenuController.print_menu(title=f"{error}")
            MenuController.print_menu(title="Enter a valid number as character")
        else:
            voter_name = input("Enter the username you would like to vote as: ")
            self.poll.add_poll_vote(voter_name=voter_name, option_id=option_id)
    
    def show_votes_for_poll(self):
        self.show_open_polls()
        try:
            poll_id = int(input("Enter poll you would like to see votes for: "))
            poll_votes = self.poll.get_poll_and_vote_results(poll_id=poll_id)
        except (ValueError, DivisionByZero) as error:
            print(f"{error}")
            print("No votes casted for this poll")
        else:
            for _, option, count, percentage in poll_votes:
                print(f"{option} got {count} votes ({percentage:.2f}% of total votes)")
            
    def randomize_poll_winner(self):
        try:
            self.show_open_polls()
            poll_id = int(input("Select a poll to choose a random winner for the poll: "))
        except ValueError as error:
            print(f"{error}")
        else:
            winner = self.poll.get_random_poll_vote(id=poll_id)
            winner = winner[0]
            MenuController.print_menu(title="Poll winner")
            print(f"The randomly selected winner is for the poll: "+
                  f"{winner[1]} by {winner[2]},\nis {winner[6]} with a vote for: {winner[4]}.")
            
    def program_flow(self):
        """ Controls the program flow for the user menu
        """
        while(option := input(MenuController.MENU_MESSAGE)) != "6":
            try:
                self.MENU_OPTIONS[option]()
            except KeyError:
                print("Please select between 1-6.")
        MenuController.print_menu(title="Goodbye")
        self.connection.disconnect()

if __name__ == "__main__":
    menu = MenuController(login_file_path=login_file_path)
    menu.connection.get_information()
    menu.program_flow()