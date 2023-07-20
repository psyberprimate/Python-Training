

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}


exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

get_to_location = []

#loc = 1

# for match in exits:
#     if loc in exits[match].values():
#         get_to_location.append((match, locations[match]))
#     print(f"Locations leading to {loc}", end='\t')
#     print(get_to_location)
print()
print("Nested loops")
for loc in sorted(locations):
    exit_locations = []
    for exit_path in exits:
        if loc in exits[exit_path].values():
            exit_locations.append((exit_path, locations[exit_path]))    
    print(f"Locations leading to {loc}", end='\t')
    print(exit_locations)
print()
print("List comprehension inside a for loop")
for loc in sorted(locations):
    exit2_locations = [(exit_path, locations[exit_path]) for exit_path in exits if loc in exits[exit_path].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(exit2_locations)
    
print()
print("Nested comprehension")
exits3_locations = [[(exit_path, locations[exit_path]) for exit_path in exits if loc in exits[exit_path].values()]
                    for loc in sorted(locations)]
print(exits3_locations)

print()

for index, loc in enumerate(exits3_locations):
    print("Locations leading to {}".format(index), end='\t')
    print(loc)