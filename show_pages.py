from models import pages
for p in pages.find():
    print("{id}, name - {name}, about - {about}, fans - {fan_count}".format(**p))
