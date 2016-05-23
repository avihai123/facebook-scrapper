import facebook
import datetime
import pymongo



def show_pages():
    # for p in pages.find():
    # print("{id}, name - {name}, about - {about}, fans - {fan_count}".format(**p))
    return [p for p in pages.find()]


@route('/')
def index():
    return template('base', pages=show_pages())


# @route('/<page>/<>')


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
