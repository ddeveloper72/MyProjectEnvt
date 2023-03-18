# My NoSQL Project

## Using Django==4.1.7 with MongoB - [Live Site](https://mongo-django-crud.herokuapp.com/)

[![Build Status](https://app.travis-ci.com/ddeveloper72/MyProjectEnvt.svg?branch=master)](https://app.travis-ci.com/ddeveloper72/MyProjectEnvt)

This project is about building Django CRUD application with MongoDB. I already have a flask based task manager and in this project I have re-imaged the original Mini-Walk Through Project as a Django application instead.

Off the bat, I had trouble connecting the flask project to mongoDB. I discovered the same problem with this Django application. Pymongo relies on the operating system’s root certificates. I was unable to connect my application to mongoDB Atlas due to a `SSL: CERTIFICATE_VERIFY_FAILED` error. Through a process of debugging the error logs and referencing stack overflow I eventually came to the MongoDB Developer Community guides and read the troubleshooting article 👉[here](https://www.mongodb.com/community/forums/t/serverselectiontimeouterror-ssl-certificate-verify-failed-trying-to-understand-the-origin-of-the-problem/115288).

This was how the connection string was in Flask:

```python
# To run locally, use app.config = os.getenv('MONGO_URI', 'mongodb://<username>:<password>@ds155352.mlab.com:55352/task_manager')
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
```

The modification for use in Django required that the connection string had to include an update to work with out of date OpenSSL root certificate on the host system using `tlsCAFile`.

## Setup the Django application

Before building this application, list out the things that it is going to need to need so we can then setup the folders as well as the app and then its dependencies as we need them.

1. need a folder to develop the project in
2. a name to call the main project application
3. a name to call the application

The setup used in this project:

1. the development folder is called `Django_ToDo`
2. the project is called `MyNoSQLProj`
3. the app is called `NoSQLCRUD`

First thing first, create a folder in a file directory where you like to work on your development projects and then change directory (cd) into that folder.

### Setting up the virtual environment

Next setup is to setup a python virtual environment in the new file directory. I use cmd as the default CLI Visual Studio Code, so use vs code to open the the new folder. Another way is to open your command prompt from inside the folder. What we want o do is run python to setup the virtual environment here. I have different versions of python so need to specify which version I want to use for my virtual environment.

```
|
├──c:\Python\
         ├── python37\python.exe
         ├── python38\python.exe
         ├── python311\python.exe

```

`C:\<path to your project>\Django_ToDo_2>c:\Python\python311\python -m venv .venv`

Here's some reference material: [Creation of virtual environments](https://docs.python.org/3/library/venv.html)

Once the virtual environment has been setup, from within the project folder, activate it.
from CMD by running the activate script `.venv\Scripts\activate.bat`

`C:\<path to your project>\Django_ToDo_2>.venv\Scripts\activate.bat`

You should now be in the the virtual container:
`(.venv) C:\<path to your project>\Django_ToDo_2>`

See the reference material link above for activating the virtual environment from different CLI editors.

### Secrets: the Django Environ

Sensitive information like user name and password are stored in a .env that is named in the `.gitignore` file that is then imported referenced using [django-environ](https://pypi.org/project/django-environ/)

To access the sensitive user login details for MongoDB, first setup a .env file in the same root directory as your settings.py file. Don't forget to add the .env file to your .gitignore file so the sensitive information isn't stored with your git repository online.

Before installing any dependency files in your project, make sure that your console is within the virtual environment.
eg `(.venv) C:\<path to my application>\`

1. Install django environ from the console:

`$ pip install django-environ`

2. Import and initialize the environ settings in your settings.py file:

```python

# Import environmental variables
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

```

## Configure he Django Settings

The next step is to comment out all the Data Base configuration in the `setting.py` file. The application views in this project connect directly to the database and is no longer being managed by Django. There's no using the built in Django Admin view and nor is there any need for migrations; though I do wish that this could be the case. Django's Models and Forms help developers build more intuitive, versatile applications.

```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }

```

```python


# Get env secrets escaped according to RFC 3986
#  Connection to MongoDB
connect_string = env('MONGO_URI')


# Configure the connection string with certifi
client = MongoClient(connect_string, tlsCAFile=certifi.where())

# Define the database name
db = client.task_manager

collection = db.tasks
```

Once the connection was confirmed the first view was created.

The template rendering for `get_tasks`
![Task Manager](https://github.com/ddeveloper72/MyProjectEnvt/blob/master/MyNoSQLProj/static/img/all_tasks.jpg 'Fig 1 showing Task Manager')
