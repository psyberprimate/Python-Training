import justpy as jp
from web_pages.default_layout import DefaultLayout
#from web_pages.page import Page
from web_pages import page

class About(page.Page):
    """Class for About webpage
    """    
    path = "/about"
    def serve(self):
        web_page = jp.QuasarPage(tailwind=True)
        layout = DefaultLayout(a=web_page)
        page_container = jp.QPageContainer(a=layout)
        main_div = jp.Div(a=page_container, classes="bg-gray-200 h-screen")
        jp.Div(a=main_div, text="This is the about page!", classes="text-4xl m-2")
        jp.Div(a=main_div, text="""
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