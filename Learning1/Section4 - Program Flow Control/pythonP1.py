answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("Well done, you guessed it")
elif guess != answer:
    if guess < answer:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input())
    if guess != answer:
        print("Sorry, you have not guessed correctly")
    else:
        print("Well done, you guessed it")



"""
if guess != answer: # change to if guess is equal to answer
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else: 
    print("You got it first time")
"""    