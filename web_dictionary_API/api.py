import justpy as jp
import dictionary_definitions as definitions
import json
import docs as docs

class Api():
    """ Get requests from /api?w=search_word
    """    
    @classmethod
    def serve(cls, req):
        web_page = jp.WebPage()
        search_word = req.query_params.get('w')
        word_definitions = definitions.Definition(term=search_word).get()
        response = {
            "search_word":search_word,
            "definition":word_definitions
        }
        web_page.html = json.dumps(response)
        return web_page

if __name__ == "__main__": 
    jp.Route("/api", Api.serve)
    jp.Route("/", docs.Documentation.serve)
    jp.justpy()