def fizz_buzz(num: int) -> str:
    """_summary_
    If number is divisible by 3 returns "fizz", if the number is divisible by 5 return "buzz" and if the number is divisible by both return "fizzbuzz"
    Args:
        num (int): _description_    takes the number to test(int)

    Returns:
        str: _description_  returns a string describing the contents 
    """    
    if num % 3 == 0 and num % 5 == 0:
        return "fizz buzz"
    elif num % 3 == 0: 
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)

#Fizzbuzz for exercise
#for i in range(1, 101):
#    print(fizz_buzz(i))

loop_count = 1
loop_number = 1

print("Welcome to FizzBuzz GAME!!!!")
print("We will go from 1 to 100, answer as number, 'fizz buzz' or 'fizz' or 'buzz' ")

while loop_count != 100:
    answer = fizz_buzz(loop_number)
    print("NUMBER IS: {}".format(loop_number))
    #print("FIZZ BUZZ BOT 3000: {}".format(answer))
    player_answer = "".join(input("Enter your answer: "))

    if player_answer == answer:
        print("*FIZZ BUZZ BOT 3000* *CORRECT ANSWER*")
        loop_count += 1
        loop_number += 1
    else:
        print("*FIZZ BUZZ BOT 3000* *WRONG ANSWER*")
        break    
else:
    print("Game won. Congradulations!")