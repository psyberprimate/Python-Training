def sum_numbers(*args)-> float:
    """_summary_
    Sum all of numbers tohet passed into the function
    Returns:
        float: _description_
    """    
    sum_of_all = 0
    for i in range(len(args)):
        sum_of_all += args[i]
    return sum_of_all

print(sum_numbers(1, 2, 0, 5, 1))