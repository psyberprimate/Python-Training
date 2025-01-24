

def oddnumbers_gen():
    start = 1
    while True:
        yield start
        start += 2
        
odd = oddnumbers_gen()

for _ in range(100):
    print(next(odd))
