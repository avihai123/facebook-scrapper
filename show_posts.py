import datetime
from pprint import pprint

import pymongo

from models import posts, pages


def get_recent_posts(limit=50):
    return [p for p in posts.find().sort('updated_time', pymongo.DESCENDING).limit(50)]
    # return posts.find().sort('updated_time', pymongo.DESCENDING).limit(limit)


def posts_from_date(date):
    d_end = date + datetime.timedelta(days=1)
    # return [p for p in posts.find({'updated_time': {"$gt": date, "$lt": d_end}}).sort('shares', pymongo.DESCENDING)]
    return posts.find({'updated_time': {"$gt": date, "$lt": d_end}}).sort('shares', pymongo.DESCENDING)


def get_posts_ordered_by_popularity(the_page_id):
    # return [p for p in posts.find().sort('shares', pymongo.DESCENDING)]
    return posts.find({'page_id': the_page_id}).sort('shares', pymongo.DESCENDING)


def get_posts_ordered_by_score(the_page_id, limit=50):
    return posts.find({'page_id': the_page_id}).sort('shares', pymongo.DESCENDING).limit(limit)


def get_best_posts_per_page(limit=3):
    pages_with_best_posts = dict()
    for page in pages.find():
        pages_with_best_posts[page['id']] = get_posts_ordered_by_score(page['id'], limit)
    return pages_with_best_posts

def search_text_in_db(s):
    """
    search text in db and return matched documents(posts)


    :return: return list of posts that match the text query.
    """
    return [p for p in posts.find({'$text': {'$search': s}})]

# pprint(get_best_posts())
# pprint(get_recent_posts())
# pprint(posts_from_date(datetime.datetime(2016, 5, 22)))
# pprint(get_posts_ordered_by_popularity(5550296508))
