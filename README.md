### Class-1 Flask introduction 
---
- Flask installation
- helloworld page on index.route
- users page on /user/name
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


- Version-control