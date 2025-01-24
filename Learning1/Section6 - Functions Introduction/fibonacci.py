def fibonacci(n: int) -> int:
    """Return the 'n' th Fibonacci number, for positive 'n'."""
    if 0 <= n <= 1:
        return n
    
    result = None
    n_minus1, n_minus2 = 1, 0
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result 

    return result    

for i in range(40):
    print(i, fibonacci(i))