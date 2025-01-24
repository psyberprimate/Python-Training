import sqlite3


class Seat():
    
    database_path = "cinema_tickets_booking/cinema.db"
    
    def __init__(self, seat_id : str):
        self.seat_id = seat_id
    
    def get_seats(self) -> list:
        """Returns a .fetchall request for "seat_id" from 
        database as a list
        """    
        connection = sqlite3.connect(Seat.database_path)
        cursor = connection.cursor()
        cursor.execute("""
                    SELECT "seat_id" FROM "Seat"
                    """)
        result = cursor.fetchall()
        connection.close()
        return result
    
    def get_price(self) -> float:
        connection = sqlite3.connect(Seat.database_path)
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT "price" FROM "Seat" WHERE "seat_id"="{}"
                       """.format(self.seat_id))
        [result] = cursor.fetchall() # unpack
        result = result[0] #data comes as [(data),]
        connection.close()
        return result
    
    def is_free(self) -> int:
        """Check if the seat_id is free, returns 1 or 0
        """        
        connection = sqlite3.connect(Seat.database_path)
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT "taken" FROM "Seat" WHERE "seat_id"="{}"
                       """.format(self.seat_id))
        [result] = cursor.fetchall() #unpacking value
        result = result[0]
        connection.close()
        return result
    
    def occupy(self) -> str:
        """Check if the table entry is taken or not and
        if not reserve it
        """        
        check_if_free = self.is_free()
        if not check_if_free == 1: 
            connection = sqlite3.connect(Seat.database_path)
            connection.execute(f"""
                            UPDATE "Seat" SET "taken"=1 WHERE
                            "seat_id"="{self.seat_id}"
                            """)
            connection.commit()
            connection.close()
            return f"Seat {self.seat_id} was succesfully reserved"
        else:
            return f"Seat {self.seat_id} is already occupied"
        
if __name__ == "__main__":
    #seat1 = Seat(seat_id="A1")
    seat2 = Seat(seat_id="A3")
    # print()
    # print(seat1.get_seats())
    # print()
    # print(seat1.get_price())
    # print()
    # print(seat2.get_price())
    # print()
    # print(seat1.is_free())
    # print()
    # print(seat2.is_free())
    # print()
    # print(seat1.occupy())
    # print()
    print(seat2.occupy())