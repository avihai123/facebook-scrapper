from bottle import route, run, template
from show_pages import get_page_list
from show_posts import *


@route('/')
def index():
    return template('templates/pages', title='Facebook Pages', page_list=get_page_list(), post_dict=get_best_posts())


@route('/<page_id>/')
def show_posts(page_id):
    return template('templates/posts', title='Posts', page_list=get_page_list(), post_list=get_posts_ordered_by_popularity(page_id), page_id=page_id)


@route('/latest/')
def show_recent_posts():
    return template('templates/posts', title='Recent Posts', page_list=get_page_list(), post_list=get_recent_posts())


@route('/<year:int>/<month:int>/<day:int>/')
def show_posts_from_date(year, month, day):
    date = datetime.datetime(year, month, day)
    return template('templates/posts', title="Posts from {}.{}.{}".format(day, month, year),
                    post_list=posts_from_date(date))


def run_server(interface='127.0.0.1', port=8000):
    run(host=interface, port=port, reloader=True, debug=True)


if __name__ == '__main__':
    run_server()
