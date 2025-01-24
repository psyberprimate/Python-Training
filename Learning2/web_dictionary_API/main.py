import justpy as jp
import docs as docs
import api as api


jp.Route("/api", api.Api.serve)
jp.Route("/", docs.Documentation.serve)
jp.justpy()                                    