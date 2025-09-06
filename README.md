## Class-1 Flask introduction 
---
- Flask installation
- helloworld page on index.route
- users page on /user/name
<br/>
Hii shubh kesa hai
<br/>

### Class-2 Templating with jinja
---
- `jinja2` = jinja2 is a templating language allows us to do very pythonic like thing on our webpages. we can utilize python on webpages via jinja.

- `fiters` = Jinja2 allows us to implement filters on values/data in webpages via using jinnja syntax on that website's html page.
```html
<!-- /user/user.html -->

<h1>Hello {{name}}</h1>
<h1>Hello {{name | upper }}</h1>
<h1>Hello {{name | lower }}</h1>
<h1>Hello {{name | capitalise }}</h1>
<h1>Hello {{name | safe  }}</h1>     <!-- it will help to pass html code into app.py as html otherwise flask/django automatically remove html injections.  -->
<h1>Hello {{name | title }}</h1>
<h1>Hello {{name | trim }}</h1>
<h1>Hello {{name | striptags }}</h1> <!-- remove html tags completely -->
```

- passing python list on webpage using jinja.
```python
# app.py
@app.route('/')
def index():
    first_name = "john"
    stuff = "This is <strong>Bold</strong>"

    favourite_pizza = ['pepporoni','cheeze','garlic',41]

    return render_template('index.html', first_name=first_name, stuff=stuff, favourite_pizza=favourite_pizza)
``` 

```html
<!-- ./templates/index.html -->
{% for i in favourite_pizza %}
    {{ i }}
{% endfor %}
```


- jinja2 syntax generally used to perform logical expressions on webpage via... 
    1. `{{data}}`= doubly curly braces for data/values.
    2. `{% %}` = for logic like loop and if/else
    3. `{% endfor/endif %}` = if logic is for loop it will end with `endfor` and if logic contains if-else it will end with `endif`   

- python datatypes things on webpages via jinja
```jinja
{% for i in favourite_pizza %}
    {% if i == 41 %}
        {{ i + 42}}
    {% else %}
        {{i}}
    {% endif%}
{% endfor %}
```
    
```jinja
{{ favourite_pizza.3 + 42}}
```
<br/>
<br/>

### Class-3 Custom errors & version control
----
- Custom error pages using in `app.py`
```python
# create custom error pages

# invalid url's
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error
@app.errorhandler(500)
def server_error(e):
    return render_template('404.html'), 500
```

```html
<!-- 404.html -->
<br>
<center>
    <h1>404 Error</h1>
    <p>Try again..</p>
</center>
``` 

```html
<!-- 500.html -->
<br>
<center>
    <h1>500, Some Internal Error</h1>
    <p>Pls Try again..</p>
</center>
```
<br/>

**Version-control**

1. create a ssh key using `ssh-keygen` in terminal and copy public ssh key and visit your github's website `profile>settings>ssh-keys>new` and add your public key there with a title. 

2. activate the virtualenv currently working on then apply this command in terminal

```bash
git config --global user.name "username"
git config --global user.email "email.id"
git config --global push.default matching
git config --global alias.co checkout
git init
git add . 
git commit -am 'commit message'
```

3. next steps are going to be on github i.e. ...
    1. go to github create a repo with some-name
    2. apply the command given by github on to terminal i.e.
```bash
git remote add origin https://github.com/user-name/flasker.git
git branch -M main
git push -u origin main
```
<br/>
<br/>

### Class-4 Templates, Bootstrap, navbar and links
---
- To implement html format globally on every html files inside templates directory we can create a `layout.html` file where we can define a layout of html page and then apply it to all webpage via jinja i.e ....

```jinja
<!-- /templates/layout.html -->
{% block content %}
    SOMECONTENT
{% endblock %}
```
```html
<!-- /templates/500.html -->
{% extends 'layout.html' %}
{% block content %}

<br>
<center>
    <h1>500 Error</h1>
    <p>Something went wrong.. try-again</p>
</center>

{% endblock%}
```
<br/>

**Bootstrap**
- It's a css-framework which can use to draw css elements which pre-built things from bootstrap using it's cdn links.

```html
<!-- /templates/navbar.html -->
<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" aria-disabled="true">Disabled</a>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
```

```html
<!-- /templates/layout.html -->
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    {% include 'navbar.html' %}
    <br/>
    <div class="container">
    {% block content %}

    {% endblock %}
    </div>
```


- `{include 'navbar.html'}` - this `jinja expression` helps to include files too and we can also use this navbar file using `{% block content %}`

- we can use `{{ url_for('index')}}` - we have to mention the the route-function from `app.py` to `navbar.html`

```html
    <li class="nav-item">
            <a class="nav-link" href="{{ url_for('user', name='') }}">User Profile</a>
    </li>
```
<br/>
<br/>

### Class-5 Webforms with WTF
---

