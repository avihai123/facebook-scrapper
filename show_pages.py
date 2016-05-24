from models import pages


def get_page_list():
    return [p for p in pages.find()]


def print_page_list():
    print("ID - {id}, name - {name}, fans - {fan_count}".format(**p))
