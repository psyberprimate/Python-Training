import datetime
from connection import Connection
from watchlist import WatchList

login_file_path = "/Learning3/MovieWatchList2/login.json"


class MenuController():
    """A class for controlling the user menu and
    calling WatchList class via Connection class
    """    
    def __init__(self, login_file_path : str):
        self.connection = Connection(login_file_path=login_file_path)
        self.watchlist = WatchList(connection_instance=self.connection)

    @staticmethod
    def print_menu(title : str):
        
        def see_if_rounded(header):
            return round(number=header, ndigits=None) < header or round(number=header, ndigits=None) > header 
        
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
    def get_time(time : str):
        date = datetime.datetime.fromtimestamp(time)
        return date.strftime("%d-%m-%Y")

    @staticmethod
    def parse_time(time : str):
        parsed_date = datetime.datetime.strptime(time, "%d-%m-%Y")
        return parsed_date.timestamp()

    @staticmethod
    def print_movie_list(list : list):
        if list:
            for movie_id, title, release_date in list:
                print(f"{movie_id}: {title} ({MenuController.get_time(release_date)})")
        else:
            MenuController.print_menu(title="User has not watched any movies")

    def new_movie(self):
        MenuController.print_menu(title="Adding new movie")
        MenuController.print_menu(title="")
        movie = input("Movie name: ")
        date = input("Enter the date (dd-mm-yyyy): ")
        self.watchlist.add_new_movie(movie=movie, date=MenuController.parse_time(date))

    def show_upcoming_movies(self):
        MenuController.print_menu(title="Upcoming Movies")
        MenuController.print_menu(title="")
        movies = self.watchlist.view_upcoming_movies()
        MenuController.print_movie_list(movies)

    def show_all_movies(self):
        MenuController.print_menu(title="All Movies")
        MenuController.print_menu(title="")
        movies = self.watchlist.view_all_movies()
        MenuController.print_movie_list(movies)
        
    def search_for_movie(self):
        MenuController.print_menu(title="Search for a movie")
        MenuController.print_menu(title="")
        search_keyword = input("Search for a with a keyword: ")
        movies = self.watchlist.search_for_movie(search_keyword=search_keyword)
        MenuController.print_menu(title="Found")
        MenuController.print_movie_list(movies)

    def add_watched_movie(self):
        viewer = input("Give the user's name: ")
        movie_id = input("Give movie id you watched: ")
        self.watchlist.add_watched_movie(viewer=viewer, movie_id=movie_id)
        
    def show_watched_movies(self, viewer : str = None, ask_input : bool = True):
        MenuController.print_menu(title="Watched Movies")
        MenuController.print_menu(title="")
        if ask_input:
            viewer = input("Give user name: ")
            user_movies = self.watchlist.view_watched_movies(viewer=viewer)
        else:
            user_movies = self.watchlist.view_watched_movies(viewer=viewer)
        MenuController.print_movie_list(user_movies)

    def show_users(self):
        MenuController.print_menu(title="Users")
        MenuController.print_menu(title="")
        users = self.watchlist.show_users()
        if users:
            for user in users:
                print(f"User: {user[0]}")
        else:
            print(f"No users currently")
        
    def add_user(self):
        new_user = input("Username: ")
        self.watchlist.add_user(new_user=new_user)
        print(f"User added: {new_user}")
        
    def delete_user(self):
        MenuController.show_users()
        delete_user = input("Username to be deleted: ")
        self.watchlist.delete_user(delete_user=delete_user)
        print(f"User with username: {delete_user} was deleted!")
        
    def delete_from_user_list(self):
        MenuController.print_menu(title="DELETE")
        MenuController.print_menu(title="")
        user_name = input("User name: ")
        self.show_watched_movies(viewer=user_name, ask_input=False)
        title = input("Movie id: ")
        self.watchlist.delete_from_user_list(user_name=user_name, title = title)
    
    def user_settings(self):
        MenuController.print_menu(title="User settings menu")
        while(True):
            MenuController.print_menu(title="")
            print("Select one of the following options: ")
            print("\n1) Show users.\n2) Add a user.\n3) Delete a user. \
                    \n4) Delete from user watchlist. \n5) Exit user settings.")
            try:
                user_input = int(input("\nYour selection: "))
            except:
                print("Error! Not a number!")
                continue
            match user_input:
                case 1:
                    self.show_users()
                case 2:
                    self.add_user()
                case 3:
                    self.delete_user()
                case 4:
                    self.delete_from_user_list()
                case 5:
                    break
                case _:
                    print("Select between choices 1-5")
    
    def program_flow(self):
        """ Controls the program flow for the user menu
        """
        while(True):
            MenuController.print_menu(title="Watchlist")
            MenuController.print_menu(title="")
            print("Select one of the following options: ")
            print("\n1) Add new movie.\n2) View upcoming movies.\n3) View all movies. \
                \n4) Search for a movie. \n5) Add watched movie. \n6) View watched movies.  \
                \n7) Show user settings. \n8) Exit.")
            try:
                user_input = int(input("\nYour selection: "))
            except:
                MenuController.print_menu(title="Error! Not a number!")
                continue
            match user_input:
                case 1:
                    self.new_movie()
                case 2:
                    self.show_upcoming_movies()
                case 3:
                    self.show_all_movies()
                case 4:
                    self.search_for_movie()
                case 5:
                    self.add_watched_movie()
                case 6:
                    self.show_watched_movies()
                case 7:
                    self.user_settings()
                case 8:
                    MenuController.print_menu(title="Goodbye")
                    self.connection.disconnect()
                    break
                case _:
                    MenuController.print_menu(title="Select between choices 1-8")


if __name__ == "__main__":
    menu = MenuController(login_file_path=login_file_path)
    menu.connection.get_information()
    menu.program_flow()