from concurrent import futures

from models import pages, posts, graph, upsert
import dateutil.parser
import requests

REQUEST_POSTS_FORMAT = '/{}/posts/?fields=shares, type,picture,message,likes.limit(1).summary(True),comments.limit(1).summary(true), updated_time&limit={}'
POSTS_LIMIT_REQUEST = 50


def async_posts_update(page, post_limit):
    print('Updating page "{}"'.format(page['name']))

    page_data = []
    page_posts = graph.get_object(REQUEST_POSTS_FORMAT.format(page['id'], POSTS_LIMIT_REQUEST))
    page_data.extend(page_posts['data'])
    for i in range(post_limit // POSTS_LIMIT_REQUEST):

        # no more posts to request
        if 'paging' not in page_posts.keys():
            break
        if 'next' not in page_posts['paging']:
            break

        page_posts = requests.get(page_posts['paging']['next']).json()
        page_data.extend(page_posts['data'])
        # updating posts
    result_list = []
    for i, post in enumerate(page_data):
        if i == post_limit:
            break

        # convert time to datetime, add reference to page_id
        post['updated_time'] = dateutil.parser.parse(post['updated_time'])
        post['page_id'] = page['id']

        # convert shares, likes, comments to total shares
        # TODO use difault dict here and remove checks from html
        if 'shares' in post.keys():
            post['shares'] = int(post['shares']['count'])
        if 'likes' in post.keys():
            post['likes'] = int(post['likes']['summary']['total_count'])
        if 'comments' in post.keys():
            posts['comments'] = int(post['comments']['summary']['total_count'])

        # add posts and print DB status
        result = upsert(posts, post)
        result_list.append(result)

    # counting changes in db for each page
    modified_posts = sum(r['nModified'] for r in result_list)
    inserted_posts = sum(not r['updatedExisting'] for r in result_list)
    print("Inserted {} posts, update {} posts.".format(inserted_posts, modified_posts))


# TODO remove fields from code, put the in dict or list.
# TODO add twitter api

def update_posts_per_page(post_limit=100):
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        for page in pages.find():
            executor.submit(async_posts_update, page, post_limit)

    print("Done")


if __name__ == '__main__':
    update_posts_per_page()
