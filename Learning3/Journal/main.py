import database 

def program_flow():
    """ Controls the program flow for the user menu
    """
    print("Programming Diary")
    while(True):
        print("***************************************")
        print("\nSelect one of the following options: ")
        print("\n1) Add new entry for today.\n2) View entries.\n3) Exit.")
        try:
            user_input = int(input("\nYour selection: "))
        except:
            print("Error! Not a number!")
            continue
        match user_input:
            case 1:
                database.add_new_entry()
            case 2:
                database.see_entries()
            case 3:
                print("Goodbye")
                break
            case _:
                print("Select between choices 1-3")
        print("\n")


if __name__ == "__main__":
    program_flow()