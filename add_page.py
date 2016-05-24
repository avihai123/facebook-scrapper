from models import upsert, graph, pages, posts
import facebook
import sys

ERROR_MSG = 'Not a page'
SUCCESS_ADD_MSG = "Output: OK, added id #{id} with {fan_count} fans."


def add_page(arg):
    #print(page)
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

def remove_page(page_id):
    pages.remove({'id': page_id})
    posts.remove({'page_id': page_id})
    print("Removed")

if __name__ == '__main__':
    if sys.argv[1] == 'add':
        add_page(sys.argv[2])
    if sys.argv[1] == 'remove':
        add_page(sys.argv[2])


