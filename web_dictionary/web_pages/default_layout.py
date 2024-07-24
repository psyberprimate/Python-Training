import justpy as jp

class DefaultLayout(jp.QLayout):
    
    
    def __init__(self, view="hHh lpR fFf", **kwargs):
        #init parent class
        super().__init__(view=view, **kwargs)
        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=self, show_if_above=True, v_model="left",
                            bordered=True)
        #Side bar scroller
        page_scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=page_scroller)
        settings_classes = "p-2 m-2 text-lg text-orange-500 hover:text-orange-800"
        jp.A(a=qlist, text="Home", href="/", classes=settings_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=settings_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=settings_classes)
        jp.Br(a=qlist)
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=self.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant English Dictionary")
        
        
    @staticmethod
    def move_drawer(widget, msg):
        widget.drawer.value = not widget.drawer.value