from flask import Flask, render_template



# create a Flask Instance
app = Flask(__name__)


# create a route decorator
@app.route('/')
def index():
    first_name = "john"
    stuff = "This is <strong>Bold</strong>"

    favourite_pizza = ['pepporoni','cheeze','garlic',41]

    return render_template('index.html', first_name=first_name, stuff=stuff, favourite_pizza=favourite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# create custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error
@app.errorhandler(500)
def server_error(e):
    return render_template('404.html'), 500

