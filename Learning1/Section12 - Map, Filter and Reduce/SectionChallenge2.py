from data import basic_plants_list, plants_list, plants_dict

#search = "Cactus"
search = "Grass"

#print(plants_dict['Andromeda'])

#if any([plant for plant in plants_dict if search in plants_dict[plant]]):
if any((plant.plant_type == search for plant in plants_dict.values())):
    print(f"This pack contains {search}s")
else:
    print(f"No {search} in this pack")