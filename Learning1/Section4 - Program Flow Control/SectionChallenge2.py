import random

highest = 1000
iter = 1
answer = random.randint(1, highest)

guess = int(input("Please enter a number between 1 and {}: ".format(highest)))

print("\nPress '0' to give up and quit\n")

while guess != 0:
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
    guess = int(input("Please enter a number between 1 and {}: ".format(highest)))
    iter += 1