- `wtforms` is framework agnostic form system which have different ports to other languages suchas python, js etc, now before building website from wtfforms we have to define a secret key with forms their is something we called [**csrf-token**](https://www.geeksforgeeks.org/csrf-protection-in-flask/) it will sync up behind the scene with another secret-key at server to make sure a hacker hasn't hijackjed your form.



| type of [fields](https://wtforms.readthedocs.io/en/2.3.x/fields/) | type of [validators]((https://wtforms.readthedocs.io/en/2.3.x/validators/))|
|----------------|-------------------|
|Boolean Field   |    DataRequired | 
|DateField    |Email|
|DateTimeField|EqualTo |
|DecimalField| InputRequired       | 
|FileField    |IpAddress
|HiddenField|  MacAddress   | 
|FloatField     |NumberRange| 
|FormField      |Optional| 
|IntegerField       |Regexp| 
|PasswordField    |URL| 
|RadioField   |UUID|
|SelectField      |AnyOf| 
|SelectMultipleField| Noneof| 
|SubmitField     |     
|StringField     |      
|TextAreaField     |      

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# create a Flask Instance
app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# create a form class
class NamerForm(FlaskForm):
    name = StringField("whats your name? ", validators=[DataRequired()])
    submit = SubmitField("submit")


# create name page
@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()

    # validation stufff
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('name.html', name=name, form=form)
```

```html
<!-- name.html -->
{% extends 'base.html' %}
{% block content %}

{% if name %}
    <h1>Hello {{name}}</h1>
{% else %}
    <h1>What's Your Name? </h1>
    <br/>
    <form method="post">
        {{form.hidden_tag()}}     <!--csrf-token -->
        {{form.name.label(class="form-label")}}       <!-- name lable from Namerform() class --> 
        {{form.name(class="form-control")}}       <!-- 'name' variable value from namepage method -->
    <br/>
        {{form.submit(class="btn btn-secondary")}}       <!-- submit from Namerform() class -->
    </form>
{% endif %}
{% endblock %}
```
<br/>
<br/>


### Class-6 flash messages
---
- flash is a class in flask module which can be used to flash message on screen and can be styled with bootstrap

```python
# app.py
from flask import Flask, render_template, flash
# create name page
@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()

    # validation stufff
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Sucessfully") # flash to show message at this logic point
    return render_template('name.html', name=name, form=form)
```

```html
<!-- name.html -->

{% for message in get_flashed_messages()%}
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
    <!-- looping through each character and showing message and then styling it using bootstrap -->
        {{message}}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
{%endfor%}

```
<br/>
<br/>

### Class-7 CSS, JS and images with Flask Static Files
---
- create your custom css file and override the bootstrap style for certain elements like this...
```css
/* ./static/css/style.css */
h1{
    color: darkblue;
    font-size: 60px;
}

body{
    background: #f4f4f4;
}

#demo{
    font-size: xx-large;
    color: black;
}
```
<br/>

```js
// ./static/js/myfile.js
document.getElementById('demo').innerHTML = ('This was created with javascript');
```
<br/>

```html
<!-- ./templates/base.html -->
  <!-- our css -->
<link href="{{url_for('static',filename='css/style.css')}}" rel="stylesheet">

```
<br/>

```html
<!-- ./templates/index.html -->
{% if name %}
    <h1>Hello {{name}}</h1>
    <br/>
    <img src="{{url_for('static',filename='images/img.jpg')}}" width="1100" >
    <br/>
    <p id="demo">This is  stuff</p>
    <script src="{{url_for('static',filename='js/myfile.js')}}"></script>
```
<br/>
<br/>


### Class-8 Flask with sqlite database using SQLAlchemy
----
- Before starting with sqlite we have to install a package for interacting with all type of databases i.e. `SQLAlchemy` using `pip install flask-sqlalchemy`

```python
# app.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired, Email

# Add Databse
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)


# Create Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    data_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A String
    def __repr__(self):
        return "<Name %r>" % self.name


# Create a form class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    submit = SubmitField("submit")

@app.route("/user/add", methods=["GET", "POST"])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ""
        form.email.data = ""
        flash("User Added Successfully!")

    our_users = Users.query.order_by(Users.data_added)
    return render_template("add_user.html", name=name, form=form, our_users=our_users)
  

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
<br/>

```html
<!-- ./templates/add_user.html -->
{% extends 'base.html' %}
{% block content %}

{% for message in get_flashed_messages()%}
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
    
        {{message}}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    
    </div>
{%endfor%}

{% if name %}
    <h1>User Added</h1><br/>
    <table class="table table-hover table-bordered table-striped">
        <tr>
            <td>
                {% for our_user in our_users %}
                    {{ our_user.id }}. {{ our_user.name }} - {{ our_user.email }} 
                {% endfor%}
            </td>
        </tr>
    </table>

{% else %} 
    <h1>User List:</h1><br/>
    <div class="shadow p-3 mb-5 bg-body rounded">
    <form method="post">
        {{form.hidden_tag()}}
        {{form.name.label(class="form-label")}}
        {{form.name(class="form-control")}}
        {{form.email.label(class="form-label")}}
        {{form.email(class="form-control")}<br/>
        {{form.submit(class="btn btn-secondary")}}
    </form><br/><br>
    </div>
    
{% endif %}
{% endblock %}
```
<br/>

```sql
-- ./instance/users.db

-- open terminal and type this command...
sqlite3 

-- to open a file use this command with filename i.e. users.db
.open FILENAME

-- to search for different types of table 
.tables 
.table

-- to check the schema of the table use
.schema table_name

-- to view the data/value in tables
SELECT * FROM table_name;
```
<br/><br/>


### Class-9 Flask with MySql database using SQLAlchemy
----
```python
# app.py

# Add database i.e new mysql
load_dotenv()
localhost = os.environ.get("DB_HOST")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
database = os.environ.get("DB_DATABASE")
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{user}:{password}@{localhost}/{database}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Improves performance
db = SQLAlchemy(app)

def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
```

- `create_db.py` will execute the database creation command to initialize and create database using `mysql-connector-python` package.
```python
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
mydb = mysql.connector.connect(
   host=os.environ.get('DB_HOST'),
   user=os.environ.get('DB_USER'),
   passwd=os.environ.get('DB_PASSWORD'),
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE users")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
   print(db)
```
