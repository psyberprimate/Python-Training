print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number to estimated its square: "))

squares = [number ** 2 for number in numbers]

#print(squares)
index_pos = numbers.index(number)
print(squares[index_pos])