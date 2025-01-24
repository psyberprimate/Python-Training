import sqlite3

class Card():
    """A class for saving the card information and
    validation of said information
    """    
    database_path = "cinema_tickets_booking/banking.db"
    
    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        
    def validate(self, price) -> tuple:
        connection = sqlite3.connect(Card.database_path)
        cursor = connection.cursor()
        cursor.execute(f"""
                       SELECT * FROM "Card" WHERE "holder"="{self.holder}"
                       """)
        [(card_type, card_number, card_cvc, card_holder, \
        card_balance)] = cursor.fetchall()
        connection.close()
        
        if self.type==card_type and self.number==card_number \
            and self.cvc == card_cvc and self.holder==card_holder:
            if card_balance-price >= 0:
                return (True, "Card validated succesfully")
            else:
                #print("Card does not have enough balance for the transaction")
                return (False, "Card does not have enough balance for the transaction")
        else:
            #print("Card details do not match existing cards")
            return (False, "Card details do not match existing cards")
        
    def get_balance(self):
        connection = sqlite3.connect(Card.database_path)
        cursor = connection.cursor()
        cursor.execute(f"""
                       SELECT "balance" FROM "Card" WHERE "holder"="{self.holder}"
                       """)
        [result] = cursor.fetchall() # unpacking from a list containing a tuple
        result = result[0]
        connection.close()
        return result
        
    def purchase_ticket(self, price : float):
        card_balance = self.get_balance()
        connection = sqlite3.connect(Card.database_path)
        connection.execute(f"""
                           UPDATE "Card" SET "balance"={float(card_balance)-price} WHERE 
                           "holder"="{self.holder}"
                           """)
        connection.commit()
        connection.close()
        
    def details_update(self, balance : float):
        connection = sqlite3.connect(Card.database_path)
        connection.execute(f"""
                           UPDATE "Card" SET "balance"={balance} WHERE 
                           "holder"="{self.holder}"
                           """)
        connection.commit()
        connection.close()
        
    
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
                       VALUES ("Visa", 6020331, 128,
                       "Poor Poorson", 50)
                       """)
    connection.commit()
    connection.close()

def delete_record(holder : str):
    """ Delete the 'selection' pass on the table
    with provided 'value' table columns: seat_id, taken, price 
    """
    connection = sqlite3.connect(path)
    connection.execute("""
                   DELETE FROM "Card" WHERE "holder"="{}"
                   """.format(holder))
    connection.commit()
    connection.close()

if __name__ == "__main__":
    card = Card(type="Visa", number=6020331, cvc=128,
                holder="Poor Poorson")
    print(card.validate(price=51))
    #print(card.get_balance())
    #print(card.details_update(balance=250))
    #create_table()
    #insert_data()
    #delete_record(holder="Poor Poorson")
    #delete_record(holder="John Smith")