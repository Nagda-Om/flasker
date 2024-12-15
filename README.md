### Class-1 Flask introduction 
---
- Flask installation
- helloworld page on index.route
- users page on /user/name
<br/>
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
