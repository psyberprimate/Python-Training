from flask.views import MethodView
from wtforms import Form
from flask import Flask

#import flatmate_bill_web.libraries.flatmate,  flatmate_bill_web.libraries.bill

class HomePage(MethodView):
    
    def get(self):
        return "Hello"


class BillFormPage(MethodView):
    
    def get(self):
        return "BILL FORM"


class BillResultPage(MethodView):
    pass


class BillForm(Form):
    pass