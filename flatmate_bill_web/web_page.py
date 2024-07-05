from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import render_template, request
from libraries import flatmate, bill


"""
Unfinished - All the classes do not work yet, there's a problem with returning the output from  BillResultPage()
!!!!!FIX!!!!!
"""

class HomePage(MethodView):
    
    def get(self):
        return render_template("index.html")

class BillFormTemplatePage(MethodView):
    """
    Takes the user input for flatmate bill template
    """    
    def get(self):
        bill_form_template = BillFormTemplate()
        return render_template("bill_form_template_page.html", bill_form_template=bill_form_template)
    
class BillFormPage(MethodView):
    """
    Creates bill form based on user input from BillFormTemplatePage()
    """    
    def post(self):
        bill_list = [] # list for the bill_forms_per_flatmate
        
        the_bill = BillFormTemplate(request.form)
        amount = float(the_bill.amount.data)
        period = the_bill.period.data
        n_flatmates = int(the_bill.number_of_flatmates.data)
        for _ in range(n_flatmates):
            bill_list.append(BillForm())
        return render_template("bill_form_page.html", amount=the_bill.amount.data, period=the_bill.period.data, bill_form=bill_list)


class BillResultPage(MethodView):
    """
    Takes user input from bill form and calculates the split bill based on user input,
    returns a dictionary with 'name' : amount_to_pay
    """    
    def post(self):
        pays = {}
        
        bill_information = BillFormTemplate(request.form)
        bill_forms = BillForm(request.form)
        
        the_bill = bill.Bill(float(bill_information.amount.data), bill_information.period.data)
        
        return render_template("result_form_page.html", bill_form_result=pays)


class BillFormTemplate(Form):
    amount = StringField("Bill Amount: ", default = 0)
    period = StringField("Bill period: ", default = None)
    number_of_flatmates = StringField("Enter the amount of flatmates: ", default=2)
    button = SubmitField("Make the template")
    
class BillForm(Form):
    name = StringField("Name: ", default=None)
    days_in = StringField("Days in the house: ", default=0)
    button = SubmitField("Calculate Bill")


    
    

    