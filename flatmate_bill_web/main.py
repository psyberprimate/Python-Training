from flask import Flask
import web_page_basic as web # basic
#import web_page as web # free flatmate amount

if __name__ == '__main__':
    
    #basic
    app = Flask(__name__, template_folder='html_templates/basic')
    
    # free amount of flatmates
    # app = Flask(__name__, template_folder='html_templates/free')
    
    #basic - Works -
    app.add_url_rule('/', view_func=web.HomePage.as_view('home_page'))
    app.add_url_rule('/bill', view_func=web.BillFormPage.as_view('bill_form_page_basic'))
    app.add_url_rule('/results', view_func=web.BillResultPage.as_view('results_form_page'))
    
    # not fixed flatmate amount - Does not work - 
    # app.add_url_rule('/', view_func=web.HomePage.as_view('home_page'))
    # app.add_url_rule('/billtemplate', view_func=web.BillFormTemplatePage.as_view('bill_form_template_page'))
    # app.add_url_rule('/bill', view_func=web.BillFormPage.as_view('bill_form_page'))
    # app.add_url_rule('/results', view_func=web.BillResultPage.as_view('results_form_page'))

    app.run()#debug=True)