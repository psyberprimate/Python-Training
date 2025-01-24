import justpy as jp
import dictionary_definitions as definitions
from web_pages.default_layout import DefaultLayout
from web_pages.page import Page
import requests

class Dictionary(Page):
    """ Class for dictionary webpage than contains the dictionary definitions
    """
    path = "/dictionary"
    
    @classmethod
    
    def serve(cls, requirement):
        web_page = jp.QuasarPage(tailwind=True)
        
        #page layout
        layout = DefaultLayout(a=web_page)
        page_container = jp.QPageContainer(a=layout)
        
        main_div = jp.Div(a=page_container, classes="bg-gray-100 h-screen")
        jp.Div(a=main_div, text="Instant english dictionary",
               classes="text-4xl m-2")
        jp.Div(a=main_div, text="Get a definition for english words as you type.",
               classes="text-lg")
        
        input_div = jp.Div(a=main_div, classes="grid grid-cols-2")
        
        output_div = jp.Div(a=main_div, classes="m-2 p-2 text-lg borders-2 h-40")
        
        input_field = jp.Input(a=input_div, placeholder="Type a word here...",
                               outputdiv=output_div,
                               classes="m-2 bg-gray-500 border-2 border-gray-500 rounded w-64 \
                                focus:bg-white focus:border-purple-500 py-2 px-4")
        input_field.on('input', cls.get_definition)
        
        # For button
        # jp.Button(a=input_div, text="Search for a definition", click=cls.get_definition,
        #           input_word=input_field, outputdiv=output_div,
        #           classes="border-2 text-gray-500")
        
        jp.Div(a=main_div, classes="m-2 p-2 text-lg border-2 h-40")
        
        return web_page
    
    @staticmethod
    def get_definition(widget : object, msg : dict):
        """Gets the definition if there is one for the provided word
        """
        #using the api - needs to have web_dictonary api running to work
        req = requests.get("http://127.0.0.1:8000/api?w={}".format(widget.value))
        data = req.json()
        widget.outputdiv.text = " | ".join(data['definition'])
        #using defitions class directly
        # word_definitions = definitions.Definition(term=widget.value).get()#term=widget.input_field.value).get()
        # word_definitions = ["#{}: {}".format(index+1, entry) for index, entry in enumerate(word_definitions)]
        # widget.outputdiv.text = " | ".join(word_definitions)