# Made by Iyobo Eki for quick, stylish Django routes
from django.conf.urls import url

routerlist = []
# rest/joblocations/:id/
# ^rest/joblocations/(?P<id>\d+)/$

def route(urlstring, kwargs=None, name=None, prefix=''):
    def decorator(func):
        finalregex =urlstring
        # If it starts with ^, leave it alone
        if not urlstring.startswith("^"):
            blocks = urlstring.split("/")
            regex = "^"
            for block in blocks:
                # if this is a param, wrap it like a django param
                if block.__contains__(":"):
                    block = block.replace(":", "")
                    block = "(?P<"+block+">\d+)"

                if len(block)>0:
                    regex += block+"/"

            regex += "$"
            finalregex = regex
        # quickroute is intelligent and converts simple common-sense route declarations to django's raw regex version of it.
        routerlist.append(
            url(finalregex, func, kwargs, name or func.__name__, prefix),
        )
        return func
    return decorator


def initQuickRoutes(urlPatterns):
    urlPatterns.extend(routerlist)
    pass