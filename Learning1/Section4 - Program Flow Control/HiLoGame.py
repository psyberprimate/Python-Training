low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press enter to start the searching")

count = 1

while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                    "Enter h or l, or c if my guess is correct or you want to quit."
                    .format(guess)).casefold()
    if high_low == "h":
        #Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        #Guess lower. The high ned of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        #Quit the game
        print("The value was found in {} after {} guesses".format(guess, count))
        break
    else:
        print("Please enter h, l or c")      
    count += 1       