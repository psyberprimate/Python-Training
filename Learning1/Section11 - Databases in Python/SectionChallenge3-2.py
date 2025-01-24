import sqlite3
import pytz


db = sqlite3.connect("Section11 - Databases in Python/accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM transactions"):
    #time1, time2 = row
    #print(pytz.utc.localize(time1), time2)
    print(row)

db.close()
