import justpy as jp
import dictionary_definitions as definitions

class About():
    """Class for About webpage
    """    
    path = "/about"
    def serve(self):
        web_page = jp.QuasarPage(tailwind=True)
        web_div = jp.Div(a=web_page, classes="bg-gray-200 h-screen")
        jp.Div(a=web_div, text="This is the about page!", classes="text-4xl m-2")
        jp.Div(a=web_div, text="""
        Sed ut perspiciatis unde omnis iste natus error sit voluptatem \
            accusantium doloremque laudantium, totam rem aperiam, eaque \
            ipsa quae ab illo inventore veritatis et quasi architecto \
            beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia \
            voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni \
            dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, \
            qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia \
            non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam \
            quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam \
            corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? \
            Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil \
            molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
               """,
               classes="text-lg")
        
        return web_page
     
   
class Home():
    """Class for Home webpage
    """
    path = "/"
    def serve(self):
        web_page = jp.QuasarPage(tailwind=True)
        web_div = jp.Div(a=web_page, classes="bg-gray-200 h-screen")
        jp.Div(a=web_div, text="This is the home page!", classes="text-4xl m-2")
        jp.Div(a=web_div, text="""
        Sed ut perspiciatis unde omnis iste natus error sit voluptatem \
            accusantium doloremque laudantium, totam rem aperiam, eaque \
            ipsa quae ab illo inventore veritatis et quasi architecto \
            beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia \
            voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni \
            dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, \
            qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia \
            non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam \
            quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam \
            corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? \
            Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil \
            molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
               """,
               classes="text-lg")
        
        return web_page
    
    
class Dictionary():
    """ Class for dictionary webpage than contains the dictionary definitions
    """
    path = "/dictionary"
    
    @classmethod
    def serve(cls, requirement):
        web_page = jp.QuasarPage(tailwind=True)
        
        web_div = jp.Div(a=web_page, classes="bg-gray-100 h-screen")
        jp.Div(a=web_div, text="*****Instant english dictionary*****",
               classes="text-4xl m-2")
        jp.Div(a=web_div, text="Get a definition for english words as you type.",
               classes="text-lg")
        
        input_div = jp.Div(a=web_div, classes="grid grid-cols-2")
        input_word = jp.Input(a=input_div, placeholder="Type a word here...",
                classes="m-2 bg-gray-500 border-2 border-gray-500 rounded w-64 \
                    focus:bg-white focus:border-purple-500 py-2 px-4")
        
        
        output_div = jp.Div(a=web_div, classes="grid grid-cols-2")
        jp.Button(a=input_div, text="Search for a definition", click=cls.get_definition,
                  input_word=input_word, outputdiv=output_div,
                  classes="border-2 text-gray-500")
        jp.Div(a=web_div, classes="m-2 p-2 text-lg border-2 h-40")
        
        return web_page
    
    @staticmethod
    def get_definition(widget : object, msg : dict):
        word_definitions = definitions.Definition(term=widget.input_word.value).get()
        word_definitions = ["{}: {}".format(index+1, entry) for index, entry in enumerate(word_definitions)]
        widget.outputdiv.text = "".join(word_definitions)