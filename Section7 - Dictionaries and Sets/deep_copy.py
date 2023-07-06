from contents import recipes

def deep_copy(data: dict)->dict:
    """_summary_
    Copy a dictionary, creating copies of the 'list' or 'dict' values
    Args:
        data (dict): _description_

    Returns:
        dict: _description_
    """    
    new_dict = {}
    for key, items in data.items():
        new_val = items.copy()
        new_dict[key] = new_val
    return new_dict


#parts = {}

parts = deep_copy(recipes)

parts["Butter chicken"]["ginger"] = 300

print(recipes["Butter chicken"]["ginger"])
print(parts["Butter chicken"]["ginger"])
