from pprint import pprint
import datetime
import pymongo

from models import posts


def get_recent_posts():
    return [p for p in posts.find().sort('updated_time', pymongo.DESCENDING).limit(50)]


def posts_from_date(date):
    return [p for p in posts.find({'updated_time': })]

def order_by_popularity():
    return [p for p in posts.find().sort('shares', pymongo.DESCENDING)]
# pprint(get_recent_posts())
pprint(posts_from_date(datetime.datetime.now().date()))
# pprint(order_by_popularity())

