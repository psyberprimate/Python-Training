import random
import string

class Ticket():
    
    def __init__(self, customer, seat_price, seat_number):
        self.id = "".join([random.choice(string.ascii_letters) for _ in range(10)])
        self.customer = customer
        self.seat_price = seat_price
        self.seat_number = seat_number
        
    def print_pdf(self, path):
        pass