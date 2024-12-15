from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os


# create a Flask Instance
app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# create a form class
class NamerForm(FlaskForm):
    name = StringField("whats your name? ", validators=[DataRequired()])
    submit = SubmitField("submit")



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


# create name page
@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()

    # validation stufff
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Sucessfully")
    return render_template('name.html', name=name, form=form)

if __name__ == "__main__":
    app.run(debug=True)