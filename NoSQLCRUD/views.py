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
client = MongoClient(connect_string, tlsCAFile=certifi.where())

# Define the database name
db = client.task_manager

collection = db.tasks


# find all tasks
def view_all_tasks(request):
    tasks = collection.find()
    context = {'tasks': tasks}
    return render(request, 'tasks.html', context)


def edit_task(request, task_id):
    _task = db.tasks.find_one()
    task = str(_task['task_id'])
    all_categories = db.categories.find()

    return render(request, 'edit_task.html',
                  {'task': task, 'categories': all_categories})
