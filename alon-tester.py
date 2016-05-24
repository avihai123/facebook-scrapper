import argparse

from add_page import add_page
from get_or_update_all_posts import update_posts_per_page
add_page('facebook')
update_posts_per_page()

def add_fb_page(page_name=''):
    add_page(page_name)

def update_all_posts():
    update_posts_per_page()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Facebook Agg User')
#     parser.add_argument('add_fb_page', type=str, help='Add Facebook Page (page_name)')
#     parser.add_argument('update_all_posts', type=str, help='updates posts')
#
#     args = parser.parse_args()
#     print(parser.parse_args())
#     print(args)
#     # main(**args)
