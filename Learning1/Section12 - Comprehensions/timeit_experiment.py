import timeit

setup = """\
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
"""

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

#nested_loop = """\ # You can use string or functions without arguments to pass the values to the timeit module
def nested_loop():
    result = []
    for loc in sorted(locations):
        exit_locations = []
        for exit_path in exits:
            if loc in exits[exit_path].values():
                exit_locations.append((exit_path, locations[exit_path]))
        result.append(exit_locations)
        # print(f"Locations leading to {loc}", end='\t')
        # print(exit_locations)
    #print the result before returning
    for _ in result:
        pass    
    return result
#"""

#list_comp = """\ # You can use string or functions without arguments to pass the values to the timeit module
def list_comp():
    result = []
    for loc in sorted(locations):
        exit2_locations = [(exit_path, locations[exit_path]) for exit_path in exits if loc in exits[exit_path].values()]
        result.append(exit2_locations)
        #print("Locations leading to {}".format(loc), end='\t')
        #print(exit2_locations)
    #print the result before returning
    for _ in result:
        pass
    return result    
#"""    

#nested_comp = """\ # You can use string or functions without arguments to pass the values to the timeit module
def nested_comp():
    exits3_locations = [[(exit_path, locations[exit_path]) for exit_path in exits if loc in exits[exit_path].values()]
                        for loc in sorted(locations)]
    #print the result before returning
    for _ in exits3_locations:
        pass  
    return exits3_locations
    # for index, loc in enumerate(exits3_locations):
    #     print("Locations leading to {}".format(index), end='\t')
    #     print(loc)
#"""
def nested_gen():
    exits4_locations = ([(exit_path, locations[exit_path]) for exit_path in exits if loc in exits[exit_path].values()]
                        for loc in sorted(locations))
    #print the result before returning
    for _ in exits4_locations:
        pass  
    return exits4_locations


print(nested_loop())
print(list_comp())
print(nested_comp())

result1 = timeit.timeit(nested_loop, setup, number=1000)
result2 = timeit.timeit(list_comp, setup, number=1000)
result3 = timeit.timeit(nested_comp, setup, number=1000)
result4 = timeit.timeit(nested_gen, setup, number=1000)

print("Nested loop:\t{}".format(result1))
print("List comprehension:\t{}".format(result2))
print(f"Nested comprehension:\t{result3}")
print(f"Nest generator:\t{result4}")