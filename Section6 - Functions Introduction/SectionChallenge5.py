def factorial(number: int) -> int:
    """_summary_
    Returns the factorial of number N
    Args:
        number (int): _description_     Factorial N

    Returns:
        int: _description_  Return factorial of N
    """    
    #factorial_n = 1
    #for i in range(1, number+1):
    #    factorial_n *= i
    #return factorial_n#lambda factorial : (for i in range(1, number+1) factorial *= 1)#factorial

    #With recursion
    if number <= 1:
        return 1
    return number * factorial(number - 1)


for i in range(1, 36):
    print("{} {}".format(i, factorial(i)))