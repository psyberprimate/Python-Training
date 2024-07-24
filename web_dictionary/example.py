import justpy as jp

# Suppress the specific warning about the missing config file

 
# class Page(jp.WebPage):
   
#     def __init__(self):
#         self.page = jp.WebPage()
        
#     def home(self):
#         jp.Div(a=self.page, text="Hello")
#         jp.Div(a=self.page, text="Greetings!")
#         return self.page

@jp.SetRoute("/home")
def home():
    web_page = jp.QuasarPage(tailwind=True)#jp.WebPage()
    div_page = jp.Div(a=web_page, classes="bg-gray-200 h-screen")
    #divided page elements
    div_page1 = jp.Div(a=div_page, classes="grid grid-cols-3 gap-5 p-5")
    input_val1 = jp.Input(a=div_page1, placeholder="Enter first value",
             classes="form-input")
    input_val2 = jp.Input(a=div_page1, placeholder="Enter holder value",
             classes="form-input")
    div_output1 = jp.Div(a=div_page1, text="Sum",
           classes="text-blue-500 m-2 py-2 px-2")
    jp.Div(a=div_page1, text="Result 2",
           classes="text-blue-500 m-2 py-2 px-2")
    jp.Div(a=div_page1, text="Result 3",
           classes="text-blue-500 m-2 py-2 px-2")
    #
    div_page2 = jp.Div(a=div_page, classes="grid grid-cols-3 gap-5")
    #
    jp.Button(a=div_page2, text="Calculate", click = sum,
              in1=input_val1, in2=input_val2,d=div_output1,
              classes="border border-blue-500 m-2 py-2 px-2 "
              "rounded text-blue-500 hover:bg-red-500 "
              "hober:text-white-500")
    jp.Div(a=div_page2, text="Press to calculate",
           mouseenter=mouse_enter, mouseleave=mouse_leave,
           classes = "hover:bg-red-500")
    return web_page

@jp.SetRoute("/about")
def about():
    web_page = jp.WebPage()
    jp.Div(a=web_page, text="About page")
    jp.Div(a=web_page, text="About Again")
    return web_page

def sum(widget :object, msg : dict):
    widget.d.text = float(widget.in1.value) + float(widget.in2.value)
    
    
def mouse_enter(widget : object, msg : dict):
    widget.text = "Mouse here"

def mouse_leave(widget : object, msg : dict):
    widget.text = "Mouse not here"

if __name__ == '__main__':
    #jp.Route("/", home)
    jp.justpy()