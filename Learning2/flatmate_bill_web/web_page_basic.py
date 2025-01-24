from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import render_template, request
from libraries import flatmate, bill


class HomePage(MethodView):
    
    def get(self):
        return render_template("index_basic.html")

class BillFormPage(MethodView):
    """Simple way to do forms
    """    
    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page_basic.html",
                               bill_form_template=bill_form)


class BillResultPage(MethodView):
    """Takes user input from bill form and calculates the split bill based on user input,
    returns a dictionary with 'name' : amount_to_pay
    """    
    def post(self):
        bill_form = BillForm(request.form)
        the_bill = bill.Bill(float(bill_form.amount.data),
                             bill_form.period.data)
        flatmate1 = flatmate.Flatmate(bill_form.name1.data,
                                      int(bill_form.days_in1.data))
        flatmate2 = flatmate.Flatmate(bill_form.name2.data,
                                      int(bill_form.days_in2.data))
        
        pays = {flatmate1.name : flatmate1.pays(the_bill, flatmate2),
                flatmate2.name: flatmate2.pays(the_bill, flatmate1)}
        
        return render_template("result_form_page_basic.html", bill_form_result=pays)

class BillForm(Form):
    amount = StringField("Bill Amount: ", default = 0)
    period = StringField("Bill period: ", default = None)
    
    name1 = StringField("Name: ", default=None)
    days_in1 = StringField("Days in the house: ", default=0)
    
    name2 = StringField("Name: ", default=None)
    days_in2 = StringField("Days in the house: ", default=0)
    
    button = SubmitField("Calculate Bill")