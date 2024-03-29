import datetime
import certifi
import pymongo
from pymongo import MongoClient
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from bson import ObjectId

from django. shortcuts import render
from . import forms

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
def get_tasks(request):
    _tasks = collection.find()
    context = {'tasks': _tasks}
    return render(request, 'tasks.html', context)

# add a new task


def add_task(request):
    all_categories = db.categories.find()
    return render(request, 'add_task.html',
                  {'categories': all_categories})

# insert a new task


def insert_task(request):
    if request.method == 'POST':
        tasks = collection
        new_task = {
            'task_name': request.POST.get('task_name', ''),
            'category_name': request.POST.get('category_name', ''),
            'task_description': request.POST.get('task_description', ''),
            'due_date': request.POST.get('due_date', ''),
            'is_urgent': request.POST.get('is_urgent', 'off'),
            'created_date': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        }
        tasks.insert_one(new_task)
        return HttpResponseRedirect(reverse('get_tasks'))


# edit a task
def edit_task(request, task_id):
    _task = collection.find_one({'_id': ObjectId(task_id)})
    all_categories = db.categories.find()
    context = {'task': _task, 'categories': all_categories}
    return render(request, 'edit_task.html', context)


# update a task
def update_task(request, task_id):
    if request.method == 'POST':
        tasks = collection
        tasks.update_one({'_id': ObjectId(task_id)},
                         {"$set": {
                             'task_name': request.POST['task_name'],
                             'category_name': request.POST['category_name'],
                             'task_description': request.POST['task_description'],
                             'due_date': request.POST['due_date'],
                             'is_urgent': request.POST.get('is_urgent', 'off'),
                             'updated_date': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                         }})

        return HttpResponseRedirect(reverse('get_tasks'))


# delete a task
def delete_task(request, task_id):
    tasks = collection
    tasks.delete_one({'_id': ObjectId(task_id)})
    return HttpResponseRedirect(reverse('get_tasks'))


# get all categories
def get_categories(request):
    _categories = db.categories.find()
    context = {'categories': _categories}
    return render(request, 'categories.html', context)


# edit a category
def edit_category(request, category_id):
    _category = db.categories.find_one({'_id': ObjectId(category_id)})
    context = {'category': _category}
    return render(request, 'edit_category.html', context)


# update a category
def update_category(request, category_id):
    if request.method == 'POST':
        form = forms.InsertCategoryForm(request.POST)
        if form.is_valid():
            categories = db.categories
            categories.replace_one({'_id': ObjectId(category_id)},
                                   {
                'category_name': request.POST['category_name'],
                'category_description': request.POST['category_description'],
            })
            return HttpResponseRedirect(reverse('get_categories'))
        else:
            print('🚫 Error: Form Invalid, ID: ' + category_id)
            form = forms.InsertCategoryForm()
            return render(request, 'edit_category.html', {'form': form})


# insert a new category
def insert_category(request):
    if request.method == 'POST':
        form = forms.InsertCategoryForm(request.POST)
        if form.is_valid():
            categories = db.categories
            new_category = {
                'category_name': request.POST.get('category_name', ''),
                'category_description': request.POST.get('category_description', ''),
            }
            categories.insert_one(new_category)
            return HttpResponseRedirect(reverse('get_categories'))
        else:
            print('🚫 Error: Form Invalid')
            form = forms.InsertCategoryForm()
            return render(request, 'new_category.html', {'form': form})


# add a new category
def new_category(request):
    return render(request, 'new_category.html')


# delete a category
def delete_category(request, category_id):
    categories = db.categories
    categories.delete_one({'_id': ObjectId(category_id)})
    return HttpResponseRedirect(reverse('get_categories'))
