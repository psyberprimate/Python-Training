computer_parts_selection = {"1" : "computer",
                            "2" : "monitor", 
                            "3" : "keyboard", 
                            "4" :"mouse", 
                            "5" : "mouse mat", 
                            "6" : "hdmi-cable"}


current_choise = None

computer_parts = [] # As list
#computer_part = {} # As dict

while current_choise != "0":
    print("Select a part: ")
    current_choise = input("> ")
    if current_choise in computer_parts_selection:
        chosen_part = computer_parts_selection[current_choise]
        if chosen_part in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
            #computer_part.pop(chosen_part)     #DICT
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
            #computer_part[current_choise] = chosen_part    #DICT
            #print(f"Your dictionary now contains parts: {computer_parts}")
    else:
        print("Incorrect answer. Please add another part.")
        for keys, parts in computer_parts_selection.items():
            print(f"Select -> '{keys}' : {parts}")