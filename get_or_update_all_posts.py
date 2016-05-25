from concurrent import futures

from models import pages, posts, graph, upsert
import dateutil.parser
import requests

FIELDS_TO_UPDATE = 'shares,type,name,full_picture,picture,message,likes.limit(1).summary(True),comments.limit(1).summary(true),updated_time&limit='
REQUEST_POSTS_FORMAT = '/{}/posts/?fields={}{}'
POSTS_LIMIT_REQUEST = 40


def async_posts_update(page, post_limit):
    print('Updating page "{}"'.format(page['name']))

    page_data = []
    page_posts = graph.get_object(REQUEST_POSTS_FORMAT.format(page['id'], FIELDS_TO_UPDATE, POSTS_LIMIT_REQUEST))
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
    counter = 0
    for i, post in enumerate(page_data):
        counter += 1
        if i == post_limit:
            break

        # convert time to datetime, add reference to page_id
        post['updated_time'] = dateutil.parser.parse(post['updated_time'])
        post['page_id'] = page['id']

        # convert shares, likes, comments to total shares
        if 'shares' in post.keys():
            post['shares'] = int(post['shares']['count'])
        else:
            post['shares'] = 0
        if 'likes' in post.keys():
            post['likes'] = int(post['likes']['summary']['total_count'])
        else:
            post['likes'] = 0
        post['comments'] = int(post['comments']['summary']['total_count'])
        # add posts and print DB status
        result = upsert(posts, post)
        # print(result.modified_count)
        result_list.append(result)

    # counting changes in db for each page
    modified_posts = sum(r.modified_count for r in result_list)
    inserted_posts = post_limit - modified_posts
    print("Inserted {} posts, update {} posts.".format(inserted_posts, modified_posts))


# TODO add twitter api

def update_posts_per_page(post_limit=300):
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        for page in pages.find():
            executor.submit(async_posts_update, page, post_limit)

    print("Done")


if __name__ == '__main__':
    update_posts_per_page()
