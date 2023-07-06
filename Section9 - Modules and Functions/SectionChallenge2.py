import pytz
import datetime

def time_zone_and_local(string: str, index: int)->None:
    ## 1st solution not working properly
    # print('UTC time zone for: {} is: {}'.format(string, pytz.utc.localize\
    #                                             (datetime.datetime.utcnow()).astimezone()))
    # print(f'Local time zone for: {string} is: {pytz.utc.localize(datetime.datetime.now())}')
    ## INstructor solution, works better
    tz_disp = pytz.timezone(string)
    world_time = datetime.datetime.now(tz=tz_disp)
    print(f"The time {all_timezones[index]} is { world_time.strftime('%A %x %X %z')} { world_time.tzname()}")
    print(f"Local time is {datetime.datetime.now().strftime('%A %x %X')}")
    print(f"UTC time is {datetime.datetime.utcnow().strftime('%A %x %X')}")
    print()

all_timezones = pytz.all_timezones

#print(all_timezones)
while(True):
    choice = input("Write a timezone name to get the timezone time and local system time OR (0 to quit): ")#.casefold()
    if choice == '0':
        print("Goodbye")
        break
    if choice in all_timezones:
        index = all_timezones.index(choice)
        time_zone_and_local(choice, index)
    else:
        print(f"{choice} not found in timezones, please try again.")
        continue    



