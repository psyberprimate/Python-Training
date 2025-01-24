current_choise = "-"
computer_parts = []
computer_parts_selection = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi-cable"]
valid_choises = []

for i in range(1, len(computer_parts_selection) + 1):
    valid_choises.append(str(i))

while current_choise != "0":
    print("Please choose an option to choose from: ")

    for number, part in enumerate(computer_parts_selection): 
        print("{0}: {1}".format(number + 1, part))

    print("0: To exit")
    current_choise = input("Please choose what parts to add to the list: ")

    if current_choise in valid_choises:
        #print(computer_parts_selection[index])
        computer_parts.append(computer_parts_selection[int(current_choise)-1])
        print("Adding {}".format(computer_parts_selection[int(current_choise)-1]))

print(computer_parts)