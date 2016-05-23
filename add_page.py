from models import upsert, graph, pages
import facebook

ERROR_MSG = 'Not a page'
SUCCESS_ADD_MSG = "Output: OK, added id #{id} with {fan_count} fans."


def add_page(arg):
    if '/' in arg:
        fb_url = arg.split('/')[-1]
    else:
        fb_url = arg
    try:
        new_page = graph.get_object('/{}/?fields=about,fan_count,name'.format(fb_url))
    except facebook.GraphAPIError:
        print('Not a page')
        exit()
    upsert(pages, new_page)
    print(SUCCESS_ADD_MSG.format(**new_page))
