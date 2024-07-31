import sys
from ticket import Ticket

class User():
    
    def __init__(self, name):
        self.name = name
    
    def buy(self, seat : object, card : object):
        """Gets seat and card objects and tries to by
        a seat for the user
        """
        if not seat.is_free():
            price_of_seat = seat.get_price() 
            card_validation_result, message = card.validate(price=price_of_seat)
            if card_validation_result:
                print(message)
                seat.occupy()
                card.purchase_ticket(price=price_of_seat)
                Ticket(customer=self.name, seat_price=price_of_seat,
                       seat_number=seat.seat_id).print_pdf(Ticket.path)
                sys.exit("Ticket bought succesfully, please check"
                         "your printed ticked")
            else:
                print()
                print(message)
                print()
            
        else:
            print()
            print(f"The seat {seat.seat_id} is already occupied")
            print("Please, choose another seat!")
            print()

if __name__ == "__main__":
    pass
    
