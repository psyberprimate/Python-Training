import sqlite3

class Card():
    
    database_path = "/cinema_tickets_booking/banking.db"
    
    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        
    def validate(self, price):
        connection = sqlite3.connect(Card.database_path)
        cursor = connection.cursor()
        cursor.execute("""
                       
                       """)
        result = cursor.fetchall()
        connection.close()
        return result
    
path = "cinema_tickets_booking/banking.db"

def create_table():
    
    connection = sqlite3.connect(path)
    connection.execute("""
                    CREATE TABLE "Card" (
                        "type" TEXT,
                        "number" INTEGER,
                        "cvc" INTEGER,
                        "holder" TEXT,
                        "balance" REAL
                        );
                    """)
    connection.commit()
    connection.close()

def insert_data():
    
    connection = sqlite3.connect(path)
    connection.execute("""
                       INSERT INTO "Card" (
                           "type", "number", "cvc", "holder",
                           "balance")
                       VALUES ("Master Card", 1435572, 974,
                       "Voitto Saha", 5000)
                       """)
    connection.commit()
    connection.close()

def delete_record(holder : str):
    """ Delete the 'selection' pass on the table with provided 'value'
        table columns: seat_id, taken, price 
    """
    connection = sqlite3.connect(path)
    connection.execute("""
                   DELETE FROM "Card" WHERE "holder"="{}"
                   """.format(holder))
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_table()