print("Welcome to the program!")
print("To gain entry to the holiday, please enter your name and age")
age = int(input("Enter your age: "))
name = input("Enter your name: ")
print("\nChecking...\n")
if (age > 18 and age < 31):
    print("Welcome to the holiday, {0}".format(name))
elif (age > 31):
    print("We are sorry to say, you're too old for this {0} as {1} old".format(name, age))    
else:
    print("You're too young for this EPIC holiday {0}, come back in {1} years".format(name, 18-age))