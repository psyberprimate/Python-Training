

def clear() -> None:
    print()
    print('*'*40)
    print()

def devide(num1 : int, num2 : int) -> None:
    try:
        print(f"{num1} / {num2} = {num1/num2}")
    except ZeroDivisionError as ex:    
        print("Error: Cannot divide by zero")

def ask_numbers() -> tuple:
    try:
        num1, num2 = input("Please give two numbers separated by a space: ").split()
        return int(num1), int(num2)    
    except Exception as e:
        print(f"Error {type(e)}")  
        
if __name__ == '__main__' :
    while(True):
        try:
            num1, num2 = ask_numbers()
            devide(num1, num2)
            clear()
        except Exception as e:
            print(f"Error : {type(e)}")    

              