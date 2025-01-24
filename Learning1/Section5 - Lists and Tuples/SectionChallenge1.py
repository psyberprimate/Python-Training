menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]


#Just print out the other parts of the list
#Solution 1
""" for meals in menu:
        if "spam" in meals:
            for items in meals:
                 if items != "spam":
                    print(items)
            print()        
        else:
            print(meals) """
#solution 2
menu_optional = menu

""" for meals in range(len(menu_optional) - 1, -1, -1):
    if "spam" in menu_optional[meals]:
        for item in range(len(menu_optional[meals])- 1, -1, -1):
            if "spam" in menu_optional[meals][item]:
                del  menu_optional[meals][item]
    else:
        pass
    #print(meals)
    print(menu_optional[meals])
#print(menu_optional)   """          

#solution 3
for meals in menu_optional:
    for item in range(len(meals)- 1, -1, -1):
        if "spam" in meals[item]:
            del  meals[item]
    print(meals)