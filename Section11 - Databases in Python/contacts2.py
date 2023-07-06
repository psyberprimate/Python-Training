import sqlite3

db = sqlite3.connect("Section11 - Databases in Python/contacts.sqlite")

new_email = "updated@email.com"
new_phone = input("Please enter your phone number: ")#12345

#update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, new_phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, new_phone)) #executescript
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
update_cursor.connection.commit()
update_cursor.close()

for row in db.execute("SELECT * FROM contacts"):
    name, phone, email = row
    print(f"name : {name}, phone number: {phone}, email : {email}")
    print("-"*20)
    
db.close()