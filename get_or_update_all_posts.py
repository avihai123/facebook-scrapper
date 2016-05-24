from models import pages, posts, graph, upsert
import dateutil.parser

GRAPH_FACEBOOK_POSTS_API = '/{}/posts/?fields=shares, message,updated_time&limit={}'
def update_posts_per_pages(pages_list, post_limit=100):
    for page in pages_list:
        print('Updating page "{}"'.format(page['name']))
        page_posts = graph.get_object(GRAPH_FACEBOOK_POSTS_API.format(page['id'], post_limit))['data']
        #page_posts = page_posts['data']

        # updating posts
        result_list = []
        for post in page_posts:
            # convert time to datetime, add reference to page_id
            post['updated_time'] = dateutil.parser.parse(post['updated_time'])
            post['page_id'] = page['id']
            if 'shares' in post.keys():
                post['shares'] = int(post['shares']['count'])
            # add posts and print DB status
            result = upsert(posts, post)
            result_list.append(result)

        # counting changes in db for each page
        modified_posts = sum(r['nModified'] for r in result_list)
        inserted_posts = sum(not r['updatedExisting'] for r in result_list)
        print("Inserted {} posts, update {} posts.".format(inserted_posts, modified_posts))
    print("Done")


if __name__ == '__main__':
    update_posts_per_page()
