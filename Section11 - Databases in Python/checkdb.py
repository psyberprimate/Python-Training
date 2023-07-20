import sqlite3
import pytz


db = sqlite3.connect("Section11 - Databases in Python/accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM localtransactions"):
    print(row)
#for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', transactions.time, 'localtime') AS localtime,"
#                      "transactions.account, transactions.amount FROM transactions ORDER BY transactions.time"):
    
    
    # utc_time = row[0]
    # local_time = pytz.utc.localize(utc_time).astimezone()
    # print("{}\t{}".format(utc_time, local_time))
    print(row)

db.close()
