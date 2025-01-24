import sqlite3

db = sqlite3.connect("Section11 - Databases in Python/contacts.sqlite")

# update_sql = "UPDATE contacts SET email = 'update@update.com'" #WHERE contacts.phone = 12345"
# update_cursor = db.cursor()
# update_cursor.execute(update_sql)
# print("{} rows updated".format(update_cursor.rowcount))

# update_cursor.connection.commit()
# update_cursor.close()


for row in db.execute("SELECT * FROM contacts"):
    name, phone, email = row
    print(f"name : {name}, phone number: {phone}, email : {email}")
    #print(row)
    print("-"*20)
    
db.close()