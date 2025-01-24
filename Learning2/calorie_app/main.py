from flask import Flask
import web_page as web # free flatmate amount

if __name__ == '__main__':
    app = Flask(__name__, template_folder='html_templates')
    app.add_url_rule('/', view_func=web.HomePage.as_view('home_page'))
    app.add_url_rule('/calories', view_func=web.CaloriesFormPage.as_view('form_page'))
    app.run()#debug=True)