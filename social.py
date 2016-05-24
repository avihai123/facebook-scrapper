import argparse  # create the top-level parser
from add_page import add_page
from get_or_update_all_posts import update_posts_per_page
from server import run_server
from show_pages import print_page_list

def foo(args):
    print(args.x * args.y)


def bar(args):
    print('((%s))' % args.z)  # create the parser for the "foo" command


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# create the parser for the "add" command
parser_add_page = subparsers.add_parser('add', help="add a page")
parser_add_page.add_argument('page', help="facebook url/name/ID")
parser_add_page.set_defaults(func=add_page)

# create the parser for the "list" command
parser_list_page = subparsers.add_parser('list', help="list pages (for each page: name, fan count, ID)")
parser_list_page.set_defaults(func=print_page_list)

# create the parser for the "update" command
parser_update = subparsers.add_parser('update', help="update posts from facebook/twitter")
parser_update.add_argument('page', help="name or id of pages for update")
parser_update.add_argument('--posts', type=int, default=100, help="posts limits")
parser_update.set_defaults(func=update_posts_per_page)

# create the parser for the "serve" command
parser_serve = subparsers.add_parser('serve', help="start a web server to access collected data")
parser_serve.add_argument('--port', type=int, default=8000, help="server port")
parser_serve.add_argument('--interface', default='127.0.0.1', help="server ip")
parser_serve.set_defaults(func=run_server)


# create the parser for the "remove" command
# parser_remove_page = subparsers.add_parser('remove a page')
# parser_remove_page.add_argument('link', help="facebook url/name/ID")
# parser_remove_page.set_defaults(func=remove_page)

# # parse the args and call whatever function was selected
# args = parser.parse_args()
# args.func(args)
#
# # parse the args and call whatever function was selected
args = parser.parse_args()
args.func(args)
