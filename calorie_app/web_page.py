from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import render_template, request
import calories as cal
import temperature as temp

class HomePage(MethodView):
    
    def get(self):
        return render_template("index_basic.html")


class CaloriesFormPage(MethodView):
    """Simple way to do forms
    """    
    
    def get(self):
        bill_form = CaloriesForm()
        return render_template("form_page_basic.html", bill_form=bill_form)
    
    def post(self):
        bill_form = CaloriesForm(request.form)
        temperature = temp.Temperature(country=bill_form.country.data, 
                                       city=bill_form.city.data).get()
        calories = cal.Calories(weight=float(bill_form.weight.data), 
                                height=float(bill_form.height.data),
                                age=int(bill_form.age.data), 
                                gender=bill_form.gender.data, 
                                temperature=temperature).calculate()
        
        return render_template("form_page_basic.html", bill_form=bill_form, calories=calories)


class CaloriesForm(Form):
    weight = StringField("Weight: ", default = 0)
    height = StringField("Height: ", default = 0)
    age = StringField("Age: ", default=0)
    gender = StringField("Biological gender: male | female", default=None)
    country = StringField("Country: ", default="finland")
    city = StringField("City: ", default="peräjärvi")
    button = SubmitField("Calculate calories")
    
    