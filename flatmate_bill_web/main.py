from flask import Flask
import web_page as web


if __name__ == '__main__':
    
    app = Flask(__name__)
    
    app.add_url_rule('/', view_func=web.HomePage.as_view('home_page'))
    app.add_url_rule('/bill', view_func=web.BillFormPage.as_view('bill_form_page'))

    app.run()