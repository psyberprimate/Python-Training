

def oddnumbers_gen():
    start = 1
    while True:
        yield start
        start += 2
     
     
def pi_series():
    odd = oddnumbers_gen()      
    approximation = 0
    while True:
        approximation += (4 / next(odd))  
        yield approximation
        approximation -= (4 / next(odd))
        yield approximation
        
approx_pi = pi_series()


for _ in range(1000000):
    print(next(approx_pi))
