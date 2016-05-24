#!/usr/bin/env python3
import argparse
from add_page import add_page, remove_page
from get_or_update_all_posts import update_posts_per_page
from server import run_server
from show_pages import print_page_list


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='choose blabla')

# create the parser for the "add" command
parser_add_page = subparsers.add_parser('add', help="add a page")
parser_add_page.add_argument('page', help="facebook url/name/ID")
parser_add_page.set_defaults(func=lambda args: add_page(args.page))

# create the parser for the "list" command
parser_list_page = subparsers.add_parser('list', help="list pages (for each page: name, fan count, ID)")
parser_list_page.set_defaults(func=lambda args: print_page_list())

# create the parser for the "update" command
parser_update = subparsers.add_parser('update', help="update posts from facebook/twitter")
parser_update.add_argument('--posts', type=int, default=100, help="posts limits")
parser_update.set_defaults(func=lambda args: update_posts_per_page(args.posts))

# create the parser for the "serve" command
parser_serve = subparsers.add_parser('serve', help="start a web server to access collected data")
parser_serve.add_argument('--port', type=int, default=8000, help="server port")
parser_serve.add_argument('--interface', default='127.0.0.1', help="server ip")
parser_serve.add_argument('--debug', default=False, help="enable debugger")
parser_serve.add_argument('--reloader', default=False, help="enable auto reload")
parser_serve.set_defaults(func=lambda args: run_server(args.interface, args.port, args.debug, args.reloader))


#create the parser for the "remove" command
parser_remove_page = subparsers.add_parser('remove')
parser_remove_page.add_argument('page_id', help="page id")
parser_remove_page.set_defaults(func=lambda args: remove_page(args.page_id))


# # parse the args and call whatever function was selected
args = parser.parse_args()
args.func(args)
