# My NoSQL Project

## Using Django v4.3.13 with MongoB

This project is about building Django CRUD application with MongoDB.  I already have a flask based task manager.  This project hopes to re-image this original Mini-Walk Through Project as a Django application instead.

🚧 This is currently work in progress. 🚧

The first thing to realize when starting  new project, especially this one, is that nothing is ever simple.  Some applications work straight out out of box, but in this case, I wanted a Django application which works with noSQL and so change the way that I understand Django.

I have an existing task manager application written in Python Flask that I'm rebuilding in Django.  The thought being that repurposing an existing project would be easier than building one from nothing.  Well yes it is.  There's lots of reference material to look at, but in the mean while, security on how to access a Mongo DB database ahs changed and tat application I had, no longer works.  So that had to be fixed and then the fix translated so it could be used in Django.

Off the bat, pymongo relies on the operating system’s root certificates.  I was unable to connect my application to mongoDB Atlas due to a `SSL: CERTIFICATE_VERIFY_FAILED` error.   Through a process of debugging the error logs and referencing stack overflow I eventually came to the MongoDB Developer Community guides and read the troubleshooting article 👉[here](https://www.mongodb.com/community/forums/t/serverselectiontimeouterror-ssl-certificate-verify-failed-trying-to-understand-the-origin-of-the-problem/115288).

This was how the connection string was in Flask:

```python
# To run locally, use app.config = os.getenv('MONGO_URI', 'mongodb://<username>:<password>@ds155352.mlab.com:55352/task_manager') 
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
```


The modification for use in Django required the connection string had to include an update to work with out of date OpenSSL root certificate on the host system using `tlsCAFile`.
Sensitive information like user name and password are stored in a .env that is named in the `.gitignore` file that is then imported referenced using [django-environ](https://pypi.org/project/django-environ/)

```python

import certifi
import pymongo

# Get env secrets escaped according to RFC 3986
user = env('USER')
password = env('PASSWORD')
mongo_dbname = env('MONGO_DBNAME')

# Build the connection string
connect_string = 'mongodb+srv://%s:%s@%s.8i0tx.mongodb.net/?retryWrites=true&w=majority' % (
    user, password, mongo_dbname)

# Configure the connection string with certifi
client = pymongo.MongoClient(connect_string, tlsCAFile=certifi.where())

# Define the database name
db = client['task_manager']
```

Once the connection was confirmed the first view was created.

The template rendering for `view_all_tasks`
![Task Manager](https://github.com/ddeveloper72/MyProjectEnvt/blob/master/MyNoSQLProj/static/img/all_tasks.jpg "Fig 1 showing Task Manager")