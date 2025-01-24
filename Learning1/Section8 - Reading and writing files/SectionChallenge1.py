input_filename = 'Section8 - Reading and writing files\country_info.txt'#"C:\Users\oskur\Desktop\Python Training\Section8 - Reading and writing files\country_info.txt"          
#'country_info.txt' 

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        #print(country_dict)
        countries[country.casefold()] = country_dict

print(countries)
print("#"*80)
print("Country data base")

search = ""

while search != "quit":
    search = input(": ")
    print("Write 'search' to search for a country capital'")
    if search.casefold == "search":
        search = input("Enter a country name to search for it in the database: ") # More efficient only to use .casefold() here to get the characters to small characters
        if search.casefold() in countries:
            print(f"{search}'s capital is: {countries[search.casefold()]['capital']}")
        else:
            print(f"{search} was not found by the search in countries")
    else:
        print("Countries without a capital")
        for country in countries:
            if countries[country]['capital'] == "":
                print(f"{countries[country]['name']} doesn't have a capital {countries[country]['capital']}")

else:
    print("Goodbye")
