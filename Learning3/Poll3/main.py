import datetime
from connection_pool import ConnectionPool
from poll import Poll
from options import Options
import random

login_file_path = "/Learning3/Poll2/login.json"


class MenuController():
    """A class for controlling the user menu and
    calling database class via Connection class
    """

    MENU_MESSAGE = """\nSelect one of the following options:\n
1) Create a new poll.\n2) List open polls.\n3) Vote on a poll.
4) Show poll votes.\n5) Exit.\nYour choice:
"""
    NEW_POLL_OPTION = "Enter new option text (or leave empty to stop adding options): "

    def __init__(self, login_file_path: str):
        ConnectionPool.init(min_connection=1, max_connection=10,
                            login_file_path=login_file_path)
        self.MENU_OPTIONS = {
            "1": self.create_polls,
            "2": self.show_open_polls,
            "3": self.vote_for_poll,
            "4": self.show_votes_for_poll,
        }

    @staticmethod
    def print_menu(title: str):

        def see_if_rounded(header):
            return round(number=header, ndigits=None) < header or \
                round(number=header, ndigits=None) > header

        header = 60
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
    def _print_poll_selection(_list: list):
        if _list:
            MenuController.print_menu(title="Poll selection:")
            _index = 0
            for index, option in enumerate(_list):
                print(f"{option.id}: {option.text}")
                _index = option.id
            print(f"{_index+1}: Vote randomly")
        else:
            MenuController.print_menu(title="No poll to vote for id")

    def create_polls(self):
        MenuController.print_menu(title="Create a poll:")
        title = input("Enter poll title: ")
        owner = input("Enter poll owner: ")
        poll = Poll(title=title, poll_maker=owner)
        poll.save()
        options = []
        while (option := input(MenuController.NEW_POLL_OPTION)):
            if option in options:
                break
            else:
                options.append(option)
        for option in options:
            poll.add_option(option_text=option)

    def show_open_polls(self):
        MenuController.print_menu(title="Open polls:")
        polls = Poll.get_all_polls()
        for poll in polls:
            print(f"{poll.id}: {poll.title} (created by {poll.poll_maker})")

    def vote_for_poll(self):
        MenuController.print_menu(title="Vote for a poll:")
        text = "Enter poll would like to vote on: "
        self.show_open_polls()
        try:
            poll_id = int(input(text))
            poll_options = Poll.get_poll(poll_id=poll_id).get_options
            option_id_saved = [option_id.id for option_id in poll_options]
            MenuController._print_poll_selection(poll_options)
            option_id = int(input("Enter option you would like to vote for: "))
        except ValueError as error:
            MenuController.print_menu(title=f"{error}")
            MenuController.print_menu(
                title="Enter a valid number as character")
        else:
            voter_name = input(
                "Enter the username you would like to vote as: ")
            if option_id not in option_id_saved:
                pick_random = random.choice(option_id_saved)
                Options.get_option(option_id=pick_random).vote(
                    voter_name=voter_name)
            else:
                Options.get_option(option_id=option_id).vote(
                    voter_name=voter_name)

    def _votes_per_option(self, options):
        for option in options:
            MenuController.print_menu(title=option.text)
            votes = option.get_votes
            if not votes:
                MenuController.print_menu(title="no votes")
            else:
                for vote in votes:
                    date = datetime.datetime.fromtimestamp(timestamp=vote[2],
                                                           tz=datetime.timezone.utc)
                    local_date = date.strftime("%Y-%m-%d %H:%M:%S")
                    MenuController.print_menu(
                        title=f"{vote[0]} on {local_date}")

    def show_votes_for_poll(self):
        self.show_open_polls()
        try:
            poll_id = int(
                input("\nEnter poll you would like to see votes for: "))
            poll = Poll.get_poll(poll_id=poll_id)
            poll_options = poll.get_options
            votes_per_option = [len(votes.get_votes) for votes in poll_options]
            total_votes = sum(votes_per_option)
            MenuController.print_menu(title="")
            for option, count in zip(poll_options, votes_per_option):
                percentage = count / total_votes * 100
                print(f"{option.text} got {count} votes ({
                      percentage:.2f}% of total votes)")

        except (ValueError, ZeroDivisionError) as _:
            print("No votes casted for this poll")
        finally:
            MenuController.print_menu(title="log")
            see_log = input(
                "Do you want to see the vote log? Type y to see log: ")
            if see_log == 'y':
                self._votes_per_option(options=poll_options)

    def program_flow(self):
        """ Controls the program flow for the user menu
        """
        while (option := input(MenuController.MENU_MESSAGE)) != "5":
            try:
                self.MENU_OPTIONS[option]()
            except KeyError:
                print("Please select between 1-5.")
        MenuController.print_menu(title="Goodbye")
        ConnectionPool.disconnect()


if __name__ == "__main__":
    menu = MenuController(login_file_path=login_file_path)
    connection = ConnectionPool.get_connection()
    ConnectionPool.get_information(connection=connection)
    ConnectionPool.release_connection(connection=connection)
    menu.program_flow()
