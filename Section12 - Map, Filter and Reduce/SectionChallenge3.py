name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(f"Your age is: {age}")

message = "You're old enough to vote" if age >= 18 else f"Please come back in {18-age} years"
print(message)