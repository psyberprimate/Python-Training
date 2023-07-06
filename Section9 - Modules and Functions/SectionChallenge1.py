import time

def time_info(string: str) -> None:
    """_summary_

    Prints info regarding Clock type and clock information
    
    Args:
        string (str): _description_
    """    
    clock_info = time.get_clock_info(string)
    print(f'Clock type: {string} \n Clock info:{clock_info}')


options = ('time', 'perf_counter', 'monotonic', 'process_time')

while(True):
    print(f"Call docoumentation for the clock type by writing: {options[0]} | {options[1]} | {options[2]} | {options[3]}")
    choice = input(": ").casefold()
    if choice in options:
        time_info(choice)
