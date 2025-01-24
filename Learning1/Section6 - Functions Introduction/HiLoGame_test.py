import random

LOW = 1
HIGH = 65535

answer = random.randint(LOW, HIGH)

def guess_binary(answer, LOW, HIGH):
    """_summary_
    A binary guesser for randomised value. 
    Args:
        answer (_type_): _description_
        low (_type_): _description_
        high (_type_): _description_

    Returns:
        _type_: _description_
    """    
    guess_count = 1
    while True:
        guess = LOW + (HIGH - LOW) // 2
        #high_low = input("My guess is {}. Should I guess higher or lower?"
        #                "Enter h or l, or c if my guess is correct or you want to quit."
        #                .format(guess)).casefold()
        #if high_low == "h":
        if guess < answer:
            #Guess higher. The low end of the range becomes 1 greater than the guess.
            LOW = guess + 1
        #elif high_low == "l":
        elif guess > answer:
            #Guess lower. The high ned of the range becomes one less than the guess.
            HIGH = guess - 1
        #elif high_low == "c":
        elif guess == answer:
            #Quit the game
            #print("The value was found in {} after {} guesses".format(guess, guess))
            return  guess_count
        #else:
        #    print("Please enter h, l or c")      
        guess_count += 1 


print("Please think of a number between {} and {}".format(LOW, HIGH))
input("Press enter to start the searching")

correct_count = 0
max_guesses = 0

for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))
    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("I guessed without being told {} times. Max {} guesses.".format(correct_count, max_guesses))

      