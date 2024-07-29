import sqlite3


class Seat():
    
    database_path = "cinema_tickets_booking/cinema.db"
    
    def __init__(self, seat_id : str):
        self.seat_id = seat_id
    
    def select_all() -> list:
        """Returns a .fetchall request from database as a list
        """    
        connection = sqlite3.connect(Seat.database_path)
        cursor = connection.cursor()
        cursor.execute("""
                    SELECT * FROM "Seat"
                    """)
        result = cursor.fetchall()
        connection.close()
        return result
    
    def get_price(self) -> list:
        connection = sqlite3.connect(Seat.database_path)
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT "price" FROM "Seat" WHERE "seat_id"="{}"
                       """.format(self.seat_id))
        result = cursor.fetchall()
        connection.close()
        return result
    
    def is_free(self):
        connection = sqlite3.connect(Seat.database_path)
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT "taken" FROM "Seat" WHERE "seat_id"="{}"
                       """.format(self.seat_id))
        result = cursor.fetchall()
        connection.close()
        return result
    
    def occupy(self) -> str:
        """Check if the table entry is taken or not and if not reserve it
        """        
        # since .is_free() returns a list with a tuple(s),
        #[0][0] to access the exact value of 'taken' -> 1 == taken, 0 == free
        check_if_free = self.is_free()[0][0]
        if not check_if_free == 1: 
            connection = sqlite3.connect(Seat.database_path)
            connection.execute(f"""
                            UPDATE "Seat" SET "taken"=1 WHERE "seat_id"="{self.seat_id}"
                            """)
            connection.commit()
            connection.close()
            return f"Seat {self.seat_id} was succesfully reserved"
        else:
            return f"Seat {self.seat_id} is already occupied"
        
if __name__ == "__main__":
    seat1 = Seat(seat_id="A1")
    seat2 = Seat(seat_id="A2")
    print()
    print()
    print(seat1.get_price())
    print()
    print(seat2.get_price())
    print()
    print(seat1.is_free())
    print()
    print(seat2.is_free())
    print()
    print(seat1.occupy())
    print()
    print(seat2.occupy())