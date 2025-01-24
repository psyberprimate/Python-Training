def fact(n : int) -> int:
    """_summary_
    calculate n! iteratively
    Args:
        n (int): _description_

    Returns:
        int: _description_
    """    
    result = 1
    if n > 1:
        for f in range (2, n + 1):
            result *= f
    return result


def factorial(n : int) -> int:
    """_summary_
    Calculate n! by recursion
    Args:
        n (int): _description_

    Returns:
        int: _description_
    """    
    if n <= 1:
        return 1
    else:
        return n * factorial(n)
    

def fibonacci_recursion(n : int) -> int:

    if n < 2:
        return n 
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
    #return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_iterative(n : int) -> int:
    if n == 0:
        result = 0
    elif n == 1:
        result = 1  
    else:
        n_minus2, n_minus1 = 0, 1
        for f in range(n - 1):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result 
    return result    

for i in range(30):
    #print(i, fact(i))        
    #print(i, fibonacci_recursion(i))  
    print(i, fibonacci_recursion(i), fibonacci_iterative(i))