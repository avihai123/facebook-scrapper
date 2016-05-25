from models import upsert, graph, pages, posts
import facebook
import sys

ERROR_MSG = 'Not a page'
SUCCESS_ADD_MSG = "Output: OK, added id #{id} with {fan_count} fans."
FIELDS = ('about', 'fan_count', 'name', 'cover')
FIELDS_FORMAT = '?fields={},{},{},{}'.format(FIELDS)
REQUEST_FORMAT = '/{}/{}'

# TODO save all fields in tuple
# TODO let other function to select fields to request
def add_page(arg):
    """
    add specific information from facebook page to DB

    connecting facebook api and request selected fields.
    :param arg: page name, id or full url
    """
    if '/' in arg:
        fb_url = arg.split('/')[-1]
    else:
        fb_url = arg
    try:
        new_page = graph.get_object(REQUEST_FORMAT.format(fb_url, FIELDS_FORMAT))
    except facebook.GraphAPIError:
        print('Not a page')
        exit()

    # relpace cover with cover link
    new_page['cover'] = new_page['cover']['source']

    # add field values to database
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


