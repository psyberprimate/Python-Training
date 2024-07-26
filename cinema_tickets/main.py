import sqlite3


def create_table():
    
    connection = sqlite3.connect("cinema_tickets/cinema.db")
    connection.execute("""
                    CREATE TABLE "Seat" (
                        "seat_id" TEXT,
                        "taken" INTEGER,
                        "price" REAL
                        );
                    """)
    connection.commit()
    connection.close()
    
def insert_data():
    
    connection = sqlite3.connect("cinema_tickets/cinema.db")
    connection.execute("""
                       INSERT INTO "Seat" ("seat_id", "taken", "price") VALUES ("A1", "0", "90"), ("A2", "1", 90), ("A3", "0", 100)
                       """)
    connection.commit()
    connection.close()
    
def select_all() -> list:
    """Returns a .fetchall request from database as a list
    """    
    connection = sqlite3.connect("cinema_tickets/cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT * FROM "Seat"
                   """)
    result = cursor.fetchall()
    connection.close()
    return result

def select_specific_columns() -> list:
    """aa
    """
    connection = sqlite3.connect("cinema_tickets/cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT "seat_id", "price" FROM "Seat"
                   """)
    result = cursor.fetchall()
    connection.close()
    return result

def select_with_condition(selection : str, operator : str, condition) -> list:
    """Selects column, operator and condition makes a fetchall request
    """
    connection = sqlite3.connect("cinema_tickets/cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT "seat_id", "price" FROM "Seat" WHERE "{}" {} "{}"
                   """.format(selection, operator, condition))
    result = cursor.fetchall()
    connection.close()
    return result
    
def update_value(selection : str, value, filter_key, filter_value):
    """ Update the 'selection' pass on the table with provided 'value'
        table columns: seat_id, taken, price 
    """
    connection = sqlite3.connect("cinema_tickets/cinema.db")
    connection.execute("""
                   UPDATE "Seat" SET "{}"="{}" WHERE "{}"="{}"
                   """.format(selection, value, filter_key, filter_value))
    connection.commit()
    connection.close()

def delete_record(seat_id : str):
    """ Delete the 'selection' pass on the table with provided 'value'
        table columns: seat_id, taken, price 
    """
    connection = sqlite3.connect("cinema_tickets/cinema.db")
    connection.execute("""
                   DELETE FROM "Seat" WHERE "seat_id"="{}"
                   """.format(seat_id))
    connection.commit()
    connection.close()

if __name__ == "__main__":
    #insert_data()
    print(select_all())
    print()
    print(select_specific_columns())
    print()
    print(select_with_condition(selection="price", operator=">",condition=90))
    print()
    update_value(selection="taken",value=int(1), filter_key="seat_id",
                 filter_value="A3")
    print()
    delete_record(seat_id="A3")
    