import facebook
import pymongo
import sys

API_KEY = '1598480263776324|IdYDQgU-bNut44sZi564EZGkTHk'
graph = facebook.GraphAPI(access_token=API_KEY, version='2.5')

client = pymongo.MongoClient()
db = client.get_database('facebook_scrapper')

pages = db.get_collection('pages')
pages.create_index('id', unique=True)

posts = db.get_collection('posts')
posts.create_index('id', unique=True)
posts.create_index([('message', 'text'), ('name', 'text')])


def upsert(collection, item):
    return collection.update_one(
        {'id': item['id']},
        {'$set': item},
        upsert=True
    )

# TODO add more advanced/complex querys and aggregators.
