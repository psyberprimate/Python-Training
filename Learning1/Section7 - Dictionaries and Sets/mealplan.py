from contents import pantry, recipes

#Alternative method to update list
#def add_shopping_list(data: dict, *args) -> None: # Original solution using tuples as str and int and modifying the directionary directly
    #    if args[0] in data:
    #    data[args[0]] += args[1]
    #else:
    #    data[args[0]] = args[1]

def add_shopping_list(data: dict, items: str, amount: int) -> None: # You could always get, 
    """_summary_
    add items to the shopping list
    """   
    #if items in data:
    #    data[items] += amount
    #else:
    #    data[items] = amount
    data[items] = data.setdefault(items,0) + amount


#display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# Compreheson should be used over the below method
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    #Display a menu of recipes

    if shopping_list.items != {}:
        print("You shopping list:")
        for index, items in shopping_list.items():
            print(f"{index} : {items}")

    print("Please choose your recipe")
    print("-"*20)
    for key, value in display_dict.items():
        print(f"{key} : {value}")
    choice = input(": ")

    if choice == "0":
        print(f"{choice} Enter to exit")
        break   

    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        ingredients = recipes[selected_item]
        print(ingredients)
        print(f"To make: {selected_item}")
        for ingredient, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(ingredient, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"You have enough of: {ingredient}")
            else:
                print(f"You lack the ingredients: {ingredient} of {required_quantity-quantity_in_pantry}")
                print(f"Adding item to the shopping list... {ingredient}")
                add_shopping_list(shopping_list,ingredient, required_quantity-quantity_in_pantry)
    input("Press ENTER to process\n\n")            