import justpy as jp

class Documentation():
    """Class for Documentation webpage
    """    
    path = "/"
    def serve(self):
        web_page = jp.WebPage()
        main_div = jp.Div(a=web_page, classes="bg-gray-200 h-screen")
        jp.Div(a=main_div, text="English Dictionary Search API", classes="text-4xl m-2")
        jp.Div(a=main_div, text="Get definitions of words by search",
               classes="text-lg")
        jp.Hr(a=main_div)
        jp.Div(a=main_div, text="Example path:")
        jp.Div(a=main_div, text="www.example.com/api?=water")
        jp.Hr(a=main_div)
        jp.Div(a=main_div, text="Example search result:")
        jp.Div(a=main_div, text="""
               {"search_word": "water", "definition": ["Significant accumulation of water, \
                covering the Earth or another planet.", "Common liquid (H\u2082O) which forms \
                rain, rivers, the sea, etc., and which makes up a large part of the bodies of \
                organisms.", "To pour water onto the soil surrounding plants.", "Of the eyes: \
                To secrete tears because of an irritation caused by wind, smoke etc."]}
                """)
        return web_page