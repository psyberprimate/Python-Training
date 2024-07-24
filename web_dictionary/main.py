import inspect
import justpy as jp
from web_pages.page import Page
from web_pages import about, dictionary, home 


if __name__ == "__main__":
    
    # Not working, the issues seems to that the path via global is not properly set
    # only web_pages.page.Page is found as an object, to be fixed.
    # imports = list(globals().values())
    # for obj in imports:
    #     # print(obj)
    #     if inspect.isclass(obj):
    #         # print()
    #         # print("Class object")
    #         # print(obj)
    #         if issubclass(obj, Page) and obj is not Page:
    #             jp.Route(obj.path, obj.serve)
    #             # print("Route established")
    
    jp.Route(home.Home.path, home.Home.serve)
    jp.Route(about.About.path, about.About.serve)
    jp.Route(dictionary.Dictionary.path, dictionary.Dictionary.serve)
    jp.justpy()