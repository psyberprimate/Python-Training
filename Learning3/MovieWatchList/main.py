import database
import datetime 

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

def get_time(time : str):
    date = datetime.datetime.fromtimestamp(time)
    return date.strftime("%d-%m-%Y")

def parse_time(time : str):
    parsed_date = datetime.datetime.strptime(time, "%d-%m-%Y")
    return parsed_date.timestamp()

def print_movie_list(list : list):
    if list:
        for movie_id, title, release_date in list:
            print(f"{movie_id}: {title} ({get_time(release_date)})")
    else:
        print_menu(title="User has not watched any movies")

def new_movie():
    print_menu(title="Adding new movie")
    print_menu(title="")
    movie = input("Movie name: ")
    date = input("Enter the date (dd-mm-yyyy): ")
    database.add_new_movie(movie=movie, date=parse_time(date))

def show_upcoming_movies():
    print_menu(title="Upcoming Movies")
    print_menu(title="")
    movies = database.view_upcoming_movies()
    print_movie_list(movies)

def show_all_movies():
    print_menu(title="All Movies")
    print_menu(title="")
    movies = database.view_all_movies()
    print_movie_list(movies)

def add_watched_movie():
    viewer = input("Give the user's name: ")
    movie_id = input("Give movie id you watched: ")
    database.add_watched_movie(viewer=viewer, movie_id=movie_id)
    
def show_watched_movies(viewer : str = None, ask_input : bool = True):
    print_menu(title="Watched Movies")
    print_menu(title="")
    if ask_input:
        viewer = input("Give user name: ")
        user_movies = database.view_watched_movies(viewer=viewer)
    else:
        user_movies = database.view_watched_movies(viewer=viewer)
    print_movie_list(user_movies)

def show_users():
    print_menu(title="Users")
    print_menu(title="")
    users = database.show_users()
    for user in users:
        print(f"User: {user[0]}")
    
def add_user():
    new_user = input("Username: ")
    database.add_user(new_user=new_user)
    print(f"User added: {new_user}")
    
def delete_user():
    show_users()
    delete_user = input("Username to be deleted: ")
    database.delete_user(delete_user=delete_user)
    print(f"User with username: {delete_user} was deleted!")
    
def delete_from_user_list():
    print_menu(title="DELETE")
    print_menu(title="")
    user_name = input("User name: ")
    show_watched_movies(viewer=user_name, ask_input=False)
    title = input("Movie id: ")
    database.delete_from_user_list(user_name=user_name, title = title)
  
def user_settings():
    print_menu(title="User settings menu")
    while(True):
        print_menu(title="")
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
                show_users()
            case 2:
                add_user()
            case 3:
                delete_user()
            case 4:
                delete_from_user_list()
            case 5:
                break
            case _:
                print("Select between choices 1-5")
    
def program_flow():
    """ Controls the program flow for the user menu
    """
    while(True):
        print_menu(title="Watchlist")
        print_menu(title="")
        print("Select one of the following options: ")
        print("\n1) Add new movie.\n2) View upcoming movies.\n3) View all movies. \
              \n4) Add watched movie. \n5) View watched movies. \n6) Show user settings. \
                  \n7) Exit.")
        try:
            user_input = int(input("\nYour selection: "))
        except:
            print_menu(title="Error! Not a number!")
            continue
        match user_input:
            case 1:
                new_movie()
            case 2:
                show_upcoming_movies()
            case 3:
                show_all_movies()
            case 4:
                add_watched_movie()
            case 5:
                show_watched_movies()
            case 6:
                user_settings()
            case 7:
                print_menu(title="Goodbye")
                break
            case _:
                print_menu(title="Select between choices 1-7")

if __name__ == "__main__":
    program_flow()