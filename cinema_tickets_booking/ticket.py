import random
from fpdf import FPDF
import string

class Ticket():
    
    path = "cinema_tickets_booking/"
    
    def __init__(self, customer, seat_price, seat_number, filename: str = "ticket"):
        self.id = "".join([random.choice(string.ascii_letters) for _ in range(10)])
        self.customer = customer
        self.seat_price = seat_price
        self.seat_number = seat_number
        self.filename = filename + "_" + self.id + "_" + ".pdf"
        
    def print_pdf(self, path):
        
        pdf = FPDF(orientation='P', unit='pt', format="A4")
        pdf.add_page()
        #general settings
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Cinema Ticket", border=0, align='C', ln=1)
        pdf.cell(w=150, h=40, txt="Customer:", border=0)
        pdf.cell(w=150, h=40, txt=self.customer, border=0, ln=1)
        
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Seat number:", border=1)
        pdf.cell(w=100, h=40, txt=self.seat_number, border=1, ln=1)
        pdf.cell(w=100, h=40, txt="Seat price:", border=1)
        pdf.cell(w=100, h=40, txt=str(self.seat_price), border=1)
        #output
        pdf.output(path+self.filename)
        

if __name__ == "__main__":
    ticket = Ticket(customer="X", seat_price=9000, seat_number="X")
    ticket.print_pdf(path=Ticket.path)