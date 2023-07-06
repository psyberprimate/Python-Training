computer_parts_selection = {"1" : "computer",
                            "2" : "monitor", 
                            "3" : "keyboard", 
                            "4" :"mouse", 
                            "5" : "mouse mat", 
                            "6" : "hdmi-cable"}


current_choise = None

#computer_parts = []

while current_choise != "0":
    print("Select a part: ")
    current_choise = input("> ")
    if current_choise in computer_parts_selection:
        chosen_part = computer_parts_selection[current_choise]
        print(f"Adding {chosen_part}")
    else:
        print("Incorrect answer. Please add another part.")
        for keys, parts in computer_parts_selection.items():
            print(f"Select -> '{keys}' : {parts}")