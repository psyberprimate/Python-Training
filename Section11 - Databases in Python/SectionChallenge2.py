import sqlite3

db = sqlite3.connect("Section11 - Databases in Python/contacts.sqlite")

row_name_check = input("Please enter a name: ")


## I HAVE NO IDEA, WELL TO BE EXACT i am NOT SURE WHY THIS DERENFENCING WORKS IN LIKE 14. My GUESS is that the sqlite is written in C and you can derefrence a pointer because of that.
# update_sql = "SELECT * FROM contacts WHERE name LIKE ?"
# print(update_sql)
# update_cursor = db.cursor()
# update_cursor.execute(update_sql, (row_name_check,)) #executescript
# #print(*update_cursor)
# print("{} rows searched".format(*update_cursor))

for row in db.execute("SELECT * FROM contacts WHERE name=?", (row_name_check,)):
    #print(f"name : {row[0]}, phone number: {row[1]}, email : {row[2]}")
    print(row)
    print("-"*20)
    
db.close()