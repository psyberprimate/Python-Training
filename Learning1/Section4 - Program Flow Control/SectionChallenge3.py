
directions = ["north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west"]

chosen_direction = ""

print("Welcome to the navigation program \n\n")

while True:
    print("*"*50)
    print("Directions to choose from: north, north-east, east, south-east. south, south-west, west and north-west")
    print("Write '0' to exit")
    print("*"*50)
    chosen_direction = input("Enter your desired direction: ")
    if chosen_direction.casefold() in directions:
        print("You have chosen to head towards {}".format(chosen_direction))
    elif chosen_direction == "0":
        print("Goodbye")
        break    
    else:
        print("Invalid directions chosen. Please choose again")
    input("Press enter to continue forwards")        