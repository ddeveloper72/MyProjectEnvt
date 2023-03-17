# My NoSQL Project

## Using Django v4.3.13 with MongoB

This project is about building Django CRUD application with MongoDB. I already have a flask based task manager. This project hopes to re-image this original Mini-Walk Through Project as a Django application instead.

The first thing to realize when starting new project, especially this one, is that nothing is ever simple. Some applications work straight out out of box, but in this case, I wanted a Django application which works with noSQL and so change the way that I understand Django.

The thought that repurposing an existing project would be easier than building one from nothing. Well yes it is. There's lots of reference material to look at, but in the mean while, security on how to access a Mongo DB database ahs changed and that application I had, no longer works. So that had to be fixed and then the fix translated so it could be used in Django.

Off the bat, pymongo relies on the operating system’s root certificates. I was unable to connect my application to mongoDB Atlas due to a `SSL: CERTIFICATE_VERIFY_FAILED` error. Through a process of debugging the error logs and referencing stack overflow I eventually came to the MongoDB Developer Community guides and read the troubleshooting article 👉[here](https://www.mongodb.com/community/forums/t/serverselectiontimeouterror-ssl-certificate-verify-failed-trying-to-understand-the-origin-of-the-problem/115288).

This was how the connection string was in Flask:

```python
# To run locally, use app.config = os.getenv('MONGO_URI', 'mongodb://<username>:<password>@ds155352.mlab.com:55352/task_manager')
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
```

The modification for use in Django required that the connection string had to include an update to work with out of date OpenSSL root certificate on the host system using `tlsCAFile`.

## Setting Up the Django Environ

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

## Setting up the Django Application

The next step is to comment out all the Data Base configuration in the setting.py file. The application views in this project connect directly to the database and is no longer being managed by Django. There's no using the built in Django Admin view and nor is there any need for migrations; though I do wish that this could be the case. Django's Models and Forms help developers build more intuitive, versatile applications.

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
