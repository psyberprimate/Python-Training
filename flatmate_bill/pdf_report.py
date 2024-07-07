from fpdf import FPDF
import webbrowser
import os

class PdfReport:
    """Generates a pdf file that contains the data about flatmate bill such as their names, their payment amount for the bill,
    and the period of the bill
    """    
    def __init__(self, filename: str = "default"):
        
        self.filename = filename + ".pdf"
        
        
    def generate(self, flatmate1, flatmate2, bill):
        
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        
        pdf = FPDF(orientation='P', unit='pt', format="A4")
        pdf.add_page()
        #add icon
        pdf.image("flatmate_bill/files/house.png", w=30, h=30)
        #general settings
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=0, align='C', ln=1)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1) # remember to add 'ln' to get a newline 
        #flatmate 1 - name and due amount
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate1_pay, border=0, ln=1) # remember to add 'ln' to 
        #get a newline 
        #flatmate 2 - name and due amount
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate2_pay, border=0)
        #output
        pdf.output("flatmate_bill/files"+self.filename)
        
        #os.chdir(flatmate_bill/files)
        
        webbrowser.open("flatmate_bill/files"+self.filename) # do not work for some reason
        