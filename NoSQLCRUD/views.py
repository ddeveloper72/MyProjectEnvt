import certifi
import pymongo
from pymongo import MongoClient
import urllib.parse
from django.template import loader
from django.http import HttpResponse

# Import environmental variables
from MyNoSQLProj.settings import environ
env = environ.Env()


# Create your views here.

# Get env secrets escaped according to RFC 3986
user = urllib.parse.quote_plus(env('USER'))
password = urllib.parse.quote_plus(env('PASSWORD'))
mongo_dbname = urllib.parse.quote_plus(env('MONGO_DBNAME'))

# Build the connection string
connect_string = 'mongodb+srv://%s:%s@%s.8i0tx.mongodb.net/?retryWrites=true&w=majority' % (
    user, password, mongo_dbname)

# Configure the connection string with certifi
client = pymongo.MongoClient(connect_string, tlsCAFile=certifi.where())

# Define the database name
db = client['task_manager']


# find all tasks
def view_all_tasks(request):
    template = loader.get_template('tasks.html')
    context = {'tasks': db.tasks.find()}
    return HttpResponse(template.render(context, request))
