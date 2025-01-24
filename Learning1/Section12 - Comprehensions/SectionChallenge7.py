# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.

import timeit
from statistics import mean, stdev

fact_test = """\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
    
x = fact(100)
"""
factorial_test = """\
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
        
x = factorial(100)
"""

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

#A Dummy function can be used to pass the values in factorial function and not run at start
# def fact_t():
#     fact(100)
#     return fact

# def factorial_t():
#     factorial(100)
#     return factorial
    
    
#fact_t = fact(100)
#factorial_t = factorial(100)

# result1 = timeit.timeit(lambda : fact(100), number = 1000)
# result2 = timeit.timeit(lambda : factorial(100), number = 1000)

# result1 = timeit.timeit(fact_t, number = 1000)
# result2 = timeit.timeit(factorial_t, number = 1000)

result1 = timeit.timeit(fact_test, number = 1000)
result2 = timeit.timeit(factorial_test, number = 1000)

print(result1)
print(result2)

if __name__ == '__main__':
    #print(timeit.timeit("x = fact(100)", setup="from __main__ import fact", number = 1000))
    #print(timeit.timeit("x = factorial(100)", setup="from __main__ import factorial", number = 1000))
    
    list1 = timeit.repeat("x = fact(100)", setup="from __main__ import fact", number = 1000, repeat = 5)
    list2 = timeit.repeat("x = factorial(100)", setup="from __main__ import factorial", number = 1000, repeat = 5)
    
    print()
    print(mean(list1), stdev(list1))
    print(mean(list2), stdev(list2))