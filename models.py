import facebook
import pymongo

API_KEY = '1598480263776324|IdYDQgU-bNut44sZi564EZGkTHk'
graph = facebook.GraphAPI(access_token=API_KEY, version='2.5')

client = pymongo.MongoClient()
db = client.get_database('facebook_scrapper')

pages = db.get_collection('pages')
pages.create_index('id', unique=True)

posts = db.get_collection('posts')
posts.create_index('id', unique=True)


def upsert(collection, item):
    return collection.update({'id': item['id']}, item, upsert=True)


