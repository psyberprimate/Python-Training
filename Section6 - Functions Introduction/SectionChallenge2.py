import random

def get_integer(prompt):
    """_summary_
    Gets an integer from Standard Input (stdin).

    The function will contiue looping, and prompting the user, until a valid 'int' is entered.
    Args:
        prompt (_type_): _ 
        description_The string that the user will see, when they're prompted to enter the value

    Returns:
        _type_: _description_
        The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else:#Not need when IF executes
        #    print("Invalid number - Enter a value between '{}' and '{}'".format(lowest,highest))
        print("{0} is not a valid number".format(temp))
        

highest = 1000
lowest = 1
iter = 1
guess = 0
answer = random.randint(lowest, highest)

print("\nPress '0' to give up and quit\n")
while guess != answer:
    print("Please enter a number between 1 and {}: ".format(highest))
    guess = get_integer(": ")
    if guess == answer:
        print("You got it correct on the {} try, well done!".format(iter))
        print("You win")
        break
    elif guess > answer:
        print("You guessed too high, maybe try a smaller value")    
    elif guess < answer:
        print("You guess too low, maybe try guessing for a larger value")    
    else:
        if guess != 0:
            print("Invalid value used for guessing -- Guess again")
        else:
            print("You quit")
            break
    
    iter += 1