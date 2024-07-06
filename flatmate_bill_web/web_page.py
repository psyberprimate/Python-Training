from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, FieldList, FormField
from flask import render_template, request
from libraries import flatmate, bill


"""
Unfinished - All the classes do not work yet, there's a problem with returning the output from  BillResultPage()
 in  bill_forms = BillFormList(request.form)
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
        the_bill_template = BillFormTemplate(request.form)
        the_bill = bill.Bill(float(the_bill_template.amount.data),  the_bill_template.period.data)
        n_flatmates = int(the_bill_template.number_of_flatmates.data)
        bill_list = BillFormList(n_flatmates, the_bill)
        for i in range(len(bill_list.list)):
            bill_list.list[i] = BillForm()
        return render_template("bill_form_page.html", bill_form=bill_list, enumerate=enumerate)

class BillResultPage(MethodView):
    """
    Takes user input from bill form and calculates the split bill based on user input,
    returns a dictionary with 'name' : amount_to_pay
    """    
    def post(self):
        pays = {}
        flatmate_bill_combined_amount = 0
        # Currently there a problem here, the BillFormList has to be re-thinked
        # or something, the user data cannot be request back like its being done below
        bill_forms = BillFormList(request.form)  # DOes not work
        the_bill = bill_forms.bill
        bill_form_list = bill_forms.list
        print(the_bill)
        #get combined days for all of the flatmates
        for flatmate_bill in bill_form_list:
            flatmate_bill_combined_amount += flatmate_bill.days_in.data
        flatmates_bill_combined = flatmate.Flatmate('', int(flatmate_bill_combined_amount))
        # Go through all of the flatmates and add to dictionary to get the results
        for flatmate_bill in bill_form_list:
            flatmate_ind = flatmate.Flatmate(flatmate_bill.name.data, int(flatmate_bill.days_in.data))
            pays[flatmate_ind.name] = flatmate_ind.pays(the_bill, flatmates_bill_combined)
        
        
        return render_template("result_form_page.html", bill_form_result=pays)

class BillFormTemplate(Form):
    amount = StringField("Bill Amount: ", default = 0)
    period = StringField("Bill period: ", default = None)
    number_of_flatmates = StringField("Enter the amount of flatmates: ", default=2)
    button = SubmitField("Make the template")
    
class BillFormList():
    """
    Initialize the class to be posted to the method
    """    
    def __init__(self, lenght: int, the_bill: object):
        self.list = [None] * lenght
        self.bill = the_bill
        
class BillForm(Form):
    name = StringField("Name: ", default=None)
    days_in = StringField("Days in the house: ", default=0)
    button = SubmitField("Calculate Bill")
    




    
    

    