from .models import Blog
import csv, datetime
import io

def handleCSV(csv_file):
    csv_text = csv_file.read().decode('utf-8')
    stringio = io.StringIO(csv_text)
    reader = csv.reader(stringio, delimiter='|', quotechar='\'')
    for row in reader:
        print(row)

def createRecords():
    for i in range(5):
        blog = Blog()
        blog.title = 'Hello'
        blog.entry = 'Hello world'
        blog.date_published = datetime.datetime.now()
        blog.save()
    print('Done creating records you nerd...')
