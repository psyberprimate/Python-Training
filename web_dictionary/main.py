import web_page as web
import justpy as jp


if __name__ == "__main__":
    jp.Route(web.Home.path, web.Home.serve)
    jp.Route(web.About.path, web.About.serve)
    jp.Route(web.Dictionary.path, web.Dictionary.serve)
    jp.justpy()