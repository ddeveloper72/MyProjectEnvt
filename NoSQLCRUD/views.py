import certifi
import pymongo
from pymongo import MongoClient
from django.template import loader
from django.shortcuts import render

# Import environmental variables
from MyNoSQLProj.settings import environ
env = environ.Env()


# Create your views here.

# Get env secrets escaped according to RFC 3986
#  Connection to MongoDB
connect_string = env('MONGO_URI')


# Configure the connection string with certifi
client = pymongo.MongoClient(connect_string, tlsCAFile=certifi.where())

# Define the database name
db = client['task_manager']


# find all tasks
def view_all_tasks(request):
    tasks = db.tasks.find()

    return render(request, 'tasks.html', {'tasks': tasks})
