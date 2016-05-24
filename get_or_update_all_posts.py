from models import pages, posts, graph, upsert
import dateutil.parser


def update_posts_per_page():
    for page in pages.find():
        print('Updating page "{}"'.format(page['name']))
        page_posts = graph.get_object('/{}/posts/?fields=shares, message,updated_time&limit=100'.format(page['id']))
        page_posts = page_posts['data']
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
