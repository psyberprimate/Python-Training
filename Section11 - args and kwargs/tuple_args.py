

def build_tuple(*args) -> tuple:
    return args
    
    
if __name__ == '__main__':
    print("Hello, write a writing tuples")
    
    msg_tuple = build_tuple("krak", "grenade", "launcher", "PEACE")
    int_tuple = build_tuple(1, 10, 5)
    float_tuple = build_tuple(1.3, 2.5, 5.9, 8.2, 3.4, 5.1, 20.20)
    
    print(type(msg_tuple))
    print(msg_tuple)
        
    print(type(int_tuple))
    print(int_tuple)
    
    print(type(float_tuple))
    print(float_tuple)    