from bottle import route, run, template
from show_pages import get_page_list, get_page_name
from show_posts import *

# TODO make search text work for posts, i mad i function search_text_in_db. it need to redirect to posts pages. if you want i can do for pages too.
# we need to send search query with get like @route('search/')
# TODO rearrange project
# TODO add comments and rename functions and variables.
# TODO for each post put small picture(in post['picture'])
# TODO convert id to link to post.
# TODO each post now have link and type of link, (video,picture,link) maybe we can use it.
# TODO show page cover picture(in page['picture'] for all pages
# TODO posts got this fields now, we to use them (shares, likes, comments)
@route('/')
def index():
    return template('templates/pages', title='Home', page_list=get_page_list(), post_dict=get_best_posts_per_page())


@route('/<page_id>/')
def show_posts(page_id):
    return template('templates/posts', title='{} Posts'.format(get_page_name(page_id)), page_list=get_page_list(), post_list=get_posts_ordered_by_popularity(page_id), page_id=page_id)
                    # post_list=get_posts_ordered_by_popularity(page_id), page_id=page_id)


# @route('/<page_name>/')
# def page_name_posts(page_name):
#     return template('templates/posts', title=page_name, page_list=get_page_list(), post_list=get_posts_ordered_by_popularity('40796308305'), page_id='40796308305')
#                     # post_list=get_posts_ordered_by_popularity(page_id), page_id=page_id)


# TODO fix latest template, broken
@route('/latest/')
def show_recent_posts():
    return template('templates/posts', title='Recent Posts', page_list=get_page_list(), post_list=get_recent_posts(), page_id='needtofix')


@route('/<year:int>/<month:int>/<day:int>/')
def show_posts_from_date(year, month, day):
    date = datetime.datetime(year, month, day)
    return template('templates/posts', title="Posts from {}.{}.{}".format(day, month, year), post_list=posts_from_date(date))


def run_server(interface='127.0.0.1', port=8000, debug=False, reloader=False):
    run(host=interface, port=port, reloader=reloader, debug=debug)


if __name__ == '__main__':
    run_server()
