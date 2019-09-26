from .models import Blog
import datetime

def createRecords():
    for i in range(5):
        blog = Blog()
        blog.title = 'Hello'
        blog.entry = 'Hello world'
        blog.date_published = datetime.datetime.now()
        blog.save()
    print('Done creating records you nerd...')
