import datetime
from pprint import pprint

import pymongo
from bson import SON

from models import posts, pages


def get_recent_posts(limit=50):
    return posts.find().sort('updated_time', pymongo.DESCENDING).limit(limit)


def posts_from_date(date):
    d_end = date + datetime.timedelta(days=1)
    return posts.find({'updated_time': {"$gt": date, "$lt": d_end}}).sort('shares', pymongo.DESCENDING)


def get_posts_ordered_by_popularity(the_page_id):
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
    return posts.find({'$text': {'$search': s}})

def aggregate_post_types():
    """
    counting the types of posts.


    :return: list of dicts each one contain type name and counter
    """
    pipeline = [
             {"$group": {"_id": "$type", "count": {"$sum": 1}}},
             {"$sort": SON([("count", -1), ("_id", -1)])}
            ]
    return posts.aggregate(pipeline)

def page_statictics():



# pprint(get_best_posts())
#pprint(get_recent_posts())
#pprint(aggregate_post_types())
# pprint(posts_from_date(datetime.datetime(2016, 5, 22)))
# pprint(get_posts_ordered_by_popularity(5550296508))
