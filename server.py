from bottle import route, run, template
from show_pages import get_page_list
from show_posts import *


@route('/')
def index():
    return template('templates/pages', title='Facebook Pages', page_list=get_page_list(), post_dict=get_best_posts_per_page())


@route('/<page_id>/')
def show_posts(page_id):
    return template('templates/posts', title='Posts', post_list=get_posts_ordered_by_popularity(page_id))


@route('/latest/')
def show_recent_posts():
    return template('templates/posts', title='Recent Posts', post_list=get_recent_posts())


@route('/<year:int>/<month:int>/<day:int>/')
def show_posts_from_date(year, month, day):
    date = datetime.datetime(year, month, day)
    return template('templates/posts', title="Posts from {}.{}.{}".format(day, month, year),
                    post_list=posts_from_date(date))


def run_server(ip='127.0.0.1', port=8000):
    run(host=ip, port=port, reloader=True, debug=True)

if __name__ == '__main__':
    run_server()
