import sqlite3

db = sqlite3.connect("Section11 - Databases in Python/contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 765552, 'time@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 12345, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

#print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())


for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-"*20)

cursor.close()
db.commit()
db.close()
